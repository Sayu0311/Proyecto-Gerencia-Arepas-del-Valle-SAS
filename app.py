def consultar_comparacion(fecha, turno):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Producción real
    cursor.execute("""
        SELECT COALESCE(SUM(unidades_producidas), 0)
        FROM produccion
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    produccion_real = cursor.fetchone()[0]

    # Meta establecida
    cursor.execute("""
        SELECT meta
        FROM metas
        WHERE fecha = ? AND turno = ?
    """, (fecha, turno))

    resultado_meta = cursor.fetchone()

    conexion.close()

    if resultado_meta is None:
        meta = None
    else:
        meta = resultado_meta[0]

    return produccion_real, meta


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