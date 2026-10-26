# Pruebas HU-03 – Registrar unidades rechazadas por turno

## Resultado de las pruebas

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje indicando que debe seleccionar un turno | Se mostró el mensaje correspondiente | PASS |
| Cantidad vacía | No permitir guardar | Se mostró el mensaje correspondiente | PASS |
| Cantidad no numérica | No permitir guardar | Se mostró el mensaje correspondiente | PASS |
| Cantidad negativa | No permitir guardar | Se mostró el mensaje correspondiente | PASS |
| Cantidad igual a cero | Permitir guardar el registro | Se guardó correctamente el registro | PASS |
| Rechazos superiores a producción | No permitir guardar | Se mostró el mensaje correspondiente | PASS |
| Registro duplicado para el mismo turno | No permitir duplicar el registro | Se mostró el mensaje correspondiente y se conservó el valor original | PASS |
| Registro válido para otro turno | Permitir guardar el registro | Se guardó correctamente el registro | PASS |

## Evidencia funcional

Se verificó el registro de unidades rechazadas para:

- Turno 1: 0 unidades rechazadas.
- Turno 2: 20 unidades rechazadas.

También se verificó que el sistema no permite registrar más unidades rechazadas que las unidades producidas del turno y que no permite duplicar el reporte de rechazos para un mismo turno.

## Conclusión

Las pruebas realizadas para HU-03 fueron satisfactorias para los criterios de aceptación implementados en esta versión.
