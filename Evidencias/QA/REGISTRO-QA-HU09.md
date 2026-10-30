# Registro general de validación QA
## Proyecto: Arepas del Valle S.A.S.

**Fecha de validación:** 2026-10-30  
**Rama:** HU-09  
**Tipo de validación:** Pruebas funcionales independientes

## Resumen general

| Historia de usuario | Estado QA | Pruebas verificadas |
|---|---|---:|
| HU-01 | En validación | 7 PASS |
| HU-02 | En validación | 7 PASS |
| HU-03 | En validación | 6 PASS, 1 FAIL, 1 BLOQUEADA |
| HU-04 | En validación | 3 PASS, 1 DISCREPANCIA |
| HU-05 | En validación | 5 PASS |
| HU-06 | BLOQUEADA | 5 NO EJECUTADAS |
| HU-07 | En validación | 2 PASS |
| HU-08 | En validación | 2 PASS |
| HU-09 | En validación | 6 PASS, 1 BLOQUEADA |

## HU-01: Registrar tiempos y causas de paro

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje de validación | Debe seleccionar un turno. | PASS |
| No seleccionar causa | Mostrar mensaje de validación | Debe seleccionar una causa de paro. | PASS |
| Cálculo de duración | Calcular minutos entre las horas | Duración del paro: 30 minutos. | PASS |
| Hora final anterior a inicial | Rechazar el cálculo | La hora de finalización no puede ser anterior a la hora de inicio. | PASS |
| Guardar registro válido | Confirmar el almacenamiento | Registro de paro guardado correctamente. | PASS |
| Consultar registro | Mostrar turno, causa, horas y duración | Turno 1, Falla de máquina, 10:00 - 10:30, 30 minutos. | PASS |
| Guardar sin calcular duración | Impedir el guardado | Debe calcular la duración antes de guardar. | PASS |

**Evidencia:** `Evidencias/QA/Capturas/HU1_registro de paro.jpeg`

**Observación:** La prueba de duración máxima respecto al turno no se ha realizado, porque el repositorio no define una duración específica para los turnos.

**Resultado HU-01:** 7 pruebas PASS verificadas. La historia queda en validación hasta completar la revisión de los demás criterios y evidencias.

## Control de evidencias

Las pruebas se marcarán como aprobadas únicamente cuando se hayan ejecutado y sus resultados hayan sido comprobados. Las historias todavía no revisadas permanecen pendientes.

## HU-02: Registrar unidades producidas por turno

| Prueba | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|
| No seleccionar turno | Mostrar mensaje de validación | Debe seleccionar un turno. | PASS |
| Cantidad vacía | Impedir el registro | Debe ingresar la cantidad de unidades producidas. | PASS |
| Cantidad no numérica | Rechazar texto | La cantidad de unidades debe ser un número entero. | PASS |
| Cantidad igual a cero | Rechazar el valor | La cantidad de unidades debe ser mayor que cero. | PASS |
| Registro duplicado | Impedir duplicados | Ya existe un registro para este turno. | PASS |
| Registro en otro turno | Permitir guardar | Registro guardado correctamente para Turno 3. | PASS |
| Consulta de registros | Mostrar valores almacenados | Turno 1: 100, Turno 2: 200 y Turno 3: 150 unidades. | PASS |

**Evidencia:** `Evidencias/QA/Capturas/HU2_ registro produccion.jpeg`

**Resultado HU-02:** 7 pruebas PASS verificadas independientemente.

**Observación:** El intento de registrar 150 unidades en Turno 1 fue rechazado porque ya existía un registro. Los valores originales se conservaron.

## HU-03: Registrar unidades rechazadas por turno

**Estado:** En validación  
**Evidencia:** `Evidencias/QA/Capturas/HU3_ registro rechazo.jpeg`

| N.º | Prueba | Resultado |
|---|---|---|
| 1 | Guardar sin seleccionar turno | PASS |
| 2 | Guardar sin ingresar cantidad | PASS |
| 3 | Ingresar texto no numérico (`abc`) | PASS |
| 4 | Ingresar cantidad negativa (`-5`) | FAIL |
| 5 | Registrar cero rechazos | BLOQUEADA |
| 6 | Registrar más rechazos que unidades producidas | PASS |
| 7 | Registrar 10 rechazos en Turno 3 | PASS |
| 8 | Intentar registrar nuevamente en Turno 3 | PASS |

