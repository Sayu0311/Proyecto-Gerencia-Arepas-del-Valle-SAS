# Empresa caso de estudio: Arepas del Valle S.A.S.

**Marco Metodológico de Gestión:** Metodología Ágil - SCRUM

**Asignatura:** Gerencia de Proyectos (Periodo 2026-2)

**Integrantes:** Andrea Carolina Montes Barragan y Sayuri Alexandra Moreno Espinosa.

# 1. INFORMACIÓN DE LA EMPRESA Y DEL PROCESO

## 1.1 Información de la empresa

**Arepas del Valle S.A.S.** es una empresa manufacturera de alimentos ubicada en el Valle de Aburrá (Antioquia, Colombia), dedicada a la elaboración y comercialización de arepas empacadas para consumo.

**Producto seleccionado:** arepa tradicional de maíz blanco precocida, empacada en presentaciones de 5 y 10 unidades.

## 1.2 Proceso y problemática

El proyecto monitorea el proceso productivo desde la preparación de materias primas hasta el almacenamiento refrigerado. Las principales etapas son:

1. Preparación y dosificación de materias primas.
2. Mezclado y formación de la masa.
3. Formado y troquelado de las arepas.
4. Precocción.
5. Enfriamiento.
6. Empaque y rotulado.
7. Almacenamiento refrigerado.

Actualmente, variables como producción, unidades rechazadas y tiempos de paro se registran manualmente y posteriormente se consolidan en hojas de cálculo. Esto ocasiona:

- Disponibilidad tardía de la información, entre 8 y 12 horas después del turno.
- Baja trazabilidad de las variables del proceso.
- Detección tardía de paradas y mermas.
- Dificultades para realizar seguimiento oportuno al desempeño de la producción.

## 1.3 Visión del producto

La aplicación web busca centralizar el registro de las variables de producción y facilitar la consulta de información e indicadores relacionados con producción, calidad y tiempos de paro.

El producto está dirigido principalmente a los **Supervisores de Producción y la Gerencia de Operaciones**, quienes podrán consultar la información de manera organizada para apoyar el seguimiento del proceso y la toma de decisiones.

## 1.4 SIPOC

| Proveedores | Entradas | Proceso | Salidas | Clientes |
|---|---|---|---|---|
| Materias primas | Harina de maíz, agua, aceite y sal | Preparación, mezclado y formado | Masa y arepas formadas | Áreas de producción y precocción |
| Área de precocción | Arepas formadas | Precocción | Arepas precocidas | Área de enfriamiento |
| Área de enfriamiento | Arepas precocidas | Enfriamiento | Arepas enfriadas | Área de empaque |
| Área de empaque | Arepas enfriadas y material de empaque | Empaque, sellado y rotulado | Arepas empacadas | Almacenamiento y distribución |
| Almacenamiento | Arepas empacadas | Almacenamiento refrigerado | Producto terminado | Supermercados, tiendas y distribuidores |

# 2. ESTRATEGIA CORPORATIVA Y CONTRIBUCIÓN DEL PROYECTO

## 2.1 Estrategia corporativa

Arepas del Valle S.A.S. orienta su estrategia hacia la **excelencia operacional y la digitalización progresiva de sus procesos productivos**, buscando mejorar la eficiencia, la calidad y la toma de decisiones basada en datos.

El proyecto contribuye a esta estrategia mediante la centralización de información de producción, calidad y tiempos de paro. Esto facilita el seguimiento de las variables del proceso y permite identificar oportunidades de mejora y reducción de desperdicios, en línea con principios de **Lean Manufacturing**.

## 2.2 Contribución a los ODS

El proyecto se relaciona con el **ODS 12: Producción y Consumo Responsables**, principalmente mediante:

- **Meta 12.5:** el registro de unidades quemadas, rotas o rechazadas permite identificar fuentes de desperdicio y apoyar acciones para reducir las mermas.
- **Meta 12.2:** el seguimiento de producción, mermas y tiempos de operación permite identificar oportunidades para mejorar el aprovechamiento de recursos como materia prima, agua y energía.

# 3. PORTAFOLIO, PROGRAMA Y PROYECTO

