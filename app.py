import sqlite3
from datetime import datetime, date
import streamlit as st
import pandas as pd

DB = "produccion.db"
DB_NAME = "produccion.db"


CAUSAS_PARO = [
    "Falla de máquina",
    "Falta de materia prima",
    "Cambio o ajuste de producto",
    "Limpieza",
    "Mantenimiento",
    "Falta de personal",
    "Problema de calidad",
    "Otro"
]


# ============================================================
# CONEXIÓN A BASE DE DATOS
# ============================================================

def conectar():
    return sqlite3.connect(DB)


def conectar_db():
    return conectar()


# ============================================================
# PREPARACIÓN DE BASE DE DATOS
# ============================================================

def preparar_bd():
    conn = conectar()
    cur = conn.cursor()

    # --------------------------------------------------------
    # Tabla de producción
    # --------------------------------------------------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL,
            unidades_producidas INTEGER NOT NULL
                CHECK (unidades_producidas > 0),
            fecha TEXT NOT NULL,
            UNIQUE(fecha, turno)
        )
    """)

    # --------------------------------------------------------
    # Tabla de unidades rechazadas
    # --------------------------------------------------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS rechazos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL,
            unidades_rechazadas INTEGER NOT NULL
                CHECK (unidades_rechazadas >= 0),
            fecha TEXT NOT NULL,
            UNIQUE(fecha, turno)
        )
    """)

    # --------------------------------------------------------
    # Tabla de paros
    # --------------------------------------------------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS paros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL,
            hora_inicio TEXT NOT NULL,
            hora_fin TEXT NOT NULL,
            duracion_minutos INTEGER NOT NULL
                CHECK (duracion_minutos >= 0),
            causa TEXT NOT NULL,
            fecha TEXT
        )
    """)

    # --------------------------------------------------------
    # Tabla de metas
    # --------------------------------------------------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS metas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            turno TEXT NOT NULL,
            meta INTEGER NOT NULL
                CHECK (meta > 0),
            UNIQUE(fecha, turno)
        )
    """)

    # --------------------------------------------------------
    # Agregar columna fecha a tablas existentes
    # --------------------------------------------------------
    for tabla in ["produccion", "rechazos", "paros"]:

        columnas = [
            fila[1]
            for fila in cur.execute(
                f"PRAGMA table_info({tabla})"
            )
        ]

        if "fecha" not in columnas:
            cur.execute(
                f"ALTER TABLE {tabla} ADD COLUMN fecha TEXT"
            )

    # --------------------------------------------------------
    # Asignar fecha actual a registros antiguos
    # --------------------------------------------------------
    fecha_actual = str(date.today())

    cur.execute(
        """
        UPDATE produccion
        SET fecha = ?
        WHERE fecha IS NULL
        """,
        (fecha_actual,)
    )

    cur.execute(
        """
        UPDATE rechazos
        SET fecha = ?
        WHERE fecha IS NULL
        """,
        (fecha_actual,)
    )

    cur.execute(
        """
        UPDATE paros
        SET fecha = ?
        WHERE fecha IS NULL
        """,
        (fecha_actual,)
    )

    # Migrar tablas antiguas que tenían UNIQUE(turno) a UNIQUE(fecha, turno).
    # Se reconstruyen dentro de una transacción y se preservan los registros.
    for tabla, columna_valor, restriccion in [
        ("produccion", "unidades_producidas", "CHECK (unidades_producidas > 0)"),
        ("rechazos", "unidades_rechazadas", "CHECK (unidades_rechazadas >= 0)"),
    ]:
        sql_tabla = cur.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name=?", (tabla,)
        ).fetchone()[0]
        if "turno TEXT UNIQUE" in sql_tabla or "turno TEXT UNIQUE NOT NULL" in sql_tabla:
            temporal = f"{tabla}_nueva"
            cur.execute(f"DROP TABLE IF EXISTS {temporal}")
            cur.execute(f"""CREATE TABLE {temporal} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                turno TEXT NOT NULL,
                {columna_valor} INTEGER NOT NULL {restriccion},
                fecha TEXT NOT NULL,
                UNIQUE(fecha, turno)
            )""")
            cur.execute(
                f"INSERT INTO {temporal} (id, turno, {columna_valor}, fecha) "
                f"SELECT id, turno, {columna_valor}, COALESCE(fecha, ?) FROM {tabla}",
                (fecha_actual,),
            )
            cur.execute(f"DROP TABLE {tabla}")
            cur.execute(f"ALTER TABLE {temporal} RENAME TO {tabla}")

    conn.commit()
    conn.close()


def crear_tabla():
    preparar_bd()


def crear_tablas():
    preparar_bd()


# ============================================================
# HU-05: INDICADORES
# ============================================================

