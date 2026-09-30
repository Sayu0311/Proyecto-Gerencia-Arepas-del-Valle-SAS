import sqlite3
from datetime import date, datetime
import streamlit as st


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


def conectar_db():
    return sqlite3.connect(DB_NAME)


def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Tabla de producción
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL UNIQUE,
            unidades_producidas INTEGER NOT NULL
                CHECK (unidades_producidas > 0)
        )
    """)

    # Tabla de unidades rechazadas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rechazos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL UNIQUE,
            unidades_rechazadas INTEGER NOT NULL
                CHECK (unidades_rechazadas >= 0)
        )
    """)

    # Tabla de paros
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS paros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL,
            hora_inicio TEXT NOT NULL,
            hora_fin TEXT NOT NULL,
            duracion_minutos INTEGER NOT NULL
                CHECK (duracion_minutos >= 0),
            causa TEXT NOT NULL
        )
    """)

    # Tabla de metas de producción
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            turno TEXT NOT NULL,
            meta INTEGER NOT NULL,
            UNIQUE(fecha, turno)
        )
    """)

    # Agregar fecha a las tablas existentes si todavía no existe
    for tabla in ["produccion", "rechazos", "paros"]:
        columnas = [
            fila[1]
            for fila in cursor.execute(
                f"PRAGMA table_info({tabla})"
            )
        ]

        if "fecha" not in columnas:
            cursor.execute(
                f"ALTER TABLE {tabla} ADD COLUMN fecha TEXT"
            )

    # Asociar los registros existentes a la fecha actual
    fecha_actual = str(date.today())

    cursor.execute(
        "UPDATE produccion SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    cursor.execute(
        "UPDATE rechazos SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    cursor.execute(
        "UPDATE paros SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    conexion.commit()
    conexion.close()


def crear_tablas():
    crear_tabla()


def guardar_produccion(turno, unidades):
    conexion = conectar_db()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO produccion (turno, unidades_producidas)
            VALUES (?, ?)
            """,
            (turno, unidades)
        )

        conexion.commit()
        resultado = True

    except sqlite3.IntegrityError:
        resultado = False

    finally:
        conexion.close()

    return resultado


def consultar_produccion():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT turno, unidades_producidas
        FROM produccion
        ORDER BY turno
    """)

    registros = cursor.fetchall()
    conexion.close()

    return registros


def consultar_produccion_turno(turno):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT unidades_producidas
        FROM produccion
        WHERE turno = ?
    """, (turno,))

    registro = cursor.fetchone()
    conexion.close()

    return registro


def guardar_rechazo(turno, unidades_rechazadas):
    conexion = conectar_db()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO rechazos (turno, unidades_rechazadas)
            VALUES (?, ?)
            """,
            (turno, unidades_rechazadas)
        )

        conexion.commit()
        resultado = True

    except sqlite3.IntegrityError:
        resultado = False

    finally:
        conexion.close()

    return resultado