El proyecto hace parte de una propuesta académica de modernización operacional y transformación digital para Arepas del Valle S.A.S. La estructura distingue el portafolio, los programas que agrupan iniciativas relacionadas y los proyectos que pueden desarrollarse de manera independiente.

| Nivel | Nombre propuesto | Iniciativas incluidas |
|---|---|---|
| **Portafolio** | Portafolio de Modernización Operacional y Transformación Digital | Agrupa iniciativas orientadas a mejorar la eficiencia, la calidad y el uso de información en la empresa. |
| **Programa 1** | Programa de Digitalización y Eficiencia de Procesos Productivos | Incluye el proyecto de dashboard de producción y una iniciativa propuesta para digitalizar la programación y el seguimiento de órdenes de producción. |
| **Programa 2** | Programa de Calidad y Reducción de Desperdicios | Incluye una iniciativa propuesta para registrar y analizar causas de rechazo, así como un proyecto futuro para medir el consumo de materias primas y las mermas por periodo. |
| **Proyecto desarrollado** | Aplicación web de dashboard para el monitoreo de indicadores de producción de arepas | Solución desarrollada en este trabajo para registrar producción, unidades rechazadas, tiempos de paro y metas, y consultar indicadores y gráficos. |

Las iniciativas adicionales mencionadas en los programas son **propuestas de portafolio y no proyectos implementados ni validados**. El alcance efectivamente desarrollado en este trabajo corresponde a la aplicación web descrita en la arquitectura y en las historias de usuario.

# 4. ELECCIÓN Y CLASIFICACIÓN DEL PROYECTO

## 4.1 Tipo de proyecto

El proyecto corresponde a un **desarrollo de software a la medida y transformación digital**. Consiste en construir una aplicación web para registrar, procesar y visualizar información operativa de la planta, relacionada con producción, tiempos de paro, mermas e indicadores.

La solución digitaliza el flujo de información sin modificar físicamente las máquinas ni el producto. El desarrollo será gestionado y versionado mediante **Git y GitHub**.

## 4.2 Ciclo de vida: metodología Scrum

Se utilizará una metodología ágil basada en **Scrum**, organizada en dos Sprints relacionados con las fechas de entrega del proyecto.

### Sprint 1: Producto Mínimo Viable (MVP)

**Objetivo:** Implementar el registro de producción, unidades rechazadas, tiempos de paro y metas de producción por fecha y turno.

**Funcionalidades principales:**

- Configuración del entorno de desarrollo y de la base de datos SQLite.
- Registro de unidades producidas por fecha y turno.
- Registro de unidades rechazadas por fecha y turno.
- Registro de tiempos de paro, duración y causa.
- Registro de metas de producción por fecha y turno.
- Validación para evitar registros duplicados de producción y unidades rechazadas para la misma fecha y turno.

**Entregable:** Primera versión funcional de la aplicación web con formularios de registro y almacenamiento local de la información.

### Sprint 2: Indicadores, comparación y visualización

**Objetivo:** Facilitar la consulta de los registros y comparar los resultados de producción con las metas establecidas.

**Funcionalidades principales:**

- Consulta de indicadores de producción, unidades rechazadas y tiempos de paro.
- Comparación de producción real frente a la meta por fecha y turno.
- Visualización de gráficos de producción, metas, unidades rechazadas y tiempos de paro.
- Consulta de información de diferentes fechas y turnos.
- Carga de archivos CSV y Excel para previsualizar los datos y validar las columnas requeridas.
- Documentación de pruebas funcionales y correcciones realizadas.

**Entregable:** Versión integrada de la aplicación con registros, consultas, indicadores, gráficos y previsualización de archivos CSV y Excel.

**Alcance y limitaciones:** La versión actual trabaja con unidades producidas y rechazadas, tiempos de paro y metas. No implementa todavía el cálculo de OEE, el registro de kilogramos de masa, las presentaciones de paquetes de 5 y 10 unidades, la autenticación por roles ni la importación automática de archivos a la base de datos. Estas funcionalidades no se presentan como terminadas.

## 4.3 Relación con el ODS 12

El proyecto se relaciona con el **ODS 12: Producción y Consumo Responsables**, principalmente mediante el seguimiento de producción, calidad, paradas y mermas.