**Observaciones:**
- La cantidad negativa fue rechazada, pero el mensaje indicó que debía ingresarse un número entero, en lugar del mensaje específico para cantidades negativas. Se identifica una discrepancia en la validación.
- La prueba de cero rechazos no pudo repetirse porque Turno 1 ya tenía un registro de rechazos y el sistema impide duplicados.
- Se verificaron los registros almacenados: Turno 1 = 0, Turno 2 = 20 y Turno 3 = 10.
- El intento de duplicar el registro de Turno 3 fue rechazado correctamente.

**Resultado:** 6 PASS, 1 FAIL y 1 BLOQUEADA.

## HU-04: Consultar información registrada por turno

**Estado:** En validación  
**Evidencia:** `Evidencias/QA/Capturas/HU4_consulta turno.jpeg`

| N.º | Prueba | Resultado |
|---|---|---|
| 1 | Consultar sin seleccionar turno | PASS |
| 2 | Consultar información de Turno 1 | PASS |
| 3 | Consultar información de Turno 2 | PASS |
| 4 | Consultar Turno 3 sin registros, según caso histórico | DISCREPANCIA |

**Observaciones:**
- Turno 1 mostró 100 unidades producidas, 0 rechazadas y tres registros de paro con sus horarios y duraciones.
- Turno 2 mostró 200 unidades producidas, 20 rechazadas y el aviso de que no existen tiempos de paro.
- Turno 3 mostró 150 unidades producidas, 10 rechazadas y el aviso de que no existen tiempos de paro. La verificación identificó correctamente la información faltante.
- El caso histórico esperaba que Turno 3 no tuviera registros. La diferencia se explica por los registros creados durante las pruebas de HU-02 y HU-03. No se modificaron los datos para forzar el resultado esperado.
- Las consultas mostraron información correspondiente al turno seleccionado.

**Resultado:** 3 PASS y 1 DISCREPANCIA respecto al caso histórico.

## HU-05: Consultar indicadores de producción por periodo y turno

**Estado:** En validación  
**Evidencia:** `Evidencias/QA/Capturas/HU5_consulta indicadores.jpeg`

| N.º | Prueba | Resultado |
|---|---|---|
| 1 | Consultar sin seleccionar turno | PASS |
| 2 | Consultar 29/09/2026 – Turno 1 | PASS |
| 3 | Consultar 29/09/2026 – Turno 2 | PASS |
| 4 | Consultar 29/09/2026 – Turno 3 | PASS |
| 5 | Consultar 28/09/2026 – Turno 1 | PASS |

**Observaciones:**
- Turno 1: 100 unidades producidas, 0 rechazadas y 45 minutos de paro.
- Turno 2: 200 unidades producidas, 20 rechazadas y 0 minutos de paro.
- Turno 3: se mostró el mensaje de que no existen datos para el periodo y turno seleccionados.
- Para el 28/09/2026 y Turno 1 también se mostró el mensaje de ausencia de datos.
- Las consultas mostraron los resultados correspondientes a la fecha y turno seleccionados.

**Resultado:** 5 pruebas PASS verificadas independientemente.

## HU-06: Comparar producción real con metas establecidas

**Estado:** BLOQUEADA – posible funcionalidad incompleta

| N.º | Prueba histórica | Resultado |
|---|---|---|
| 1 | Consultar sin seleccionar turno | NO EJECUTADA |
| 2 | Turno 1 sin meta | NO EJECUTADA |
| 3 | Producción 100, meta 120 | NO EJECUTADA |
| 4 | Producción 100, meta 100 | NO EJECUTADA |
| 5 | Producción 100, meta 80 | NO EJECUTADA |

