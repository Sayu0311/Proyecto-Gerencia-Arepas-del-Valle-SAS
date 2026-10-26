# Pruebas HU-02 – Registrar unidades producidas por turno

## Resultado de las pruebas

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje indicando que debe seleccionar un turno | Se mostró el mensaje correspondiente | PASS |
| Cantidad vacía | No permitir guardar | Se mostró el mensaje correspondiente | PASS |
| Cantidad no numérica | No permitir guardar | Se mostró el mensaje correspondiente | PASS |
| Cantidad igual a 0 | No permitir guardar | Se mostró el mensaje correspondiente | PASS |
| Registro válido | Guardar las unidades producidas | Se guardó correctamente el registro | PASS |
| Registro duplicado para el mismo turno | No permitir duplicar el registro | Se mostró el mensaje correspondiente y se conservó el valor original | PASS |
| Registro para otro turno | Permitir guardar el registro | Se guardó correctamente el segundo turno | PASS |
| Consulta del registro | Mostrar exactamente el valor almacenado | Se visualizaron los valores registrados | PASS |

## Evidencia funcional

Se verificó el registro de unidades producidas para:

- Turno 1: 100 unidades.
- Turno 2: 200 unidades.

El sistema impidió registrar nuevamente el Turno 1 y conservó el valor original de 100 unidades.

## Conclusión

Las pruebas realizadas para HU-02 fueron satisfactorias para los criterios de validación implementados en esta versión.
## Datos de ejecución

- Fecha: 26/10/2026
- Versión: rama `main`, posterior al Pull Request #29.
- Ejecutor: completar con el nombre real de quien realizó las pruebas.
- Evidencias: adjuntar capturas reales de los casos probados.
- QA independiente: pendiente de confirmar.

## Observación

La prueba de duplicados debe verificarse considerando la misma fecha y turno. También debe comprobarse que se pueda registrar el mismo turno en fechas diferentes.

## Conclusión

Los resultados documentados indican que las validaciones descritas funcionaron. La prueba queda pendiente de completar con evidencia verificable y revisión independiente de QA.