La digitalización de estos datos permite identificar pérdidas y oportunidades de mejora en el uso de materias primas y otros recursos, contribuyendo especialmente a la **meta 12.5**, relacionada con la reducción de la generación de desechos.

## 4.4 Responsabilidad Social Empresarial (RSE)

El proyecto aporta a la responsabilidad social empresarial mediante:

- **Eficiencia de recursos:** seguimiento de desperdicios y oportunidades de mejora.
- **Sostenibilidad ambiental:** seguimiento de residuos asociados a las mermas.
- **Bienestar laboral:** reducción de tareas repetitivas de registro manual.
- **Transparencia:** disponibilidad organizada de información operativa.
- **Toma de decisiones basada en datos:** apoyo a la gestión de las áreas operativas y administrativas.

# 5. ESTUDIO DE PREFACTIBILIDAD Y FACTIBILIDAD

El estudio de factibilidad analiza la viabilidad técnica, económica, operativa, legal y social de la aplicación web para el monitoreo de información e indicadores del proceso productivo.

## 5.1 Viabilidad técnica

El proyecto utilizará tecnologías de código abierto:

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.11 |
| Interfaz y analítica | Streamlit |
| Base de datos local | SQLite |
| Base de datos multiusuario | PostgreSQL |
| Control de versiones | Git y GitHub |
| Metodología | Scrum |

La aplicación estará orientada a la captura, procesamiento y monitoreo de información. No intervendrá físicamente sobre la maquinaria de producción.

## 5.2 Viabilidad económica

La viabilidad económica del proyecto se evalúa de manera preliminar. La inversión inicial de **$6.000.000 COP** corresponde a una estimación académica y no a un costo ejecutado y verificado. Para validar la viabilidad será necesario documentar las horas de desarrollo, los costos de operación, la capacitación y el mantenimiento.

### Estimaciones de beneficios

En esta etapa no se dispone de registros reales suficientes para comprobar un ahorro mensual por reducción del tiempo de supervisión ni por disminución de mermas. Por lo tanto, los valores económicos mencionados en versiones anteriores se consideran hipótesis de trabajo y no resultados demostrados.

Para estimar los beneficios cuando se disponga de datos, se utilizarán los siguientes cálculos:

- **Ahorro por tiempo administrativo:** horas efectivamente ahorradas al mes × costo laboral por hora.
- **Ahorro por reducción de mermas:** kilogramos de materia prima cuya pérdida se evita al mes × costo de materia prima por kilogramo.
- **Beneficio neto mensual:** beneficios económicos verificables − costos adicionales mensuales de operación y mantenimiento.
- **Periodo de recuperación:** inversión inicial ÷ beneficio neto mensual, siempre que este último sea positivo.

### Datos requeridos para validar el caso de negocio

Para sustentar el cálculo se deberán recopilar registros del proceso real, incluyendo:

- Tiempo dedicado actualmente a registrar y consolidar la información de producción.
- Costo laboral por hora de las personas que realizan estas actividades.
- Cantidad de materia prima procesada y cantidad de merma por periodo.
- Costo de la materia prima por kilogramo.
- Costos de implementación, operación, capacitación y mantenimiento de la aplicación.

Hasta contar con estos datos, **no se afirma que el proyecto genere un ahorro mensual de $2.650.000 COP ni que recupere la inversión en 2,3 meses**. Esos resultados solo podrán calcularse después de validar los supuestos con información documentada.

## 5.3 Viabilidad operativa

El proyecto será desarrollado mediante roles Scrum:

| Integrante | Rol |
|---|---|
| Sayuri | Scrum Master |
| Andrea | Developer |


Los supervisores registrarán la información operativa y la gerencia consultará los datos e indicadores mediante la aplicación.

El registro de un dato individual se estima en menos de **40 segundos**. Este tiempo corresponde al ingreso de un registro y no al tiempo total de captura y consolidación del turno.

## 5.4 Viabilidad legal

El proyecto tendrá en cuenta la **Ley 1581 de 2012 de Colombia** para el manejo de información personal y establecerá perfiles de acceso según las funciones de los usuarios.