def consultar_indicadores(fecha, turno):
    conn = conectar()
    cur = conn.cursor()

    # Producción real
    cur.execute("""
        SELECT COALESCE(SUM(unidades_producidas), 0)
        FROM produccion
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    produccion = cur.fetchone()[0]

    # Unidades rechazadas
    cur.execute("""
        SELECT COALESCE(SUM(unidades_rechazadas), 0)
        FROM rechazos
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    rechazadas = cur.fetchone()[0]

    # Tiempo acumulado de paro
    cur.execute("""
        SELECT COALESCE(SUM(duracion_minutos), 0)
        FROM paros
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    tiempo_paros = cur.fetchone()[0]

    conn.close()

    return produccion, rechazadas, tiempo_paros


# ============================================================
# CONSULTA DE COMPARACIÓN
# ============================================================

def consultar_comparacion(fecha, turno):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Producción real
    cursor.execute("""
        SELECT COALESCE(SUM(unidades_producidas), 0)
        FROM produccion
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    produccion_real = cursor.fetchone()[0]

    # Meta establecida
    cursor.execute("""
        SELECT meta
        FROM metas
        WHERE fecha = ? AND turno = ?
        ORDER BY id DESC
        LIMIT 1
    """, (fecha, turno))

    resultado_meta = cursor.fetchone()

    conexion.close()

    if resultado_meta is None:
        meta = None
    else:
        meta = resultado_meta[0]

    return produccion_real, meta


# ============================================================
# HU-02: PRODUCCIÓN
# ============================================================

def guardar_produccion(turno, unidades, fecha=None):
    fecha = str(fecha or date.today())
    with conectar_db() as conexion:
        try:
            conexion.execute(
                "INSERT INTO produccion (turno, unidades_producidas, fecha) VALUES (?, ?, ?)",
                (turno, unidades, fecha),
            )
            conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False



def consultar_produccion():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT fecha, turno, unidades_producidas
        FROM produccion
        ORDER BY fecha DESC, turno
    """)

    registros = cursor.fetchall()
    conexion.close()

    return registros


def consultar_produccion_turno(turno, fecha=None):
    fecha = str(fecha or date.today())
    with conectar_db() as conexion:
        return conexion.execute(
            "SELECT unidades_producidas FROM produccion WHERE turno = ? AND fecha = ? ORDER BY id DESC LIMIT 1",
            (turno, fecha),
        ).fetchone()



def guardar_rechazo(turno, unidades_rechazadas, fecha=None):
    fecha = str(fecha or date.today())
    with conectar_db() as conexion:
        try:
            conexion.execute(
                "INSERT INTO rechazos (turno, unidades_rechazadas, fecha) VALUES (?, ?, ?)",
                (turno, unidades_rechazadas, fecha),
            )
            conexion.commit()
            return True
        except sqlite3.IntegrityError:
            return False



def consultar_rechazos():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT fecha, turno, unidades_rechazadas
        FROM rechazos
        ORDER BY fecha DESC, turno
    """)

    registros = cursor.fetchall()
    conexion.close()

    return registros


def consultar_rechazos_turno(turno, fecha=None):
    fecha = str(fecha or date.today())
    with conectar_db() as conexion:
        return conexion.execute(
            "SELECT unidades_rechazadas FROM rechazos WHERE turno = ? AND fecha = ? ORDER BY id DESC LIMIT 1",
            (turno, fecha),
        ).fetchone()



def consultar_rechazos_por_periodo(fecha):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(unidades_rechazadas), 0)
        FROM rechazos
        WHERE fecha = ?
    """, (fecha,))

    total_rechazadas = cursor.fetchone()[0]

    conexion.close()

    return total_rechazadas


# ============================================================
# HU-01: PAROS
# ============================================================

def guardar_paro(
    turno,
    hora_inicio,
    hora_fin,
    duracion_minutos,
    causa,
    fecha=None
):
    conexion = conectar_db()
    cursor = conexion.cursor()

    fecha_registro = str(fecha or date.today())

    cursor.execute(
        """
        INSERT INTO paros (
            turno,
            hora_inicio,
            hora_fin,
            duracion_minutos,
            causa,
            fecha
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            turno,
            hora_inicio,
            hora_fin,
            duracion_minutos,
            causa,
            fecha_registro
        )
    )

    conexion.commit()
    conexion.close()


def consultar_paros():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            turno,
            hora_inicio,
            hora_fin,
            duracion_minutos,
            causa,
            fecha
        FROM paros
        ORDER BY fecha DESC, id DESC
    """)

    registros = cursor.fetchall()
    conexion.close()

    return registros


def consultar_paros_turno(turno, fecha=None):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT
            causa,
            hora_inicio,
            hora_fin,
            duracion_minutos
        FROM paros
        WHERE turno = ? AND fecha = ?
        ORDER BY id
        """,
        (turno, str(fecha or date.today()))
    )

    registros = cursor.fetchall()
    conexion.close()

    return registros


