import sqlite3
from datetime import datetime
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


def crear_tablas():
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produccion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL UNIQUE,
            unidades_producidas INTEGER NOT NULL
                CHECK (unidades_producidas > 0)
        )
    """)

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

    conexion.commit()
    conexion.close()


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


crear_tablas()

st.title("Registro de tiempos y causas de paro")

st.write(
    "HU-01: Registrar tiempos y causas de paro del proceso"
)

turno = st.selectbox(
    "Seleccione el turno",
    ["Turno 1", "Turno 2", "Turno 3"],
    index=None,
    placeholder="Seleccione un turno"
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


if st.button("Guardar registro"):

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

registros = consultar_paros()

if registros:

    for (
        turno_registrado,
        inicio_registrado,
        fin_registrado,
        duracion_registrada,
        causa_registrada
    ) in registros:

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