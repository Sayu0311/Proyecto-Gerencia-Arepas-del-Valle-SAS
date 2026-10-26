# Pruebas HU-01 – Registrar tiempos y causas de paro

## Resultado de las pruebas

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Solicitar selección de turno | Se mostró el mensaje correspondiente | PASS |
| No seleccionar causa | Impedir el cálculo o guardado | Se mostró el mensaje correspondiente | PASS |
| Hora final anterior a la inicial | Rechazar el registro | Se mostró el mensaje correspondiente | PASS |
| Calcular duración | Mostrar duración en minutos | Se calcularon 30 minutos | PASS |
| Guardar registro | Guardar los datos del paro | Se guardó correctamente | PASS |
| Seleccionar causa | Permitir elegir una causa | Se seleccionaron causas disponibles | PASS |
| Consultar registro | Mostrar los datos guardados | Los registros se visualizaron correctamente | PASS |

## Registros verificados

- Turno 1 | Falla de máquina | 10:00–10:30 | 30 minutos.
- Turno 1 | Mantenimiento | 11:00–11:15 | 15 minutos.

## Limitaciones

No se valida la duración máxima respecto al turno porque el repositorio no define los horarios oficiales de los turnos.

## Datos de ejecución

- Fecha: 26/10/2026
- Versión: rama `main`, posterior al Pull Request #29.
- Ejecutor: completar con el nombre real de quien ejecutó las pruebas.
- Evidencias: adjuntar capturas reales de las pruebas realizadas.
- QA independiente: pendiente de confirmar.

## Conclusión

Las pruebas descritas fueron satisfactorias para los criterios implementados. La validación queda parcial hasta documentar la evidencia, confirmar la revisión independiente de QA y definir los horarios oficiales de los turnos.