# ============================================================
# HU-07: CONSULTAR PRINCIPALES CAUSAS Y TIEMPOS DE PARO
# ============================================================

def consultar_paros_por_periodo(fecha):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Tiempo total de paro
    cursor.execute("""
        SELECT COALESCE(SUM(duracion_minutos), 0)
        FROM paros
        WHERE fecha = ?
    """, (fecha,))

    tiempo_total = cursor.fetchone()[0]

    # Tiempo acumulado por causa
    cursor.execute("""
        SELECT
            causa,
            SUM(duracion_minutos) AS tiempo
        FROM paros
        WHERE fecha = ?
        GROUP BY causa
        ORDER BY tiempo DESC
    """, (fecha,))

    resultados = cursor.fetchall()

    conexion.close()

    return tiempo_total, resultados


# ============================================================
# HU-09: REGISTRAR METAS DE PRODUCCIÓN POR PERIODO
# ============================================================

def consultar_meta(fecha, turno):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT meta
        FROM metas
        WHERE fecha = ? AND turno = ?
        ORDER BY id DESC
        LIMIT 1
    """, (fecha, turno))

    resultado = cursor.fetchone()

    conexion.close()

    if resultado:
        return resultado[0]

    return None


def registrar_meta(fecha, turno, meta):
    conexion = conectar_db()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO metas (
                fecha,
                turno,
                meta
            )
            VALUES (?, ?, ?)
        """, (
            fecha,
            turno,
            meta
        ))

        conexion.commit()
        resultado = True

    except sqlite3.IntegrityError:
        resultado = False

    finally:
        conexion.close()

    return resultado


# ============================================================
# INICIALIZACIÓN
# ============================================================

preparar_bd()


# ============================================================
# TÍTULO PRINCIPAL
# ============================================================

st.title(
    "Registro de información del proceso de producción"
)

st.write(
    "Sistema de registro de unidades producidas, "
    "unidades rechazadas y tiempos y causas de paro."
)


# ============================================================
# SELECCIÓN DEL TURNO
# ============================================================

turno = st.selectbox(
    "Seleccione el turno",
    ["Turno 1", "Turno 2", "Turno 3"],
    index=None,
    placeholder="Seleccione un turno"
)


fecha_operacion = st.date_input(
    "Fecha del registro de producción", value=date.today(), key="fecha_operacion"
)
fecha_operacion_texto = str(fecha_operacion)

# ============================================================
# CONSULTA DE INFORMACIÓN POR TURNO
# ============================================================

if st.button("Consultar información"):

    if turno is None:

        st.error(
            "Debe seleccionar un turno."
        )

    else:

        produccion = consultar_produccion_turno(turno, fecha_operacion_texto)
        rechazos = consultar_rechazos_turno(turno, fecha_operacion_texto)
        paros = consultar_paros_turno(turno, fecha_operacion_texto)

        tiene_informacion = (
            produccion is not None
            or rechazos is not None
            or len(paros) > 0
        )

        if not tiene_informacion:

            st.info(
                "No existen datos disponibles "
                "para el turno seleccionado."
            )

        else:

            st.subheader(
                f"Información registrada - {turno}"
            )

            # ------------------------------------------------
            # Producción
            # ------------------------------------------------

            st.write(
                "### Unidades producidas"
            )

            if produccion is not None:

                st.write(
                    f"{produccion[0]} unidades producidas"
                )

            else:

                st.warning(
                    "No existen unidades producidas "
                    "registradas para este turno."
                )

            # ------------------------------------------------
            # Rechazos
            # ------------------------------------------------

            st.write(
                "### Unidades rechazadas"
            )

            if rechazos is not None:

                st.write(
                    f"{rechazos[0]} unidades rechazadas"
                )

            else:

                st.warning(
                    "No existen unidades rechazadas "
                    "registradas para este turno."
                )

            # ------------------------------------------------
            # Paros
            # ------------------------------------------------

            st.write(
                "### Tiempos y causas de paro"
            )

            if paros:

                for (
                    causa,
                    hora_inicio,
                    hora_fin,
                    duracion
                ) in paros:

                    st.write(
                        f"**Causa:** {causa} | "
                        f"**Horario:** {hora_inicio} - {hora_fin} | "
                        f"**Duración:** {duracion} minutos"
                    )

            else:

                st.warning(
                    "No existen tiempos de paro "
                    "registrados para este turno."
                )

            # ------------------------------------------------
            # Verificación
            # ------------------------------------------------

            st.write(
                "### Verificación de consistencia"
            )

            informacion_faltante = []

            if produccion is None:

                informacion_faltante.append(
                    "unidades producidas"
                )

            if rechazos is None:

                informacion_faltante.append(
                    "unidades rechazadas"
                )

            if not paros:

                informacion_faltante.append(
                    "tiempos de paro"
                )

            if informacion_faltante:

                st.warning(
                    "Información faltante para este turno: "
                    + ", ".join(informacion_faltante)
                    + "."
                )

            else:

                st.success(
                    "La información consultada corresponde "
                    "al turno seleccionado."
                )


