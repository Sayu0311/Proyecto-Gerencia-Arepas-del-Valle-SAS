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

    # Tabla de metas de producción
    cur.execute("""
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
            for fila in cur.execute(f"PRAGMA table_info({tabla})")
        ]

        if "fecha" not in columnas:
            cur.execute(
                f"ALTER TABLE {tabla} ADD COLUMN fecha TEXT"
            )

    # Asociar los registros existentes a la fecha actual
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


def consultar_comparacion(fecha, turno):
    conn = conectar()
    cur = conn.cursor()

    # Producción real
    cur.execute("""
        SELECT COALESCE(SUM(unidades_producidas), 0)
        FROM produccion
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    produccion_real = cur.fetchone()[0]

    # Meta establecida
    cur.execute("""
        SELECT meta
        FROM metas
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    resultado_meta = cur.fetchone()

    conn.close()

    if resultado_meta is None:
        meta = None
    else:
        meta = resultado_meta[0]

    return produccion_real, meta


preparar_bd()

st.title("HU-06: Comparación de producción real con metas")

st.write(
    "Consulta la producción real y la compara con la meta establecida "
    "para el periodo y turno seleccionados."
)

fecha_seleccionada = st.date_input(
    "Seleccione el periodo",
    value=date.today()
)

turno = st.selectbox(
    "Seleccione el turno",
    ["", "Turno 1", "Turno 2", "Turno 3"]
)

if st.button("Comparar producción"):

    if not turno:
        st.error("Debe seleccionar un turno.")

    else:
        fecha_texto = str(fecha_seleccionada)

        produccion_real, meta = consultar_comparacion(
            fecha_texto,
            turno
        )

        # No se puede realizar la comparación sin meta
        if meta is None:
            st.warning(
                "No existe una meta establecida para el periodo y turno seleccionados."
            )

        # No se puede realizar la comparación sin producción
        elif produccion_real == 0:
            st.warning(
                "No existen datos de producción real para el periodo y turno seleccionados."
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
                    "La producción real está por debajo de la meta establecida."
                )

            elif produccion_real == meta:
                st.success(
                    "La producción real es igual a la meta establecida."
                )

            else:
                st.success(
                    "La producción real está por encima de la meta establecida."
                )