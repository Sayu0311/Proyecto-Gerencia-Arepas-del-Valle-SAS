import sqlite3
from datetime import datetime, date
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

    # HU-02: producción
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL UNIQUE,
            unidades_producidas INTEGER NOT NULL
                CHECK (unidades_producidas > 0)
        )
    """)

    # HU-03: rechazos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rechazos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL UNIQUE,
            unidades_rechazadas INTEGER NOT NULL
                CHECK (unidades_rechazadas >= 0)
        )
    """)

    # HU-01: paros
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

    # HU-07 necesita fecha para consultar por periodo.
    columnas = [
        fila[1]
        for fila in cursor.execute("PRAGMA table_info(paros)")
    ]

    if "fecha" not in columnas:
        cursor.execute(
            "ALTER TABLE paros ADD COLUMN fecha TEXT"
        )

    # Los registros anteriores quedan asociados a la fecha actual.
    fecha_actual = str(date.today())

    cursor.execute(
        "UPDATE paros SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    conexion.commit()
    conexion.close()


def crear_tablas():
    crear_tabla()


# ============================================================
# HU-02: REGISTRAR UNIDADES PRODUCIDAS
# ============================================================

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

    cursor.execute(
        """
        SELECT unidades_producidas
        FROM produccion
        WHERE turno = ?
        """,
        (turno,)
    )

    registro = cursor.fetchone()
    conexion.close()

    return registro


# ============================================================
# HU-03: REGISTRAR UNIDADES RECHAZADAS
# ============================================================

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


def consultar_rechazos_turno(turno):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT unidades_rechazadas
        FROM rechazos
        WHERE turno = ?
        """,
        (turno,)
    )

    registro = cursor.fetchone()
    conexion.close()

    return registro


# ============================================================
# HU-01: REGISTRAR TIEMPOS Y CAUSAS DE PARO
# ============================================================

def guardar_paro(
    turno,
    hora_inicio,
    hora_fin,
    duracion_minutos,
    causa
):
    conexion = conectar_db()
    cursor = conexion.cursor()

    fecha_registro = str(date.today())

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
            causa
        FROM paros
        ORDER BY id
    """)

    registros = cursor.fetchall()
    conexion.close()

    return registros


def consultar_paros_turno(turno):
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
        WHERE turno = ?
        ORDER BY id
        """,
        (turno,)
    )

    registros = cursor.fetchall()
    conexion.close()

    return registros


# ============================================================
# HU-07: CONSULTAR CAUSAS Y TIEMPOS DE PARO POR PERIODO
# ============================================================

def consultar_paros_por_periodo(fecha):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Tiempo total de paro del periodo
    cursor.execute("""
        SELECT COALESCE(SUM(duracion_minutos), 0)
        FROM paros
        WHERE fecha = ?
    """, (fecha,))

    tiempo_total = cursor.fetchone()[0]

    # Causas y tiempo acumulado por causa
    cursor.execute("""
        SELECT causa, SUM(duracion_minutos) AS tiempo
        FROM paros
        WHERE fecha = ?
        GROUP BY causa
        ORDER BY tiempo DESC
    """)

    resultados = cursor.fetchall()

    conexion.close()

    return tiempo_total, resultados


# ============================================================
# INICIALIZACIÓN
# ============================================================

crear_tablas()


# ============================================================
# HU-04: CONSULTAR INFORMACIÓN POR TURNO
# ============================================================

st.title("Consulta de información por turno")

st.write(
    "HU-04: Consultar información registrada por turno"
)


turno = st.selectbox(
    "Seleccione el turno que desea consultar",
    ["Turno 1", "Turno 2", "Turno 3"],
    index=None,
    placeholder="Seleccione un turno"
)


if st.button("Consultar información"):

    if turno is None:

        st.error("Debe seleccionar un turno.")

    else:

        produccion = consultar_produccion_turno(turno)
        rechazos = consultar_rechazos_turno(turno)
        paros = consultar_paros_turno(turno)

        tiene_informacion = (
            produccion is not None
            or rechazos is not None
            or len(paros) > 0
        )

        if not tiene_informacion:

            st.info(
                "No existen datos disponibles para el turno seleccionado."
            )

        else:

            st.subheader(
                f"Información registrada - {turno}"
            )

            st.write("### Unidades producidas")

            if produccion is not None:

                st.write(
                    f"{produccion[0]} unidades producidas"
                )

            else:

                st.warning(
                    "No existen unidades producidas registradas "
                    "para este turno."
                )


            st.write("### Unidades rechazadas")

            if rechazos is not None:

                st.write(
                    f"{rechazos[0]} unidades rechazadas"
                )

            else:

                st.warning(
                    "No existen unidades rechazadas registradas "
                    "para este turno."
                )


            st.write("### Tiempos y causas de paro")

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
                    "No existen tiempos de paro registrados "
                    "para este turno."
                )


            st.write("### Verificación de consistencia")

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
# HU-07: CONSULTAR PRINCIPALES CAUSAS Y TIEMPOS DE PARO
# ============================================================

st.subheader("HU-07: Principales causas y tiempos de paro")

st.write(
    "Consulta las principales causas de paro y el tiempo acumulado "
    "para un periodo seleccionado."
)

fecha_seleccionada = st.date_input(
    "Seleccione el periodo",
    value=date.today()
)


if st.button("Consultar causas y tiempos de paro"):

    fecha_texto = str(fecha_seleccionada)

    tiempo_total, resultados = consultar_paros_por_periodo(
        fecha_texto
    )

    if not resultados:

        st.warning(
            "No existen datos de paros para el periodo seleccionado."
        )

    else:

        st.subheader(
            "Información de paros del periodo seleccionado"
        )

        st.metric(
            "Tiempo total de paro",
            f"{tiempo_total} minutos"
        )

        st.subheader("Causas y tiempo acumulado")

        for causa, tiempo in resultados:

            st.write(
                f"**{causa}:** {tiempo} minutos"
            )

        causa_principal = resultados[0][0]
        tiempo_principal = resultados[0][1]

        st.info(
            f"La causa con mayor tiempo acumulado es "
            f"**{causa_principal}**, con {tiempo_principal} minutos."
        )

        st.success(
            "Los datos corresponden únicamente al periodo seleccionado."
        )