# ============================================================
# HU-02: REGISTRAR UNIDADES PRODUCIDAS
# ============================================================

st.subheader(
    "HU-02: Registrar unidades producidas por turno"
)

unidades_texto = st.text_input(
    "Cantidad de unidades producidas"
)

if st.button("Guardar producción"):

    if turno is None:

        st.error(
            "Debe seleccionar un turno."
        )

    elif unidades_texto.strip() == "":

        st.error(
            "Debe ingresar la cantidad de "
            "unidades producidas."
        )

    elif not unidades_texto.strip().isdigit():

        st.error(
            "La cantidad de unidades debe ser "
            "un número entero."
        )

    else:

        unidades = int(unidades_texto)

        if unidades <= 0:

            st.error(
                "La cantidad de unidades debe ser "
                "mayor que cero."
            )

        else:

            guardado = guardar_produccion(
                turno,
                unidades,
                fecha_operacion_texto
            )

            if guardado:

                st.success(
                    "Registro guardado correctamente."
                )

            else:

                st.error(
                    "Ya existe un registro para este turno."
                )


st.subheader(
    "Registros de producción almacenados"
)

registros = consultar_produccion()

if registros:

    for fecha_registrada, turno_registrado, unidades_registradas in registros:
        st.write(
            f"**{fecha_registrada} | {turno_registrado}:** "
            f"{unidades_registradas} unidades"
        )

else:

    st.info(
        "No hay registros de producción almacenados."
    )


# ============================================================
# HU-03: REGISTRAR UNIDADES RECHAZADAS
# ============================================================

st.subheader(
    "HU-03: Registrar unidades rechazadas por turno"
)

rechazos_texto = st.text_input(
    "Cantidad de unidades rechazadas"
)

if st.button("Guardar rechazo"):

    if turno is None:

        st.error(
            "Debe seleccionar un turno."
        )

    elif rechazos_texto.strip() == "":

        st.error(
            "Debe ingresar la cantidad de "
            "unidades rechazadas."
        )

    elif not rechazos_texto.strip().isdigit():

        st.error(
            "La cantidad de unidades rechazadas "
            "debe ser un número entero."
        )

    else:

        unidades_rechazadas = int(
            rechazos_texto
        )

        if unidades_rechazadas < 0:

            st.error(
                "La cantidad de unidades rechazadas "
                "no puede ser negativa."
            )

        else:

            produccion = consultar_produccion_turno(
                turno,
                fecha_operacion_texto
            )

            if produccion is None:

                st.error(
                    "No existe un registro de unidades "
                    "producidas para el turno seleccionado."
                )

            elif unidades_rechazadas > produccion[0]:

                st.error(
                    "Las unidades rechazadas no pueden "
                    "ser superiores a las unidades producidas."
                )

            else:

                guardado = guardar_rechazo(
                    turno,
                    unidades_rechazadas,
                    fecha_operacion_texto
                )

                if guardado:

                    st.success(
                        "Registro de rechazo guardado correctamente."
                    )

                else:

                    st.error(
                        "Ya existe un registro de rechazos "
                        "para este turno."
                    )


st.subheader(
    "Registros de rechazos almacenados"
)

registros_rechazos = consultar_rechazos()

if registros_rechazos:

    
    for registro_rechazo in registros_rechazos:

        fecha_registrada, turno_registrado, unidades_rechazadas_registradas = registro_rechazo

        st.write(
            f"**{fecha_registrada} - {turno_registrado}:** "
            f"{unidades_rechazadas_registradas} "
            f"unidades rechazadas"
        )

        st.write(
            f"**{turno_registrado}:** "
            f"{unidades_rechazadas_registradas} "
            f"unidades rechazadas"
        )

else:

    st.info(
        "No hay registros de rechazos almacenados."
    )


# ============================================================
# HU-01: REGISTRAR TIEMPOS Y CAUSAS DE PARO
# ============================================================

st.subheader(
    "HU-01: Registrar tiempos y causas de paro del proceso"
)

hora_inicio = st.time_input(
    "Hora de inicio del paro"
)

hora_fin = st.time_input(
    "Hora de finalización del paro"
)

causa = st.selectbox(
    "Seleccione la causa del paro",
    CAUSAS_PARO,
    index=None,
    placeholder="Seleccione una causa"
)


# ============================================================
# CALCULAR DURACIÓN
# ============================================================

