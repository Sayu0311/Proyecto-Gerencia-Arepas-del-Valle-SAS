cat > Historias-de-Usuario/Pruebas-HU-05.md <<'EOF'
# Pruebas HU-05: Consultar indicadores de producción por periodo y turno

## Historia de Usuario
HU-05: Consultar indicadores de producción por periodo y turno.

## Evidencias de prueba

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje indicando que debe seleccionar un turno | Se mostró "Debe seleccionar un turno." | PASS |
| Consultar 29/09/2026 - Turno 1 | Mostrar producción, rechazados y tiempo de paro del periodo y turno | Producción: 100 unidades, rechazadas: 0 unidades, tiempo de paro: 45 minutos | PASS |
| Consultar 29/09/2026 - Turno 2 | Mostrar únicamente los indicadores del Turno 2 | Producción: 200 unidades, rechazadas: 20 unidades, tiempo de paro: 0 minutos | PASS |
| Consultar 29/09/2026 - Turno 3 | Mostrar mensaje cuando no existen datos | Se mostró "No existen datos disponibles para el periodo y turno seleccionados." | PASS |
| Consultar 28/09/2026 - Turno 1 | Mostrar mensaje cuando no existen datos para el periodo | Se mostró "No existen datos disponibles para el periodo y turno seleccionados." | PASS |

## Validaciones realizadas

- Se puede seleccionar un periodo y un turno.
- Los indicadores se actualizan según el periodo y turno seleccionados.
- Se muestra la producción real.
- Se muestran las unidades rechazadas.
- Se muestra el tiempo acumulado de paro.
- No se muestran datos de otros turnos.
- Cuando no existen datos para el periodo y turno seleccionados, se muestra un mensaje informativo.

## Observación

Las pruebas utilizaron los registros generados durante las pruebas de HU-01, HU-02 y HU-03. Los datos existentes fueron asociados a la fecha de prueba 29/09/2026 para permitir la consulta por periodo.
EOF