def consultar_rechazos():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT turno, unidades_rechazadas
        FROM rechazos
        ORDER BY turno
    """)

    registros = cursor.fetchall()
    conexion.close()

    return registros


def guardar_paro(
    turno,
    hora_inicio,
    hora_fin,
    duracion_minutos,
    causa
):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO paros (
            turno,
            hora_inicio,
            hora_fin,
            duracion_minutos,
            causa
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            turno,
            hora_inicio,
            hora_fin,
            duracion_minutos,
            causa
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
            causa
        FROM paros
        ORDER BY id
    """)

    registros = cursor.fetchall()
    conexion.close()

    return registros


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
    """, (fecha, turno))

    resultado_meta = cursor.fetchone()

    conexion.close()

    if resultado_meta is None:
        meta = None
    else:
        meta = resultado_meta[0]

    return produccion_real, meta


# ============================================================
# INICIALIZACIÓN
# ============================================================

crear_tabla()


# ============================================================
# TÍTULO PRINCIPAL
# ============================================================

st.title("Registro de información del proceso de producción")

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


# ============================================================
# HU-02: REGISTRAR UNIDADES PRODUCIDAS
# ============================================================

st.subheader("HU-02: Registrar unidades producidas por turno")

unidades_texto = st.text_input(
    "Cantidad de unidades producidas"
)

if st.button("Guardar producción"):

    if turno is None:
        st.error("Debe seleccionar un turno.")

    elif unidades_texto.strip() == "":
        st.error(
            "Debe ingresar la cantidad de unidades producidas."
        )

    elif not unidades_texto.strip().isdigit():
        st.error(
            "La cantidad de unidades debe ser un número entero."
        )

    else:
        unidades = int(unidades_texto)

        if unidades <= 0:
            st.error(
                "La cantidad de unidades debe ser mayor que cero."
            )

        else:
            guardado = guardar_produccion(
                turno,
                unidades
            )

            if guardado:
                st.success(
                    "Registro guardado correctamente."
                )
            else:
                st.error(
                    "Ya existe un registro para este turno."
                )


st.subheader("Registros de producción almacenados")

registros = consultar_produccion()

if registros:

    for turno_registrado, unidades_registradas in registros:

        st.write(
            f"**{turno_registrado}:** "
            f"{unidades_registradas} unidades"
        )

else:
    st.info(
        "No hay registros de producción almacenados."
    )


# ============================================================
# HU-03: REGISTRAR UNIDADES RECHAZADAS
# ============================================================

st.subheader("HU-03: Registrar unidades rechazadas por turno")

rechazos_texto = st.text_input(
    "Cantidad de unidades rechazadas"
)

if st.button("Guardar rechazo"):

    if turno is None:
        st.error("Debe seleccionar un turno.")

    elif rechazos_texto.strip() == "":
        st.error(
            "Debe ingresar la cantidad de unidades rechazadas."
        )

    elif not rechazos_texto.strip().isdigit():
        st.error(
            "La cantidad de unidades rechazadas "
            "debe ser un número entero."
        )

    else:
        unidades_rechazadas = int(rechazos_texto)

        if unidades_rechazadas < 0:
            st.error(
                "La cantidad de unidades rechazadas "
                "no puede ser negativa."
            )

        else:
            produccion = consultar_produccion_turno(turno)

            if produccion is None:
                st.error(
                    "No existe un registro de unidades producidas "
                    "para el turno seleccionado."
                )

            elif unidades_rechazadas > produccion[0]:
                st.error(
                    "Las unidades rechazadas no pueden ser "
                    "superiores a las unidades producidas."
                )

            else:
                guardado = guardar_rechazo(
                    turno,
                    unidades_rechazadas
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


st.subheader("Registros de rechazos almacenados")

registros_rechazos = consultar_rechazos()

if registros_rechazos:

    for (
        turno_registrado,
        unidades_rechazadas_registradas
    ) in registros_rechazos:

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

if st.button("Calcular duración"):

    if turno is None:
        st.error("Debe seleccionar un turno.")

    elif causa is None:
        st.error("Debe seleccionar una causa de paro.")

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

        if duracion_minutos < 0:
            st.error(
                "La hora de finalización no puede ser "
                "anterior a la hora de inicio."
            )

        else:
            st.session_state["duracion_paro"] = duracion_minutos

            st.success(
                f"Duración del paro: "
                f"{duracion_minutos} minutos."
            )


if st.button("Guardar registro de paro"):

    if turno is None:
        st.error("Debe seleccionar un turno.")

    elif causa is None:
        st.error("Debe seleccionar una causa de paro.")

    elif "duracion_paro" not in st.session_state:
        st.error(
            "Debe calcular la duración antes de guardar."
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

        duracion_minutos = int(
            (fin - inicio).total_seconds() / 60
        )

        if duracion_minutos < 0:
            st.error(
                "La hora de finalización no puede ser "
                "anterior a la hora de inicio."
            )

        else:
            guardar_paro(
                turno,
                hora_inicio.strftime("%H:%M"),
                hora_fin.strftime("%H:%M"),
                duracion_minutos,
                causa
            )

            st.success(
                "Registro de paro guardado correctamente."
            )

            st.session_state.pop(
                "duracion_paro",
                None
            )


st.subheader("Registros de paros almacenados")

registros_paros = consultar_paros()

if registros_paros:

    for (
        turno_registrado,
        inicio_registrado,
        fin_registrado,
        duracion_registrada,
        causa_registrada
    ) in registros_paros:

        st.write(
            f"**{turno_registrado}** | "
            f"{causa_registrada} | "
            f"{inicio_registrado} - {fin_registrado} | "
            f"{duracion_registrada} minutos"
        )

else:
    st.info(
        "No hay registros de paros almacenados."
    )


# ============================================================
# HU-06: COMPARAR PRODUCCIÓN REAL CON METAS
# ============================================================

st.subheader(
    "HU-06: Comparación de producción real con metas"
)

st.write(
    "Consulta la producción real y la compara con la meta "
    "establecida para el periodo y turno seleccionados."
)

fecha_seleccionada = st.date_input(
    "Seleccione el periodo",
    value=date.today()
)

turno_comparacion = st.selectbox(
    "Seleccione el turno para la comparación",
    ["", "Turno 1", "Turno 2", "Turno 3"]
)

if st.button("Comparar producción"):

    if not turno_comparacion:
        st.error("Debe seleccionar un turno.")

    else:
        fecha_texto = str(fecha_seleccionada)

        produccion_real, meta = consultar_comparacion(
            fecha_texto,
            turno_comparacion
        )

        if meta is None:
            st.warning(
                "No existe una meta establecida para el periodo "
                "y turno seleccionados."
            )

        elif produccion_real == 0:
            st.warning(
                "No existen datos de producción real para el "
                "periodo y turno seleccionados."
            )

        else:
            diferencia = produccion_real - meta

            st.subheader(
                "Comparación del periodo y turno seleccionado"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Producción real",
                    f"{produccion_real} unidades"
                )

            with col2:
                st.metric(
                    "Meta establecida",
                    f"{meta} unidades"
                )

            with col3:
                st.metric(
                    "Diferencia",
                    f"{diferencia} unidades"
                )

            if produccion_real < meta:
                st.info(
                    "La producción real está por debajo "
                    "de la meta establecida."
                )

            elif produccion_real == meta:
                st.success(
                    "La producción real es igual a "
                    "la meta establecida."
                )

            else:
                st.success(
                    "La producción real está por encima "
                    "de la meta establecida."
                )