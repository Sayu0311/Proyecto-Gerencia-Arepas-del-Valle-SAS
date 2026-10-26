# Pruebas HU-01 – Registrar tiempos y causas de paro

## Resultado de las pruebas

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje indicando que debe seleccionar un turno | Se mostró el mensaje correspondiente | PASS |
| No seleccionar causa | No permitir calcular/guardar el registro | Se mostró el mensaje correspondiente | PASS |
| Hora de finalización anterior a la inicial | No permitir el registro | Se mostró el mensaje correspondiente | PASS |
| Cálculo de duración | Mostrar la duración del paro en minutos | Se calculó correctamente una duración de 30 minutos | PASS |
| Guardar registro completo | Guardar el paro con sus datos | Se guardó correctamente | PASS |
| Selección de causa | Permitir seleccionar una causa de la lista | Se seleccionaron causas como Falla de máquina y Mantenimiento | PASS |
| Consulta del registro | Mostrar turno, causa, horas y duración registrados | Los registros se visualizaron correctamente | PASS |

## Evidencia funcional

Se verificaron los siguientes registros:

- Turno 1 | Falla de máquina | 10:00 - 10:30 | 30 minutos.
- Turno 1 | Mantenimiento | 11:00 - 11:15 | 15 minutos.

También se verificó que una hora de finalización anterior a la hora de inicio no puede generar una duración válida.

## Observación

El repositorio no define una duración específica para los turnos. Por esta razón, en esta versión no se valida un límite máximo de duración del paro respecto a la duración del turno.

La lista de causas utilizada en esta implementación fue definida para completar el criterio de aceptación de selección de una causa de paro.

## Conclusión

Las pruebas realizadas para HU-01 fueron satisfactorias para los criterios implementados y verificables en esta versión.