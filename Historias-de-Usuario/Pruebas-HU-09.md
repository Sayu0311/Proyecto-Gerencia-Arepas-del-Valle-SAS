# Pruebas HU-09: Registrar metas de producción por periodo

## Objetivo

Verificar que el sistema permita registrar metas de producción por periodo y turno, aplicando las validaciones definidas en la historia de usuario.

## Pruebas realizadas

| # | Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|
| 1 | Registrar meta sin seleccionar turno | Mostrar mensaje indicando que debe seleccionar un turno | Se mostró "Debe seleccionar un turno." | APROBADA |
| 2 | Registrar meta válida de 150 unidades para Turno 3 | Registrar correctamente la meta | Se registró la meta de 150 unidades para Turno 3 | APROBADA |
| 3 | Registrar meta con valor 0 | Rechazar la meta por no ser mayor que cero | Se rechazó el valor 0 | APROBADA |
| 4 | Registrar meta con valor negativo | Rechazar la meta | Se rechazó el valor negativo | APROBADA |
| 5 | Registrar meta con texto no numérico | Rechazar el valor e informar que debe ser un entero válido | Se rechazó el valor no numérico | APROBADA |
| 6 | Registrar otra meta para el mismo periodo y turno | Impedir duplicados | Se impidió registrar una segunda meta para Turno 3 en el mismo periodo | APROBADA |
| 7 | Consultar la meta registrada | Mostrar la meta asociada al periodo y turno seleccionado | Se mostró la meta de 150 unidades para Turno 3 | APROBADA |

## Observaciones

La HU-09 permite registrar una meta positiva asociada a un periodo y turno, evita registros duplicados y muestra la meta registrada para verificar su asociación.

Las pruebas realizadas corresponden a las validaciones definidas en la historia de usuario.

## Datos de ejecución

- Fecha de ejecución: completar con la fecha real.
- Versión probada: rama `main`, posterior al Pull Request #29.
- Ejecutor: completar con el nombre real.
- Evidencias: adjuntar capturas reales del registro y consulta de metas.
- QA independiente: pendiente de confirmar.

## Conclusión

Las pruebas documentadas cubren el registro, la validación y la consulta de metas por periodo y turno. Queda pendiente adjuntar las capturas reales y confirmar la revisión independiente de QA.