El software será desarrollado por el equipo y se utilizarán tecnologías y librerías de código abierto, respetando sus respectivas condiciones de licencia.

## 5.5 Viabilidad social

El proyecto busca reducir tareas repetitivas de registro manual y facilitar el acceso a información operativa para supervisores y gerencia.

Se contempla la participación del personal durante las pruebas y capacitación, con el propósito de facilitar la adopción de la herramienta y presentar la digitalización como apoyo a la mejora del proceso.

## 5.6 Análisis de construir o comprar

Se consideran tres alternativas para atender la necesidad de registrar y consultar información del proceso productivo.

| Alternativa | Ventajas | Limitaciones y costos por verificar |
|---|---|---|
| Mantener el proceso actual con planillas y hojas de cálculo | No requiere adquirir una nueva aplicación. El personal ya conoce el procedimiento. | Continúa dependiendo del registro manual y de la consolidación de información. Deben medirse las horas dedicadas y los costos laborales asociados. |
| Comprar una solución comercial de gestión de producción | Puede ofrecer funciones integradas de producción, inventario, calidad y reportes, según el producto contratado. | Es necesario solicitar cotizaciones y verificar licencias, implementación, capacitación, soporte y compatibilidad con el proceso de la empresa. No se dispone de cotizaciones verificadas para establecer un costo comparable en este estudio. |
| Construir una aplicación propia | Permite adaptar las funciones al alcance académico, controlar el código y realizar cambios de acuerdo con las necesidades identificadas. | Requiere tiempo de desarrollo, pruebas, mantenimiento, documentación y capacitación. La estimación académica de inversión de $6.000.000 COP debe validarse con un desglose de costos. |

### Criterio de selección

Para este proyecto académico se seleccionó la construcción de una aplicación propia con Python, Streamlit y SQLite, debido a que permite implementar y demostrar las funciones definidas en las historias de usuario sin asumir el costo de una licencia comercial durante el desarrollo.

Esta selección no demuestra por sí sola que construir sea más económico que comprar. Para establecer cuál alternativa ofrece el menor costo total, sería necesario comparar cotizaciones comerciales verificables y estimar los costos de desarrollo, operación y mantenimiento durante un mismo periodo.

### Información pendiente para una comparación económica

- Cotizaciones de al menos dos soluciones comerciales adecuadas para pequeñas empresas manufactureras.
- Costos de licencias, implementación, soporte y capacitación.
- Desglose de las horas de desarrollo y de los costos de mantenimiento de la aplicación propia.
- Estimación del costo actual de registrar y consolidar manualmente los datos.

Hasta obtener esta información, no se asignan precios inventados a las soluciones comerciales ni se afirma que la alternativa elegida sea la más económica en todos los escenarios.

## 5.7 Estimación de beneficios

En esta etapa, los beneficios se consideran objetivos esperados y no resultados medidos en la operación real. No se dispone de una línea base documentada que permita confirmar los tiempos actuales de registro, los porcentajes de merma o el retraso en la disponibilidad de información.

| Aspecto | Situación de referencia | Resultado esperado con la aplicación | Evidencia necesaria |
|---|---|---|---|
| Tiempo administrativo | Debe medirse el tiempo real dedicado a registrar y consolidar información. | Reducir el tiempo de digitación y consulta. | Medición del tiempo antes y después de utilizar la aplicación. |
| Disponibilidad de información | Debe documentarse cuánto tarda actualmente la información en quedar disponible. | Facilitar la consulta de los registros guardados en la aplicación. | Comparación de marcas de tiempo de los registros y del proceso actual. |
| Unidades rechazadas | Deben recopilarse registros reales por fecha y turno. | Consultar cantidades registradas e identificar variaciones. | Registros históricos y validación con el responsable de producción. |
| Tiempos de paro | Deben recopilarse la duración y las causas de los paros reales. | Consultar los tiempos registrados y sus causas. | Bitácoras de producción o registros de los responsables. |
| Cumplimiento de metas | Deben definirse metas aprobadas por fecha y turno. | Comparar las unidades producidas con la meta registrada. | Metas documentadas y registros de producción correspondientes. |

