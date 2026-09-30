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
                CHECK (unidades_rechazadas >= 0),
            fecha TEXT
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

    # Verificar si la tabla rechazos ya tenía la columna fecha
    columnas = [
        fila[1]
        for fila in cursor.execute(
            "PRAGMA table_info(rechazos)"
        )
    ]

    if "fecha" not in columnas:
        cursor.execute(
            "ALTER TABLE rechazos ADD COLUMN fecha TEXT"
        )

    # Asignar fecha actual a registros antiguos
    fecha_actual = str(date.today())

    cursor.execute(
        "UPDATE rechazos SET fecha = ? WHERE fecha IS NULL",
        (fecha_actual,)
    )

    conexion.commit()
    conexion.close()


def crear_tablas():
    crear_tabla()


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

    cursor.execute("""
        SELECT unidades_producidas
        FROM produccion
        WHERE turno = ?
    """, (turno,))

    registro = cursor.fetchone()
    conexion.close()

    return registro


def guardar_rechazo(turno, unidades_rechazadas):
    conexion = conectar_db()
    cursor = conexion.cursor()

    try:
        fecha_actual = str(date.today())

        cursor.execute(
            """
            INSERT INTO rechazos (
                turno,
                unidades_rechazadas,
                fecha
            )
            VALUES (?, ?, ?)
            """,
            (
                turno,
                unidades_rechazadas,
                fecha_actual
            )
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


def consultar_rechazos_por_periodo(fecha):
    conexion = conectar_db()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(unidades_rechazadas), 0)
        FROM rechazos
        WHERE fecha = ?
    """, (fecha,))

    total_rechazadas = cursor.fetchone()[0]

    conexion.close()

    return total_rechazadas


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