if st.button("Calcular duración"):

    if turno is None:

        st.error(
            "Debe seleccionar un turno."
        )

    elif causa is None:

        st.error(
            "Debe seleccionar una causa de paro."
        )

    else:

        inicio = datetime.combine(
            datetime.today(),
            hora_inicio
        )

        fin = datetime.combine(
            datetime.today(),
            hora_fin
        )

    diferencia = fin - inicio

    duracion_minutos = int(
        diferencia.total_seconds() / 60
    )

    if duracion_minutos <= 0:
        st.error(
            "La hora de finalización debe ser posterior "
            "a la hora de inicio."
        )

        st.session_state.pop(
            "duracion_paro",
            None
        )

    else:
        st.session_state["duracion_paro"] = (
            duracion_minutos
        )

        st.session_state["horas_paro_calculadas"] = (
            hora_inicio.strftime("%H:%M"),
            hora_fin.strftime("%H:%M")
        )

        st.success(
            f"Duración del paro: "
            f"{duracion_minutos} minutos."
        )

# ============================================================
# GUARDAR PARO
# ============================================================

if st.button("Guardar registro de paro"):

    if turno is None:
        st.error("Debe seleccionar un turno.")

    elif causa is None:
        st.error("Debe seleccionar una causa de paro.")

    elif "duracion_paro" not in st.session_state:
        st.error("Debe calcular la duración antes de guardar.")

    elif st.session_state.get("horas_paro_calculadas") != (
        hora_inicio.strftime("%H:%M"),
        hora_fin.strftime("%H:%M")
    ):
        st.session_state.pop("duracion_paro", None)
        st.session_state.pop("horas_paro_calculadas", None)

        st.error(
            "Las horas cambiaron. Calcule nuevamente "
            "la duración antes de guardar."
        )

    else:
        diferencia = (
            datetime.combine(datetime.today(), hora_fin)
            - datetime.combine(datetime.today(), hora_inicio)
        )

        duracion_minutos = int(
            diferencia.total_seconds() / 60
        )

        if duracion_minutos <= 0:
            st.error(
                "La hora de finalización debe ser posterior "
                "a la hora de inicio."
            )

            st.session_state.pop("duracion_paro", None)
            st.session_state.pop("horas_paro_calculadas", None)

        else:
            guardar_paro(
                turno,
                hora_inicio.strftime("%H:%M"),
                hora_fin.strftime("%H:%M"),
                duracion_minutos,
                causa,
                fecha_operacion_texto
            )

            st.success(
                "Registro de paro guardado correctamente."
            )

            st.session_state.pop("duracion_paro", None)
            st.session_state.pop("horas_paro_calculadas", None)

# ============================================================
# REGISTROS DE PAROS
# ============================================================

st.subheader(
    "Registros de paros almacenados"
)

registros_paros = consultar_paros()

if registros_paros:

    for (
        turno_registrado,
        inicio_registrado,
        fin_registrado,
        duracion_registrada,
        causa_registrada,
        fecha_paro_registrada
    ) in registros_paros:

        st.write(
            f"**{fecha_paro_registrada} | {turno_registrado}** | "
            f"{causa_registrada} | "
            f"{inicio_registrado} - {fin_registrado} | "
            f"{duracion_registrada} minutos"
        )

else:

    st.info(
        "No hay registros de paros almacenados."
    )


# ============================================================
# HU-09: REGISTRAR METAS DE PRODUCCIÓN POR PERIODO
# ============================================================

st.subheader(
    "HU-09: Registrar metas de producción por periodo"
)

st.write(
    "Registro de metas de producción para un periodo "
    "y turno seleccionados."
)

fecha_seleccionada = st.date_input(
    "Seleccione el periodo",
    value=date.today(),
    key="fecha_meta"
)

turno_meta = st.selectbox(
    "Seleccione el turno para la meta",
    ["", "Turno 1", "Turno 2", "Turno 3"],
    key="turno_meta"
)

meta_texto = st.text_input(
    "Ingrese la meta de producción",
    placeholder="Ejemplo: 100",
    key="meta_texto"
)


# ============================================================
# REGISTRAR META
# ============================================================

if st.button("Registrar meta"):

    if not turno_meta:

        st.error(
            "Debe seleccionar un turno."
        )

    elif not meta_texto.strip():

        st.error(
            "Debe ingresar una meta de producción."
        )

    elif not meta_texto.strip().isdigit():

        st.error(
            "La meta debe ser un número entero válido."
        )

    else:

        meta = int(meta_texto)

        if meta <= 0:

            st.error(
                "La meta de producción debe ser "
                "un número entero mayor que cero."
            )

        else:

            fecha_texto = str(
                fecha_seleccionada
            )

            meta_existente = consultar_meta(
                fecha_texto,
                turno_meta
            )

            if meta_existente is not None:

                st.error(
                    "Ya existe una meta registrada "
                    "para el periodo y turno seleccionados."
                )

            else:

                guardado = registrar_meta(
                    fecha_texto,
                    turno_meta,
                    meta
                )

                if guardado:

                    st.success(
                        f"Meta de {meta} unidades "
                        f"registrada correctamente."
                    )

                else:

                    st.error(
                        "No fue posible registrar la meta. "
                        "Es posible que ya exista una meta "
                        "para ese periodo y turno."
                    )