La aplicación permite registrar y consultar información operativa, pero esto no demuestra por sí solo que se hayan reducido los tiempos administrativos, las mermas o los costos. Para comprobar esos beneficios se requiere comparar datos reales de un periodo anterior con los obtenidos después de implementar la solución.

Los porcentajes y tiempos que se propongan como objetivos deberán identificarse expresamente como metas de mejora y contar con un método de medición definido.

## 5.8 Criterios de éxito

| Criterio | Resultado esperado |
|---|---|
| Funcionalidades del alcance | 100 % de las funcionalidades del Product Backlog implementadas. |
| Indicadores | Indicadores definidos en el alcance disponibles y dinámicos. |
| Calidad de los registros | Al menos 95 % de registros sin errores de validación. |
| Capacitación | 100 % de los usuarios previstos capacitados. |
| Reducción del tiempo de consolidación | Reducción mínima del 30 % del tiempo total de procesamiento y consolidación. |
| Satisfacción | Al menos 80 % de valoración positiva de los usuarios. |

# 8. GESTIÓN DEL PROYECTO BAJO EL MARCO DE TRABAJO SCRUM

El proyecto se gestiona mediante el marco de trabajo **Scrum**, utilizando GitHub para el control de versiones, revisión de cambios y seguimiento del trabajo.

## 8.1 Equipo Scrum

| Integrante | Responsabilidad |
|---|---|
| Sayuri | Scrum Master |
| Andrea | Developer |


El Product Owner corresponde al profesor de la asignatura, quien realiza la validación y retroalimentación del producto.

## 8.2 Fuente de verdad del Product Backlog

El Product Backlog vigente está conformado por las **nueve historias de usuario** almacenadas en la carpeta `Historias-de-Usuario`. Estas historias constituyen la fuente de verdad del alcance funcional del proyecto.

| Orden | Historia | Descripción | Story Points |
|---:|---|---|---:|
| 1 | HU-02 | Registrar unidades producidas | 2 |
| 2 | HU-03 | Registrar unidades rechazadas | 2 |
| 3 | HU-01 | Registrar tiempos y causas de paro | 3 |
| 4 | HU-09 | Registrar metas de producción | 3 |
| 5 | HU-04 | Consultar información por turno | 3 |
| 6 | HU-05 | Consultar indicadores por período y turno | 5 |
| 7 | HU-06 | Comparar resultados con las metas de producción | 5 |
| 8 | HU-07 | Visualizar causas y tiempos de paro | 5 |
| 9 | HU-08 | Visualizar unidades rechazadas | 3 |

El orden del backlog considera las dependencias entre las historias, priorizando primero el registro de información y posteriormente las funcionalidades de consulta, comparación y análisis.

## 8.3 Historia pivote y estimación

La **HU-05** se utiliza como historia pivote con una estimación de **5 Story Points**.

Las demás historias se estiman de manera relativa utilizando una escala de Fibonacci, considerando complejidad, esfuerzo y alcance.

## 8.4 Sprint 1: Producto Mínimo Viable (MVP)

**Periodo:** Inicio del proyecto hasta el 29/09/2026.

**Objetivo:** Implementar el registro de producción, unidades rechazadas, tiempos de paro y metas por fecha y turno.

**Funcionalidades principales:**

- Configuración del entorno y de la base de datos SQLite.
- Registro de unidades producidas por fecha y turno.
- Registro de unidades rechazadas por fecha y turno.
- Registro de tiempos de paro, duración y causa.
- Registro de metas de producción por fecha y turno.
- Validación de registros duplicados de producción y unidades rechazadas para la misma fecha y turno.

**Entregable:** Primera versión funcional de la aplicación web con formularios de registro y almacenamiento local.

## 8.5 Sprint 2: Indicadores, comparación y visualización

**Fecha de cierre:** 30/10/2026, correspondiente a la segunda entrega del proyecto.

**Objetivo:** Facilitar la consulta de registros y comparar la producción real con las metas establecidas.

**Funcionalidades principales:**

