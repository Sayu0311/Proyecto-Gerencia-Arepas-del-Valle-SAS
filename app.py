import sqlite3
import streamlit as st


DB_NAME = "produccion.db"


def conectar_db():
    return sqlite3.connect(DB_NAME)


def crear_tabla():
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

    conexion.commit()
    conexion.close()


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


crear_tabla()

st.title("Registro de unidades producidas")

st.write("HU-02: Registrar unidades producidas por turno")

turno = st.selectbox(
    "Seleccione el turno",
    ["Turno 1", "Turno 2", "Turno 3"],
    index=None,
    placeholder="Seleccione un turno"
)

unidades_texto = st.text_input(
    "Cantidad de unidades producidas"
)

if st.button("Guardar registro"):

    if turno is None:
        st.error("Debe seleccionar un turno.")

    elif unidades_texto.strip() == "":
        st.error("Debe ingresar la cantidad de unidades producidas.")

    elif not unidades_texto.strip().isdigit():
        st.error("La cantidad de unidades debe ser un número entero.")

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


st.subheader("Registros almacenados")

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