# ============================================================
# MOSTRAR META REGISTRADA
# ============================================================

st.subheader(
    "Meta registrada"
)

if turno_meta:

    fecha_texto = str(
        fecha_seleccionada
    )

    meta_actual = consultar_meta(
        fecha_texto,
        turno_meta
    )

    if meta_actual is not None:

        st.info(
            f"Periodo: {fecha_texto} | "
            f"Turno: {turno_meta} | "
            f"Meta: {meta_actual} unidades"
        )

    else:

        st.info(
            "No existe una meta registrada "
            "para el periodo y turno seleccionados."
        )


# ============================================================
# HU-08: CONSULTAR UNIDADES RECHAZADAS POR PERIODO
# ============================================================

st.subheader(
    "HU-08: Consultar unidades rechazadas por periodo"
)

st.write(
    "Consulta el total de unidades rechazadas "
    "para un periodo seleccionado."
)

fecha_rechazos = st.date_input(
    "Seleccione el periodo para consultar rechazos",
    value=date.today(),
    key="fecha_rechazos"
)

if st.button(
    "Consultar unidades rechazadas"
):

    fecha_texto = str(
        fecha_rechazos
    )

    total_rechazadas = consultar_rechazos_por_periodo(
        fecha_texto
    )

    st.metric(
        "Unidades rechazadas",
        total_rechazadas
    )

    if total_rechazadas == 0:

        st.info(
            "No existen unidades rechazadas registradas "
            "para el periodo seleccionado."
        )

    else:

        st.success(
            f"Se registraron {total_rechazadas} "
            "unidades rechazadas en el periodo seleccionado."
        )


# ============================================================
# HU-07: CONSULTAR PRINCIPALES CAUSAS Y TIEMPOS DE PARO
# ============================================================

st.subheader(
    "HU-07: Principales causas y tiempos de paro"
)

st.write(
    "Consulta las principales causas de paro y "
    "el tiempo acumulado para un periodo seleccionado."
)

fecha_paros = st.date_input(
    "Seleccione el periodo para consultar paros",
    value=date.today(),
    key="fecha_paros"
)

if st.button(
    "Consultar causas y tiempos de paro"
):

    fecha_texto = str(
        fecha_paros
    )

    tiempo_total, resultados = consultar_paros_por_periodo(
        fecha_texto
    )

    if not resultados:

        st.warning(
            "No existen datos de paros "
            "para el periodo seleccionado."
        )

    else:

        st.subheader(
            "Información de paros del periodo seleccionado"
        )

        st.metric(
            "Tiempo total de paro",
            f"{tiempo_total} minutos"
        )

        st.subheader(
            "Causas y tiempo acumulado"
        )

        for causa_paro, tiempo in resultados:

            st.write(
                f"**{causa_paro}:** "
                f"{tiempo} minutos"
            )

        causa_principal = resultados[0][0]
        tiempo_principal = resultados[0][1]

        st.info(
            f"La causa con mayor tiempo acumulado es "
            f"**{causa_principal}**, con "
            f"{tiempo_principal} minutos."
        )

        st.success(
            "Los datos corresponden únicamente "
            "al periodo seleccionado."
        )


# ============================================================
# HU-05: CONSULTAR INDICADORES POR PERIODO Y TURNO
# ============================================================

st.subheader(
    "HU-05: Indicadores de producción por periodo y turno"
)

st.write(
    "Consulta de producción, unidades rechazadas y "
    "tiempo de paro para un periodo y turno seleccionados."
)

fecha_indicadores = st.date_input(
    "Seleccione el periodo para indicadores",
    value=date.today(),
    key="fecha_indicadores"
)

turno_indicadores = st.selectbox(
    "Seleccione el turno para consultar indicadores",
    ["", "Turno 1", "Turno 2", "Turno 3"],
    key="turno_indicadores"
)

if st.button(
    "Consultar indicadores"
):

    if not turno_indicadores:

        st.error(
            "Debe seleccionar un turno."
        )

    else:

        fecha_texto = str(
            fecha_indicadores
        )

        produccion, rechazadas, tiempo_paros = consultar_indicadores(
            fecha_texto,
            turno_indicadores
        )

        hay_datos = (
            produccion > 0
            or rechazadas > 0
            or tiempo_paros > 0
        )

        if not hay_datos:

            st.warning(
                "No existen datos disponibles para el periodo "
                "y turno seleccionados."
            )

        else:

            st.subheader(
                "Indicadores del periodo y turno seleccionado"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Producción real",
                    f"{produccion} unidades"
                )

            with col2:

                st.metric(
                    "Unidades rechazadas",
                    f"{rechazadas} unidades"
                )

            with col3:

                st.metric(
                    "Tiempo de paro",
                    f"{tiempo_paros} minutos"
                )

            st.success(
                "Los indicadores corresponden al periodo "
                "y turno seleccionados."
            )