- Consulta de indicadores de producción, unidades rechazadas y tiempos de paro.
- Comparación de producción real frente a la meta por fecha y turno.
- Gráficos de producción, metas, unidades rechazadas y tiempos de paro.
- Consulta de información de diferentes fechas y turnos.
- Carga de archivos CSV y Excel para previsualizar los datos y validar las columnas requeridas.
- Documentación de pruebas funcionales y correcciones realizadas.

**Entregable:** Versión integrada de la aplicación con registros, consultas, indicadores, gráficos y previsualización de archivos CSV y Excel.

**Alcance y limitaciones:** La versión actual no implementa el cálculo de OEE, el registro de kilogramos de masa, las presentaciones de paquetes de 5 y 10 unidades, la autenticación por roles ni la importación automática de archivos a la base de datos. Estas funcionalidades no se consideran terminadas.

## 8.6 Definition of Done

Una historia de usuario se considera terminada cuando:

1. La funcionalidad está desarrollada e integrada.
2. Cumple sus criterios de aceptación.
3. Se realizaron las pruebas correspondientes.
4. Los datos se almacenan y procesan correctamente cuando aplique.
5. No existen errores críticos que impidan utilizarla.
6. Fue revisada por QA.
7. El código está registrado mediante un commit.
8. La documentación necesaria fue actualizada.

## 8.7 Eventos Scrum

| Evento | Aplicación |
|---|---|
| Sprint Planning | Definición del objetivo y selección de historias del Sprint. |
| Daily Scrum | Seguimiento del trabajo, pendientes e impedimentos. |
| Sprint Review | Presentación del incremento y recepción de retroalimentación. |
| Sprint Retrospective | Identificación de dificultades y oportunidades de mejora. |

## 8.8 Seguimiento del trabajo

El seguimiento se realizará mediante **GitHub Projects**.

Las nueve historias de usuario estarán registradas en el tablero y su estado se actualizará conforme avance el trabajo. El tablero constituye evidencia del seguimiento del Product Backlog y de la gestión del trabajo mediante Scrum.

## 8.9 Estrategia de control de versiones

GitHub será utilizado como repositorio central:

- `main`: versión integrada y estable.
- **Ramas por historia:** desarrollo de funcionalidades asociadas a cada HU.
- **Commits:** registro de los cambios realizados.
- **Pull Requests:** revisión e integración de cambios.
- **GitHub Projects:** seguimiento del Product Backlog y del trabajo.

Cada cambio de código deberá relacionarse con la historia de usuario correspondiente para facilitar la trazabilidad del desarrollo.

# 9. ARQUITECTURA DE LA SOLUCIÓN, PROTOTIPO V0 Y FICHAS TÉCNICAS DE LOS INDICADORES

## 9.1 Arquitectura de la solución

La solución implementada es una aplicación web desarrollada con Streamlit y Python. Permite registrar información de producción, unidades rechazadas, tiempos de paro y metas de producción, almacenarla localmente en SQLite y consultar indicadores y gráficos por fecha y turno.

La arquitectura actual está compuesta por los siguientes elementos:

1. **Interfaz de usuario:** Streamlit presenta los formularios de registro, las consultas, los indicadores y los gráficos.
2. **Lógica de aplicación:** Python procesa las solicitudes, valida los datos y ejecuta las consultas.
3. **Persistencia de datos:** SQLite almacena los registros operativos de la aplicación.
4. **Visualización:** los indicadores y gráficos permiten comparar la producción registrada con las metas y consultar unidades rechazadas y tiempos de paro.
5. **Validación de archivos externos:** la aplicación permite cargar archivos CSV y Excel para previsualizar su contenido y comprobar las columnas requeridas. Esta función no importa automáticamente los datos a la base SQLite.
6. **Control de versiones:** Git y GitHub permiten mantener el historial de cambios del código y colaborar en su desarrollo.

### Estructura de información

| Tipo de registro | Información principal |
|---|---|
| Producción | Fecha, turno y unidades producidas |
| Unidades rechazadas | Fecha, turno y cantidad de unidades rechazadas |
| Tiempos de paro | Fecha, turno, hora de inicio, hora de finalización, duración y causa |
| Metas de producción | Fecha, turno y meta de unidades |

La aplicación valida que no se registren duplicados de producción o de unidades rechazadas para una misma fecha y turno.

