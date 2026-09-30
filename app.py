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
        CREATE TABLE IF NOT EXISTS metas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            turno TEXT NOT NULL,
            meta INTEGER NOT NULL,
            UNIQUE(fecha, turno)
        )
    """)

    conn.commit()
    conn.close()


def consultar_meta(fecha, turno):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT meta
        FROM metas
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    resultado = cur.fetchone()

    conn.close()

    return resultado[0] if resultado else None


def registrar_meta(fecha, turno, meta):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO metas (fecha, turno, meta)
        VALUES (?, ?, ?)
    """, (fecha, turno, meta))

    conn.commit()
    conn.close()


preparar_bd()

st.title("HU-09: Registrar metas de producción por periodo")

st.write(
    "Registro de metas de producción para un periodo y turno seleccionados."
)

fecha_seleccionada = st.date_input(
    "Seleccione el periodo",
    value=date.today()
)

turno = st.selectbox(
    "Seleccione el turno",
    ["", "Turno 1", "Turno 2", "Turno 3"]
)

meta_texto = st.text_input(
    "Ingrese la meta de producción",
    placeholder="Ejemplo: 100"
)

if st.button("Registrar meta"):

    if not turno:
        st.error("Debe seleccionar un turno.")

    elif not meta_texto.strip():
        st.error("Debe ingresar una meta de producción.")

    else:
        try:
            meta = int(meta_texto)

            if meta <= 0:
                st.error(
                    "La meta de producción debe ser un número entero mayor que cero."
                )

            else:
                fecha_texto = str(fecha_seleccionada)

                meta_existente = consultar_meta(
                    fecha_texto,
                    turno
                )

                if meta_existente is not None:
                    st.error(
                        "Ya existe una meta registrada para el periodo y turno seleccionados."
                    )

                else:
                    registrar_meta(
                        fecha_texto,
                        turno,
                        meta
                    )

                    st.success(
                        f"Meta de {meta} unidades registrada correctamente."
                    )

        except ValueError:
            st.error(
                "La meta debe ser un número entero válido."
            )


st.subheader("Meta registrada")

if turno:
    fecha_texto = str(fecha_seleccionada)

    meta_actual = consultar_meta(
        fecha_texto,
        turno
    )

    if meta_actual is not None:
        st.info(
            f"Periodo: {fecha_texto} | "
            f"Turno: {turno} | "
            f"Meta: {meta_actual} unidades"
        )