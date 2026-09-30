cat > Historias-de-Usuario/Pruebas-HU-06.md <<'EOF'
# Pruebas HU-06: Comparar producción real con metas establecidas

## Historia de Usuario
HU-06: Comparar producción real con metas establecidas.

## Evidencias de prueba

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje indicando que debe seleccionar un turno | Se mostró "Debe seleccionar un turno." | PASS |
| Turno 1 sin meta | Informar que no existe una meta establecida | Se mostró "No existe una meta establecida para el periodo y turno seleccionados." | PASS |
| Producción 100, meta 120 | Identificar producción por debajo de la meta y mostrar diferencia | Producción: 100, meta: 120, diferencia: -20. Se indicó que estaba por debajo de la meta | PASS |
| Producción 100, meta 100 | Identificar producción igual a la meta | Producción: 100, meta: 100, diferencia: 0. Se indicó que era igual a la meta | PASS |
| Producción 100, meta 80 | Identificar producción por encima de la meta y mostrar diferencia | Producción: 100, meta: 80, diferencia: 20. Se indicó que estaba por encima de la meta | PASS |

## Validaciones realizadas

- Se puede seleccionar el periodo y turno para realizar la comparación.
- Se consulta la producción real almacenada.
- Se consulta la meta establecida para el mismo periodo y turno.
- Se calcula la diferencia entre producción real y meta.
- Se identifica si la producción está por debajo, igual o por encima de la meta.
- No se realiza la comparación cuando no existe una meta.
- No se realiza la comparación cuando no existen datos de producción.

## Observación

Las metas utilizadas para las pruebas fueron datos de prueba registrados temporalmente en la tabla de metas. El registro de metas corresponde a la HU-09.
EOF