# ============================================================
# HU-06: COMPARAR PRODUCCIÓN REAL CON META
# ============================================================
st.subheader("HU-06: Comparar producción real con meta")
st.write("Compara la producción registrada con la meta definida para la misma fecha y turno.")
fecha_comparacion = st.date_input("Fecha para comparar producción y meta", value=date.today(), key="fecha_comparacion")
turno_comparacion = st.selectbox("Turno para comparar producción y meta", ["", "Turno 1", "Turno 2", "Turno 3"], key="turno_comparacion")
if st.button("Consultar comparación HU-06"):
    if not turno_comparacion:
        st.error("Debe seleccionar un turno.")
    else:
        produccion_real, meta = consultar_comparacion(str(fecha_comparacion), turno_comparacion)
        col1, col2, col3 = st.columns(3)
        col1.metric("Producción real", f"{produccion_real} unidades")
        col2.metric("Meta", f"{meta} unidades" if meta is not None else "Sin meta")
        if meta is None:
            st.warning("No hay una meta registrada para la fecha y turno seleccionados.")
        else:
            diferencia = produccion_real - meta
            col3.metric("Diferencia frente a la meta", f"{diferencia:+d} unidades")
            if produccion_real >= meta:
                st.success("Se alcanzó o superó la meta de producción.")
            else:
                st.warning(f"Faltan {meta - produccion_real} unidades para alcanzar la meta.")

# ============================================================
# DASHBOARD GENERAL - DATOS REALES DE SQLITE
# ============================================================
st.header("Dashboard general de producción")

try:
    conexion = sqlite3.connect("produccion.db")
    produccion_df = pd.read_sql_query(
        "SELECT fecha, turno, unidades_producidas "
        "FROM produccion",
        conexion
    )
    rechazos_df = pd.read_sql_query(
        "SELECT fecha, turno, unidades_rechazadas "
        "FROM rechazos",
        conexion
    )
    paros_df = pd.read_sql_query(
        "SELECT fecha, turno, duracion_minutos AS minutos_paro FROM paros",
        conexion
    )
    metas_df = pd.read_sql_query(
        "SELECT fecha, turno, meta AS meta_produccion FROM metas",
        conexion
    )
finally:
    if "conexion" in locals():
        conexion.close()

def preparar_fecha(df):
    if not df.empty and "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
        df.dropna(subset=["fecha"], inplace=True)
    return df

for df in (produccion_df, rechazos_df, paros_df, metas_df):
    preparar_fecha(df)

if produccion_df.empty and rechazos_df.empty and paros_df.empty:
    st.info("Todavía no hay registros para mostrar en el dashboard.")
else:
    def agrupar(df, columna):
        if df.empty:
            return pd.DataFrame(columns=["fecha", columna])
        return df.groupby("fecha", as_index=False)[columna].sum()

    prod_dia = agrupar(produccion_df, "unidades_producidas")
    rech_dia = agrupar(rechazos_df, "unidades_rechazadas")
    paros_dia = agrupar(paros_df, "minutos_paro")
    meta_dia = agrupar(metas_df, "meta_produccion")

    resumen = prod_dia.merge(rech_dia, on="fecha", how="outer")
    resumen = resumen.merge(paros_dia, on="fecha", how="outer")
    resumen = resumen.merge(meta_dia, on="fecha", how="outer")
    resumen = resumen.fillna(0).sort_values("fecha")
    resumen["fecha"] = resumen["fecha"].dt.strftime("%Y-%m-%d")

    c1, c2, c3 = st.columns(3)
    c1.metric(
        "Unidades producidas",
        f"{int(resumen['unidades_producidas'].sum()):,}"
    )
    c2.metric(
        "Unidades rechazadas",
        f"{int(resumen['unidades_rechazadas'].sum()):,}"
    )
    c3.metric(
        "Minutos de paro",
        f"{int(resumen['minutos_paro'].sum()):,}"
    )

    st.subheader("Producción por día")
    graf_prod = resumen.set_index("fecha")[["unidades_producidas"]]
    if "meta_produccion" in resumen.columns and resumen["meta_produccion"].sum() > 0:
        graf_prod["meta_produccion"] = resumen["meta_produccion"].values
    st.bar_chart(graf_prod)

    st.subheader("Unidades rechazadas por día")
    st.bar_chart(resumen.set_index("fecha")[["unidades_rechazadas"]])

    st.subheader("Minutos de paro por día")
    st.bar_chart(resumen.set_index("fecha")[["minutos_paro"]])

    with st.expander("Ver resumen de datos del dashboard"):
        st.dataframe(resumen, use_container_width=True)