**Limitaciones de la versión actual:** la solución no implementa una base de datos PostgreSQL, autenticación por roles, registro de kilogramos de masa, presentaciones de paquetes de 5 y 10 unidades, cálculo de OEE ni importación automática de archivos. Estas funcionalidades no forman parte de las capacidades implementadas y verificadas en esta versión.

## Flujo general

```text
Usuario
   ↓
Interfaz web desarrollada con Streamlit
   ↓
Funciones Python y validaciones
   ↓
Base de datos local SQLite
   ↓
Consultas de producción, rechazos, paradas y metas
   ↓
Indicadores, comparación con metas y gráficos
   ↓
Apoyo a la toma de decisiones
```

Estos objetivos ya fueron establecidos en el diagnóstico y **Business Case** del proyecto.



## 10. MATRIZ DE RIESGOS 5×5

La matriz permite identificar y priorizar riesgos del proyecto según su probabilidad e impacto. Las valoraciones son estimaciones cualitativas del equipo académico y deben revisarse durante cada Sprint.

### Escalas de valoración

| Valor | Probabilidad | Impacto |
|---:|---|---|
| 1 | Muy baja | Insignificante |
| 2 | Baja | Menor |
| 3 | Media | Moderado |
| 4 | Alta | Grave |
| 5 | Muy alta | Crítico |

**Nivel de riesgo = Probabilidad × Impacto**

| Puntaje | Nivel | Tratamiento |
|---:|---|---|
| 1–4 | Bajo | Monitorear |
| 5–9 | Moderado | Definir acciones preventivas |
| 10–16 | Alto | Priorizar mitigación y seguimiento |
| 17–25 | Crítico | Atención inmediata |

### Registro de riesgos

| ID | Riesgo | Probabilidad | Impacto | Puntaje | Nivel | Acción de mitigación |
|---|---|---:|---:|---:|---|---|
| R1 | Pérdida o corrupción de la base de datos SQLite | 3 | 5 | 15 | Alto | Crear copias de seguridad y probar su recuperación. |
| R2 | Errores en los datos ingresados por los usuarios | 4 | 4 | 16 | Alto | Validar campos, rangos y duplicados; ejecutar pruebas funcionales. |
| R3 | Retrasos en el desarrollo de historias de usuario | 3 | 4 | 12 | Alto | Priorizar el Product Backlog y revisar avances en las reuniones del equipo. |
| R4 | Indicadores incorrectos por errores de cálculo o consulta | 3 | 5 | 15 | Alto | Comparar resultados con cálculos manuales y documentar casos de prueba. |
| R5 | Archivos CSV o Excel con columnas o formatos incorrectos | 4 | 3 | 12 | Alto | Validar las columnas requeridas y mostrar mensajes claros al usuario. |
| R6 | Falta de evidencias o revisión independiente de QA | 4 | 3 | 12 | Alto | Asignar responsable, registrar fecha y adjuntar capturas reales de las pruebas. |
| R7 | Beneficios económicos estimados sin datos reales suficientes | 4 | 4 | 16 | Alto | Obtener registros reales de producción, mermas, tiempos y costos antes de afirmar ahorros. |
| R8 | Pérdida de cambios o integración defectuosa en el repositorio | 2 | 4 | 8 | Moderado | Usar commits frecuentes, ramas y revisión de cambios antes de integrar. |

### Matriz de probabilidad e impacto

Las filas representan el impacto y las columnas la probabilidad. Cada celda muestra el producto de ambos valores.

| Impacto \ Probabilidad | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| **5 – Crítico** | 5 | 10 | 15 | 20 | 25 |
| **4 – Grave** | 4 | 8 | 12 | 16 | 20 |
| **3 – Moderado** | 3 | 6 | 9 | 12 | 15 |
| **2 – Menor** | 2 | 4 | 6 | 8 | 10 |
| **1 – Insignificante** | 1 | 2 | 3 | 4 | 5 |

### Seguimiento

El equipo revisará los riesgos al inicio y cierre de cada Sprint. Se actualizarán las valoraciones cuando aparezcan nuevos riesgos o cambien las condiciones del proyecto. Los puntajes representan una valoración inicial del equipo, no mediciones estadísticas.

EOF
