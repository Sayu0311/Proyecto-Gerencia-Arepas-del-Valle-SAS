# Pruebas HU-08: Consultar unidades rechazadas por periodo

## Historia de Usuario
HU-08: Consultar unidades rechazadas por periodo.

## Evidencias de prueba

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| Consultar 29/09/2026 con registros | Mostrar el total de unidades rechazadas del periodo | Se mostraron 20 unidades rechazadas | PASS |
| Consultar 28/09/2026 sin registros | Mostrar mensaje cuando no existen unidades rechazadas para el periodo | Se mostró "No existen unidades rechazadas registradas para el periodo seleccionado." | PASS |

## Validaciones realizadas

- Se puede seleccionar el periodo de consulta.
- Se muestra el total de unidades rechazadas del periodo seleccionado.
- El total corresponde a los registros almacenados.
- Cuando no existen registros para el periodo seleccionado, se muestra un mensaje informativo.

## Observación

Las pruebas utilizaron los registros generados durante la prueba de HU-03.

## Prueba funcional reciente: 25/10/2026

| Fecha | Prueba | Resultado obtenido | Estado |
|---|---|---|---|
| 25/10/2026 | Consultar unidades rechazadas del turno seleccionado | Se mostraron 5 unidades rechazadas | Verificado |

La consulta mostró el total de unidades rechazadas para el periodo y turno seleccionado.
