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
        CREATE TABLE IF NOT EXISTS paros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL,
            hora_inicio TEXT NOT NULL,
            hora_fin TEXT NOT NULL,
            duracion_minutos INTEGER NOT NULL,
            causa TEXT NOT NULL
        )
    """)

    columnas = [
        fila[1]
        for fila in cur.execute("PRAGMA table_info(paros)")
    ]

    if "fecha" not in columnas:
        cur.execute(
            "ALTER TABLE paros ADD COLUMN fecha TEXT"
        )

    # Asociar los registros existentes de las pruebas
    # a la fecha actual.
    fecha_actual = str(date.today())

    cur.execute(
        "UPDATE paros SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    conn.commit()
    conn.close()


def consultar_paros_por_periodo(fecha):
    conn = conectar()
    cur = conn.cursor()

    # Tiempo total de paro del periodo
    cur.execute("""
        SELECT COALESCE(SUM(duracion_minutos), 0)
        FROM paros
        WHERE fecha = ?
    """, (fecha,))

    tiempo_total = cur.fetchone()[0]

    # Causas y tiempo acumulado por causa
    cur.execute("""
        SELECT causa, SUM(duracion_minutos) AS tiempo
        FROM paros
        WHERE fecha = ?
        GROUP BY causa
        ORDER BY tiempo DESC
    """, (fecha,))

    resultados = cur.fetchall()

    conn.close()

    return tiempo_total, resultados


preparar_bd()

st.title("HU-07: Principales causas y tiempos de paro")

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