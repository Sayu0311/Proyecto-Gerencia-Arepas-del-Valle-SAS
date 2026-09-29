import sqlite3
from datetime import date
import streamlit as st

DB = "produccion.db"


def conectar():
    return sqlite3.connect(DB)


def preparar_bd():
    conn = conectar()
    cur = conn.cursor()

    # Tabla de producción
    cur.execute("""
        CREATE TABLE IF NOT EXISTS produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT UNIQUE NOT NULL,
            unidades_producidas INTEGER NOT NULL
        )
    """)

    # Tabla de unidades rechazadas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS rechazos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT UNIQUE NOT NULL,
            unidades_rechazadas INTEGER NOT NULL
        )
    """)

    # Tabla de paros
    cur.execute("""
        CREATE TABLE IF NOT EXISTS paros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL,
            hora_inicio TEXT NOT NULL,
            hora_fin TEXT NOT NULL,
            duracion_minutos INTEGER NOT NULL,
            causa TEXT NOT NULL
        )
    """)

    # Agregar fecha a las tablas si todavía no existe
    for tabla in ["produccion", "rechazos", "paros"]:
        columnas = [
            fila[1]
            for fila in cur.execute(f"PRAGMA table_info({tabla})")
        ]

        if "fecha" not in columnas:
            cur.execute(
                f"ALTER TABLE {tabla} ADD COLUMN fecha TEXT"
            )

    # Los registros existentes de las pruebas anteriores
    # se asocian a la fecha actual para poder consultarlos
    # por periodo.
    fecha_actual = str(date.today())

    cur.execute(
        "UPDATE produccion SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    cur.execute(
        "UPDATE rechazos SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    cur.execute(
        "UPDATE paros SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    conn.commit()
    conn.close()


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


# Preparar la base de datos
preparar_bd()


# Interfaz
st.title("HU-05: Indicadores de producción por periodo y turno")

st.write(
    "Consulta de producción, unidades rechazadas y tiempo de paro "
    "para un periodo y turno seleccionados."
)

# Selección del periodo
fecha_seleccionada = st.date_input(
    "Seleccione el periodo",
    value=date.today()
)

# Selección del turno
turno = st.selectbox(
    "Seleccione el turno",
    ["", "Turno 1", "Turno 2", "Turno 3"]
)

# Consulta
if st.button("Consultar indicadores"):

    if not turno:
        st.error("Debe seleccionar un turno.")

    else:
        fecha_texto = str(fecha_seleccionada)

        produccion, rechazadas, tiempo_paros = consultar_indicadores(
            fecha_texto,
            turno
        )

        hay_datos = (
            produccion > 0
            or rechazadas > 0
            or tiempo_paros > 0
        )

        if not hay_datos:

            st.warning(
                "No existen datos disponibles para el periodo y turno seleccionados."
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
                "Los indicadores corresponden al periodo y turno seleccionados."
            )