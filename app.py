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

    conexion.commit()
    conexion.close()


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


crear_tablas()

st.title("Registro de unidades rechazadas")

st.write(
    "HU-03: Registrar unidades rechazadas por turno"
)

turno = st.selectbox(
    "Seleccione el turno",
    ["Turno 1", "Turno 2", "Turno 3"],
    index=None,
    placeholder="Seleccione un turno"
)

unidades_texto = st.text_input(
    "Cantidad de unidades rechazadas"
)

if st.button("Guardar rechazo"):

    if turno is None:
        st.error("Debe seleccionar un turno.")

    elif unidades_texto.strip() == "":
        st.error(
            "Debe ingresar la cantidad de unidades rechazadas."
        )

    elif not unidades_texto.strip().isdigit():
        st.error(
            "La cantidad de unidades rechazadas "
            "debe ser un número entero."
        )

    else:
        unidades_rechazadas = int(unidades_texto)

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

registros = consultar_rechazos()

if registros:

    for turno_registrado, unidades_registradas in registros:

        st.write(
            f"**{turno_registrado}:** "
            f"{unidades_registradas} unidades rechazadas"
        )

else:
    st.info(
        "No hay registros de rechazos almacenados."
    )
    