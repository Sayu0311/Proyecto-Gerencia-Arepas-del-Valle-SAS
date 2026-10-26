# Pruebas HU-07: Consultar principales causas y tiempos de paro

## Historia de Usuario
HU-07: Consultar principales causas y tiempos de paro.

## Evidencias de prueba

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| Consultar 29/09/2026 con datos | Mostrar tiempo total de paro, causas y tiempo acumulado por causa | Tiempo total: 45 minutos. Falla de máquina: 45 minutos | PASS |
| Consultar 28/09/2026 sin datos | Mostrar mensaje indicando que no existen datos de paros | Se mostró "No existen datos de paros para el periodo seleccionado." | PASS |

## Validaciones realizadas

- Se puede seleccionar el periodo de consulta.
- Se muestra el tiempo total acumulado de paro.
- Se muestran las causas registradas para el periodo.
- Se muestra el tiempo acumulado correspondiente a cada causa.
- Se identifica la causa con mayor tiempo acumulado.
- Cuando no existen datos para el periodo seleccionado, se muestra un mensaje informativo.
- Los resultados corresponden únicamente al periodo seleccionado.

## Observación

Las pruebas utilizaron los registros de paros generados durante las pruebas de HU-01.

## Prueba funcional reciente: 25/10/2026

| Fecha | Prueba | Resultado obtenido | Estado |
|---|---|---|---|
| 25/10/2026 | Consultar el tiempo y la causa del paro del turno seleccionado | Se mostró un paro de 30 minutos, de 10:00 a 10:30 | Verificado |

La consulta mostró el tiempo y la causa del paro para el periodo y turno seleccionado.
