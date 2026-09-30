cat > Historias-de-Usuario/Pruebas-HU-04.md <<'EOF'
# Pruebas HU-04: Consultar información registrada por turno

## Historia de Usuario
HU-04: Consultar información registrada por turno.

## Evidencias de prueba

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje indicando que debe seleccionar un turno | Se mostró "Debe seleccionar un turno." | PASS |
| Consultar Turno 1 | Mostrar únicamente la información registrada del Turno 1 | Se mostraron 100 unidades producidas, 0 rechazadas y los paros registrados del Turno 1 | PASS |
| Consultar Turno 2 | Mostrar únicamente la información registrada del Turno 2 | Se mostraron 200 unidades producidas y 20 rechazadas, sin datos de otros turnos | PASS |
| Consultar Turno 3 sin registros | Informar que no existen datos disponibles para el turno | Se mostró "No existen datos disponibles para el turno seleccionado." | PASS |

## Validaciones realizadas

- La consulta se realiza seleccionando un turno.
- La información mostrada corresponde al turno seleccionado.
- Se muestran unidades producidas, unidades rechazadas y paros registrados.
- Se identifica la causa y duración de los paros cuando existen.
- Cuando no existen registros para el turno seleccionado, se muestra un mensaje y no se muestran datos de otros turnos.
- Se verificó que los datos consultados corresponden a la información almacenada.

## Observación

En la prueba del Turno 1 se observaron dos registros de paro con la causa "Falla de máquina". Esto corresponde a los registros utilizados durante las pruebas de HU-01 y no representa una mezcla de información entre turnos.
EOF