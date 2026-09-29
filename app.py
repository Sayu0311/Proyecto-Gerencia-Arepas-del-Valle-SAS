import sqlite3
import streamlit as st


DB_NAME = "produccion.db"


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
        CREATE TABLE IF NOT EXISTS rechazos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            turno TEXT NOT NULL UNIQUE,
            unidades_rechazadas INTEGER NOT NULL
                CHECK (unidades_rechazadas >= 0)
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


crear_tablas()

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