# ============================================================
# CARGA DE ARCHIVOS Y GENERACIÓN DE DASHBOARD
# ============================================================
st.header("Generar dashboard desde CSV o Excel")
st.write(
    "Carga un archivo para construir gráficos a partir de sus datos. "
    "Esta operación no modifica la base de datos."
)

archivo = st.file_uploader(
    "Selecciona un archivo CSV o Excel",
    type=["csv", "xlsx"]
)

if archivo is not None:
    try:
        if archivo.name.lower().endswith(".csv"):
            datos = pd.read_csv(archivo)
        else:
            datos = pd.read_excel(archivo)

        datos.columns = [
            str(col).strip().lower() for col in datos.columns
        ]

        # Admitir nombres alternativos comunes para la meta.
        alternativas_meta = [
            "meta", "meta diaria", "meta de producción",
            "meta de produccion", "unidades_meta"
        ]
        for nombre in alternativas_meta:
            if nombre in datos.columns and "meta_produccion" not in datos.columns:
                datos.rename(columns={nombre: "meta_produccion"}, inplace=True)
                break

        requeridas = [
            "fecha", "turno", "unidades_producidas",
            "unidades_rechazadas", "minutos_paro"
        ]
        faltantes = [col for col in requeridas if col not in datos.columns]

        if faltantes:
            st.error(
                "Faltan columnas obligatorias: "
                + ", ".join(faltantes)
            )
            st.caption(
                "El archivo debe incluir fecha, turno, "
                "unidades_producidas, unidades_rechazadas y minutos_paro."
            )
        else:
            datos["fecha"] = pd.to_datetime(
                datos["fecha"], errors="coerce"
            )
            datos["turno"] = datos["turno"].astype(str).str.strip()

            numericas = [
                "unidades_producidas",
                "unidades_rechazadas",
                "minutos_paro"
            ]
            if "meta_produccion" in datos.columns:
                numericas.append("meta_produccion")

            for col in numericas:
                datos[col] = pd.to_numeric(datos[col], errors="coerce")

            invalidas = (
                datos["fecha"].isna()
                | datos["turno"].isin(["", "nan", "None"])
            )
            for col in numericas:
                invalidas = invalidas | datos[col].isna() | (datos[col] < 0)

            filas_invalidas = int(invalidas.sum())
            datos = datos.loc[~invalidas].copy()

            if filas_invalidas:
                st.warning(
                    f"Se excluyeron {filas_invalidas} filas con "
                    "fechas, turnos o valores numéricos inválidos."
                )

            if datos.empty:
                st.error("No hay filas válidas para generar el dashboard.")
            else:
                st.success(
                    f"Archivo leído correctamente: {len(datos)} filas válidas."
                )
                st.subheader("Vista previa del archivo")
                st.dataframe(datos, use_container_width=True)

                resumen_archivo = datos.groupby(
                    "fecha", as_index=False
                )[numericas].sum().sort_values("fecha")

                resumen_archivo["fecha"] = (
                    resumen_archivo["fecha"].dt.strftime("%Y-%m-%d")
                )

                a, b, c = st.columns(3)
                a.metric(
                    "Unidades producidas",
                    f"{int(resumen_archivo['unidades_producidas'].sum()):,}"
                )
                b.metric(
                    "Unidades rechazadas",
                    f"{int(resumen_archivo['unidades_rechazadas'].sum()):,}"
                )
                c.metric(
                    "Minutos de paro",
                    f"{int(resumen_archivo['minutos_paro'].sum()):,}"
                )

                st.subheader("Producción del archivo por día")
                grafico_archivo = resumen_archivo.set_index("fecha")[
                    ["unidades_producidas"]
                ]
                if (
                    "meta_produccion" in resumen_archivo.columns
                    and resumen_archivo["meta_produccion"].sum() > 0
                ):
                    grafico_archivo["meta_produccion"] = (
                        resumen_archivo["meta_produccion"].values
                    )
                st.bar_chart(grafico_archivo)

                st.subheader("Rechazos del archivo por día")
                st.bar_chart(
                    resumen_archivo.set_index("fecha")[
                        ["unidades_rechazadas"]
                    ]
                )

                st.subheader("Paros del archivo por día")
                st.bar_chart(
                    resumen_archivo.set_index("fecha")[["minutos_paro"]]
                )

                st.subheader("Producción por turno")
                por_turno = datos.groupby("turno")[
                    ["unidades_producidas", "unidades_rechazadas"]
                ].sum()
                st.bar_chart(por_turno)

                with st.expander("Ver resumen agrupado por día"):
                    st.dataframe(
                        resumen_archivo, use_container_width=True
                    )

    except Exception as error:
        st.error(f"No fue posible procesar el archivo: {error}")
