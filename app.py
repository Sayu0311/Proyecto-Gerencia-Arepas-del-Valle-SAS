import sqlite3
from datetime import date
import streamlit as st

DB = "produccion.db"


def conectar():
    return sqlite3.connect(DB)


def preparar_bd():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS rechazos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT UNIQUE NOT NULL,
            unidades_rechazadas INTEGER NOT NULL
        )
    """)

    columnas = [
        fila[1]
        for fila in cur.execute("PRAGMA table_info(rechazos)")
    ]

    if "fecha" not in columnas:
        cur.execute(
            "ALTER TABLE rechazos ADD COLUMN fecha TEXT"
        )

    # Asociar los registros existentes de las pruebas
    # a la fecha actual.
    fecha_actual = str(date.today())

    cur.execute(
        "UPDATE rechazos SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    conn.commit()
    conn.close()


def consultar_rechazos_por_periodo(fecha):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT COALESCE(SUM(unidades_rechazadas), 0)
        FROM rechazos
        WHERE fecha = ?
    """, (fecha,))

    total_rechazadas = cur.fetchone()[0]

    conn.close()

    return total_rechazadas


preparar_bd()

st.title("HU-08: Consultar unidades rechazadas por periodo")

st.write(
    "Consulta el total de unidades rechazadas registradas "
    "para un periodo seleccionado."
)

fecha_seleccionada = st.date_input(
    "Seleccione el periodo",
    value=date.today()
)

if st.button("Consultar unidades rechazadas"):

    fecha_texto = str(fecha_seleccionada)

    total_rechazadas = consultar_rechazos_por_periodo(
        fecha_texto
    )

    if total_rechazadas == 0:
        st.warning(
            "No existen unidades rechazadas registradas para el periodo seleccionado."
        )

    else:
        st.subheader(
            "Unidades rechazadas del periodo seleccionado"
        )

        st.metric(
            "Total de unidades rechazadas",
            f"{total_rechazadas} unidades"
        )

        st.success(
            "El total corresponde a los registros almacenados "
            "para el periodo seleccionado."
        )