**Hallazgos de revisión de código:**
- Existe la función `consultar_comparacion(fecha, turno)` en `app.py`, líneas 203–234.
- La función consulta la producción real y la meta correspondiente al periodo y turno.
- La búsqueda en los archivos Python encontró únicamente la definición de la función, sin llamadas a ella.
- No se encontró una interfaz para ejecutar la comparación ni lógica visible para clasificar el resultado como inferior, igual o superior a la meta.
- No se modificó el código ni se registraron metas durante esta revisión.

**Resultado:** 5 pruebas NO EJECUTADAS. Hallazgo pendiente de revisión por desarrollo.

## HU-07: Consultar principales causas y tiempos de paro

**Estado:** En validación  
**Evidencia:** `Evidencias/QA/Capturas/HU7_consulta paro.jpeg`

| N.º | Prueba | Resultado |
|---|---|---|
| 1 | Consultar el 29/09/2026 con datos | PASS |
| 2 | Consultar el 28/09/2026 sin datos | PASS |

**Observaciones:**
- Para el 29/09/2026 se obtuvo un tiempo total de paro de 45 minutos.
- La causa «Falla de máquina» acumuló 45 minutos.
- El sistema identificó correctamente «Falla de máquina» como la causa principal.
- Para el 28/09/2026 se mostró el mensaje de que no existen datos de paros.
- El sistema confirmó que los datos corresponden únicamente al periodo seleccionado.

**Resultado:** 2 pruebas PASS verificadas independientemente.

## HU-08: Consultar unidades rechazadas por periodo

**Estado:** En validación  
**Evidencia:** `Evidencias/QA/Capturas/HU8_consulta rechazos.jpeg`

| N.º | Prueba | Resultado |
|---|---|---|
| 1 | Consultar el 29/09/2026 con registros | PASS |
| 2 | Consultar el 28/09/2026 sin registros | PASS |

**Observaciones:**
- Para el 29/09/2026 se mostraron 20 unidades rechazadas y el mensaje de confirmación correspondiente.
- Para el 28/09/2026 se mostraron 0 unidades rechazadas y el mensaje de ausencia de registros.
- Los resultados coincidieron con los casos históricos.

**Resultado:** 2 pruebas PASS verificadas independientemente.

## HU-09: Registrar metas de producción por periodo

**Estado:** En validación  
**Evidencia:** `Evidencias/QA/Capturas/HU9_registro metas.jpeg`

| N.º | Prueba | Resultado obtenido | Estado |
|---|---|---|---|
| 1 | Registrar sin seleccionar turno | Debe seleccionar un turno. | PASS |
| 2 | Registrar con meta vacía | Debe ingresar una meta de producción. | PASS |
| 3 | Ingresar texto no numérico (`abc`) | La meta debe ser un número entero válido. | PASS |
| 4 | Ingresar cero | La meta de producción debe ser un número entero mayor que cero. | PASS |
| 5 | Ingresar valor negativo (`-5`) | La meta debe ser un número entero válido. | PASS |
| 6 | Registrar una meta duplicada | Ya existe una meta registrada para el periodo y turno seleccionados. | PASS |
| 7 | Consultar una meta existente | Periodo: 2026-09-29, Turno 3, meta: 150 unidades. | PASS |

**Prueba bloqueada:**
- No se pudo repetir el registro válido de una meta nueva porque ya existía una meta de 150 unidades para el 29/09/2026 y Turno 3.
- No se creó ni modificó una meta para evitar duplicar o alterar datos existentes.

**Resultado:** 6 pruebas PASS verificadas y 1 prueba de registro nuevo BLOQUEADA por la existencia previa de la meta.

## Nota para la integración en main

Este registro documenta las pruebas funcionales independientes realizadas sobre la rama `HU-09` el 30 de octubre de 2026. Sus resultados corresponden exclusivamente a esa versión y no constituyen una aprobación QA de la rama `main`.

La HU-06 quedó bloqueada durante las pruebas en `HU-09` porque no se pudo ejecutar su validación de interfaz. En la rama `main` se verificó posteriormente que la interfaz de comparación está presente; por tanto, sus pruebas deben repetirse sobre la versión integrada antes de darla por validada.

Los estados PASS, FAIL, BLOQUEADA y DISCREPANCIA se conservan tal como fueron registrados en la ejecución original.
