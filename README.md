# Empresa caso de estudio: Arepas del Valle S.A.S.

**Marco Metodológico de Gestión:** Metodología Ágil - SCRUM

**Asignatura:** Gerencia de Proyectos (Periodo 2026-2)

**Integrantes:** Jerson Esteban Ceballlos Leal, Andrea Carolina Montes Barragan y Sayuri Alexandra Moreno Espinosa.

# 1. INFORMACIÓN DE LA EMPRESA Y DEL PROCESO QUE LA APLICACIÓN VA A MONITOREAR (INCLUIDO EL SIPOC)

## 1.1 Información de la Empresa

Arepas del Valle S.A.S. es una empresa manufacturera de alimentos ubicada en el Valle de Aburrá (Antioquia, Colombia). Se dedica a la elaboración y comercialización a escala industrial de arepas empacadas listas para el consumo, dirigidas principalmente a canales mayoristas, cadenas de supermercados, minimercados locales y distribuidores del área metropolitana.

- **Clasificación Industrial:** De acuerdo con la Clasificación Industrial Internacional Uniforme (CIIU Rev. 4 A.C.), la actividad se clasifica en la Clase 1081: Elaboración de productos de panadería y derivados del maíz.
- **Producto seleccionado para el proyecto:** Arepa tradicional de maíz blanco precocida, empacada en bolsa plástica con atmósfera modificada y refrigerada (presentación paquete por 5 y 10 unidades).

## 1.2 Proceso Objeto de Monitoreo y Problemática

El proceso de producción objeto del monitoreo abarca desde la preparación de la materia prima hasta el empaquetado en cuarto frío:

1. Recepción y preparación de materias primas (harina de maíz pregelatinizada/maíz trillado, agua potable, margarina/aceite, sal).
2. Dosificación y mezclado industrial de masa.
3. Formado, laminado y troquelado de las arepas.
4. Precocción térmica en planchas de asado continúo.
5. Túnel de enfriamiento rápido.
6. Embolsado, termosellado y codificado/rotulado.
7. Almacenamiento refrigerado (4°C).

### La Problemática

Actualmente, el registro de las principales variables del proceso productivo de las arepas, como los kilogramos procesados, las unidades moldeadas, las unidades quemadas o rotas durante la etapa de precocción, los tiempos de paradas mecánicas y las unidades empacadas, se realiza de manera manual en planillas físicas diligenciadas por los operarios de línea. Posteriormente, al finalizar la jornada, esta información es digitada en hojas de cálculo de Excel para su consolidación y seguimiento.

Esta situación genera:

- **Retraso en la disponibilidad de la información:** La gerencia y los supervisores reciben los datos de producción entre 4 y 12 horas después de finalizar el turno, lo que limita su disponibilidad oportuna para la toma de decisiones.
- **Baja trazabilidad y capacidad de reacción:** La actualización de la información no permite identificar oportunamente desviaciones durante el proceso, como fallas en la dosificación de la masa, descalibración de los equipos de precocción o paradas mecánicas.
- **Detección tardía de mermas:** Las unidades quemadas, rotas o que presentan pérdidas durante el proceso pueden identificarse con retraso, dificultando el control de las mermas y generando mayores pérdidas de materia prima y producto terminado.

## 1.3 Visión Ágil del Producto (Product Vision)

Para los Supervisores de Producción y la Gerencia de Operaciones de Arepas del Valle S.A.S., que requieren realizar un seguimiento oportuno del desempeño del proceso productivo, la aplicación web de dashboard es una solución que centraliza el registro de las variables de producción y facilita el seguimiento de indicadores relacionados con la producción, calidad y tiempos de paro. A diferencia del manejo tradicional de la información mediante planillas físicas y hojas de cálculo, el producto permite consultar los datos de manera organizada y visual, facilitando el análisis del desempeño de la producción y la toma oportuna de decisiones.

## 1.4 Diagrama SIPOC

| Proveedores | Entradas | Proceso | Salidas | Clientes |
|---|---|---|---|---|
| Materia prima | Harina de maíz | Inspección de la MP, preparación de la harina, dosificación de agua potable para mezclado con sal y aceite (formación de mezcla). | Masa cruda y homogénea | 1) Área de producción |
|  | Agua potable |  |  | 2) Área de mezclado |
|  | Aceite |  |  | 3) Área de formado |
|  | Sal |  |  | 4) Área de precocción |
| A. Precocción | Masa cruda y homogénea | Precocción de la masa | Arepas precocidas | Área de enfriamiento |
| A. Enfriamiento | Arepas precocidas | Enfriamiento de las arepas precocidas | Arepas precocidas enfriadas, listas para empacar | Área de empaque |
| Área de empaque | Material de empaque (bolsa) | Introducción, sellada y rotulado de las arepas (etiquetas) | Arepas empacadas | Almacenamiento |
| A. Almacenamiento | Arepas empacadas | Almacenamiento refrigerado | Arepas refrigeradas | Supermercados, tiendas y distribuidores |

# 2. DESCRIPCIÓN DETALLADA DE LA ESTRATEGIA CORPORATIVA Y A CUÁL OBJETIVO APORTA LA APLICACIÓN

## 2.1 Estrategia Corporativa

La estrategia corporativa de Arepas del Valle S.A.S. está orientada hacia la excelencia operacional y la digitalización progresiva de sus procesos productivos, con el propósito de mejorar la eficiencia, garantizar la calidad e inocuidad del producto y apoyar la toma de decisiones basada en datos.

En este marco, la empresa busca aplicar principios de Lean Manufacturing para identificar y reducir desperdicios (mudas), tiempos de paro y pérdidas de materia prima o producto. La digitalización de la información de planta permite centralizar las variables críticas del proceso y facilitar el seguimiento de indicadores de producción, calidad y paros, contribuyendo al control de las operaciones y a la optimización de los costos de manufactura.

## 2.2 Contribución a los Objetivos de Desarrollo Sostenible (ODS)

El proyecto se articula con el ODS 12: Producción y Consumo Responsables, contribuyendo principalmente a dos de sus metas:

- **Meta 12.5 – Reducción de la generación de desechos:** La aplicación permite registrar y visualizar las mermas generadas durante las diferentes etapas del proceso productivo, como unidades quemadas, rotas o rechazadas. Esta información facilita la identificación de las principales fuentes de desperdicio y apoya la toma de acciones para reducir las pérdidas de materia prima y producto.
- **Meta 12.2 – Uso eficiente y sostenible de los recursos:** El seguimiento de variables de producción, mermas y tiempos de operación permite identificar oportunidades para mejorar el aprovechamiento de recursos como el maíz, el agua y la energía, favoreciendo una producción más eficiente.

# 3. DEFINIR EL PORTAFOLIO, PROGRAMAS Y PROYECTOS, Y UBICAR ALLÍ EL PROYECTO PROPIO

Para establecer la relación entre el proyecto y las iniciativas estratégicas de Arepas del Valle S.A.S., se presenta a continuación la estructura jerárquica que vincula el portafolio, el programa y el proyecto desarrollado bajo el enfoque Scrum:

| Nivel | Nombre propuesto | ¿Qué representa en el caso? | ¿Qué relación tiene con nuestro proyecto? |
|---|---|---|---|
| **Portafolio** | **Portafolio de Modernización Operacional y Transformación Digital** | Conjunto consolidado de iniciativas de inversión y cambio tecnológico que soportan la visión competitiva de Arepas del Valle S.A.S. | Provee el patrocinio estratégico, alineando el desarrollo del software con los fondos de inversión en modernización industrial. |
| **Programa** | **Programa de Digitalización y Eficiencia de Procesos Productivos** | Agrupación coordinada de proyectos de software, hardware y mejora de procesos orientados a optimizar la manufactura de alimentos. | Es el contenedor directo del proyecto. El software de tableros provee la capa de visualización e inteligencia de datos que retroalimentará a los demás proyectos del programa. |
| **Proyecto** | **Desarrollo de una aplicación web de Dashboard para el monitoreo de indicadores del proceso de producción de arepas.** | Es el esfuerzo temporal que está siendo ejecutado por el equipo de 3 desarrolladores bajo metodología SCRUM (es el proyecto propio). | Es el entregable tecnológico tangible: dashboard interactivo para capturar datos y monitorear la planta. |


# 4. Elección y clasificación del proyecto

## 4.1 Tipo de proyecto

El proyecto corresponde a un **desarrollo de software a la medida y transformación digital**. Consiste en diseñar y construir una aplicación web para capturar, procesar y visualizar indicadores operativos de la planta de Arepas del Valle S.A.S., como:

- Producción.
- Tiempos de paro.
- Mermas.
- Eficiencia global de los equipos (OEE).

La solución no modifica físicamente las máquinas ni el producto, sino que digitaliza el flujo de información para facilitar la toma de decisiones gerenciales. El desarrollo será gestionado y versionado mediante **Git y GitHub**.

## 4.2 Ciclo de vida: metodología Scrum

Se utilizará una metodología ágil basada en **Scrum**, dividida en dos Sprints de dos semanas cada uno. Esta estructura permite entregar valor rápidamente, recibir retroalimentación y controlar el alcance del proyecto.

### Sprint 1: Producto Mínimo Viable (MVP)

**Objetivo:** Digitalizar el registro de producción y paradas, permitiendo visualizar el cumplimiento del turno en tiempo real.

**Funcionalidades principales:**

- Configuración del entorno y la base de datos relacional.
- Formulario web para registrar:
  - Kilos de masa.
  - Paquetes de 5 y 10 unidades.
  - Producción por hora y turno.
- Registro de paradas de máquinas y sus causas.
- Dashboard con comparación entre producción real y meta.
- Visualización del tiempo muerto y acumulado.

**Entregable:** Prototipo funcional de la aplicación web, con base de datos, repositorio Git y tablero operativo.

### Sprint 2: Analítica e indicadores

**Objetivo:** Incorporar el análisis de mermas, el cálculo de OEE y los reportes gerenciales.

**Funcionalidades principales:**

- Módulo de control de mermas e indicadores de calidad.
- Registro de masa residual y unidades no conformes.
- Cálculo automático del OEE:
  - Disponibilidad.
  - Rendimiento.
  - Calidad.
- Dashboard gerencial con filtros por fecha, turno y línea.
- Exportación de reportes ejecutivos.
- Pruebas integrales de la aplicación.
- Autenticación por roles y documentación técnica.

**Entregable:** Versión final de la solución web con dashboards operativos y gerenciales, módulo de sostenibilidad y control de acceso.

## 4.3 Relación con el ODS 12

El proyecto se relaciona con el **Objetivo de Desarrollo Sostenible 12: Producción y Consumo Responsable**, porque busca mejorar el uso de los recursos empleados en la producción de arepas.

La aplicación permitirá:

- Centralizar la información de producción, calidad, paradas y mermas.
- Identificar pérdidas y desperdicios de manera oportuna.
- Controlar el uso de materias primas como harina de maíz, agua y aceite.
- Hacer seguimiento al consumo de recursos energéticos, como el gas utilizado en el horno.
- Generar alertas sobre desviaciones operativas.
- Crear reportes de balance de masa para reducir el desperdicio de alimentos.

Estas acciones contribuyen especialmente al seguimiento y reducción de desperdicios relacionados con la meta 12.5 del ODS 12.

## 4.4 Responsabilidad Social Empresarial (RSE)

El proyecto aporta a la responsabilidad social empresarial mediante:

- **Eficiencia de recursos:** seguimiento de desperdicios y oportunidades de mejora.
- **Sostenibilidad ambiental:** reducción de residuos orgánicos generados por mermas.
- **Bienestar laboral:** disminución de tareas repetitivas y del diligenciamiento manual de planillas.
- **Transparencia:** disponibilidad de información operativa para el personal y la gerencia.
- **Toma de decisiones basada en datos:** fortalecimiento de la colaboración entre las áreas operativas y administrativas.

---

# 5. Estudio de prefactibilidad y factibilidad mediante Business Case

El estudio de factibilidad evalúa la viabilidad técnica, económica, operativa, legal y social de la aplicación web para el monitoreo de indicadores de producción.

## 5.1 Viabilidad técnica

### Tecnologías seleccionadas

El proyecto utilizará tecnologías de código abierto para evitar la dependencia de soluciones comerciales cerradas y permitir un desarrollo propio.

| Componente | Tecnología |
|---|---|
| Lenguaje de programación | Python 3.11 |
| Interfaz y analítica | Streamlit |
| Base de datos local | SQLite |
| Base de datos multiusuario | PostgreSQL |
| Control de versiones | Git y GitHub |
| Metodología | Scrum |

### Localización del proyecto

- **Macrolocalización:** Planta industrial de Arepas del Valle S.A.S., ubicada en el Valle de Aburrá, Antioquia.
- **Microlocalización:** Oficinas de supervisión de producción y dispositivos de consulta ubicados en las áreas operativas, como empaque y cuarto frío.

### Restricciones técnicas

La aplicación se limita a la captura, procesamiento y monitoreo de información en tiempo real. No interviene físicamente ni modifica la maquinaria de producción, como marmitas, troqueladoras u hornos continuos.

## 5.2 Viabilidad económica

La viabilidad económica compara la inversión necesaria para desarrollar la aplicación con los ahorros y beneficios esperados en la planta.

### Presupuesto de inversión inicial

| Concepto | Costo estimado |
|---|---:|
| Desarrollo de la aplicación | $3.500.000 COP |
| Base de datos y almacenamiento | $500.000 COP |
| Diseño del dashboard | $700.000 COP |
| Pruebas e implementación | $500.000 COP |
| Capacitación | $300.000 COP |
| Mantenimiento inicial | $500.000 COP |
| **Total estimado** | **$6.000.000 COP** |

Los valores corresponden a una estimación académica para el estudio de prefactibilidad.

### Fuente de financiación

La inversión se plantea a través del presupuesto del Programa de Transformación y Mejora de Procesos Productivos de Arepas del Valle S.A.S.

### Retorno económico preliminar

| Beneficio | Estimación mensual |
|---|---:|
| Ahorro de tiempo de supervisión | $750.000 COP |
| Disminución de mermas de masa | $1.900.000 COP |
| **Beneficio mensual estimado** | **$2.650.000 COP** |

Con base en estas estimaciones, la inversión inicial de $6.000.000 COP podría recuperarse aproximadamente en **2,3 meses**.

## 5.3 Viabilidad operativa

El proyecto será desarrollado por un equipo de tres estudiantes, organizado mediante roles de Scrum.

| Integrante | Rol | Responsabilidades |
|---|---|---|
| Sayuri | Scrum Master | Facilitar las ceremonias Scrum, eliminar impedimentos, controlar los tiempos y hacer seguimiento al trabajo en GitHub Projects. |
| Andrea | Developer | Diseñar la arquitectura, desarrollar la aplicación en Python y Streamlit, configurar la base de datos y administrar el repositorio GitHub. |
| Esteban | QA | Validar los criterios de aceptación, realizar pruebas de datos, verificar la Definition of Done y evaluar la usabilidad de los dashboards. |

### Operación en planta

- Los supervisores registrarán los datos de producción, lotes y paradas.
- La gerencia consultará los dashboards y los indicadores consolidados.
- El registro se diseñará mediante listas desplegables para facilitar el uso.
- Se estima que el registro de cada lote tome menos de 40 segundos.
- No será necesario contratar personal adicional.
- Se contempla capacitación para supervisores y operarios.

## 5.4 Viabilidad legal

El proyecto debe garantizar el manejo adecuado, almacenamiento y protección de la información utilizada por la aplicación.

### Protección de datos

Se tendrá en cuenta la **Ley 1581 de 2012 de Colombia**, mediante:

- Uso de identificadores internos de turno.
- Evitar la recolección innecesaria de datos personales.
- Definición de perfiles de acceso.
- Protección de la información almacenada.

### Propiedad intelectual y licenciamiento

- El software será desarrollado desde cero.
- Se utilizarán librerías de código abierto con licencias permisivas, como MIT y Apache 2.0.
- El desarrollo contará con evidencia y control de versiones en GitHub.
- Se respetarán los derechos de autor y las condiciones académicas del proyecto.

### Control de acceso

Se establecerán perfiles diferenciados:

- **Operador:** registro de información operativa.
- **Supervisor:** consulta y seguimiento de la información de producción.
- **Administrador:** gestión general del sistema y los permisos.

Estos perfiles permitirán mantener la trazabilidad y prevenir modificaciones no autorizadas.

## 5.5 Viabilidad social

### Mapa de interesados

- **Beneficiarios principales:**
  - Supervisores de turno, porque se reduce el diligenciamiento manual.
  - Gerencia, porque obtiene información actualizada del rendimiento de la planta.

- **Posible resistencia:**
  - Operarios de planta que podrían percibir la digitalización como un mecanismo de vigilancia o temer que los errores queden expuestos.

- **Responsable de la decisión:**
  - Gerente de Operaciones, como patrocinador del proyecto.

### Plan de relacionamiento y mitigación

La aplicación se presentará como una herramienta de apoyo y mejora operativa, no como un mecanismo de control punitivo.

Se buscará:

- Evitar reprocesos.
- Justificar paradas que no dependan del operario.
- Identificar problemas relacionados con presión de gas o falta de materia prima.
- Realizar pruebas piloto participativas con operarios líderes durante el Sprint 1.
- Promover la aceptación de la herramienta mediante la participación del personal.

## 5.6 Análisis de construir o comprar

Se compararon tres alternativas:

1. No hacer nada y mantener el proceso actual.
2. Comprar un software comercial.
3. Construir una aplicación propia con Scrum, Python, Streamlit y GitHub.

| Criterio | No hacer nada | Comprar software | Construir aplicación propia |
|---|---|---|---|
| Descripción | Planillas de papel y transcripción a Excel. | Software industrial comercial. | Aplicación web a la medida. |
| Inversión inicial | $0 COP, pero con pérdidas operativas. | Superior a $25.000.000 COP. | Aproximadamente $6.000.000 COP. |
| Costos recurrentes | Pérdidas por mermas e ineficiencias. | Suscripciones y soporte anual. | Bajos, con posibilidad de alojamiento local. |
| Adaptación al proceso | Baja; no calcula automáticamente los tiempos muertos. | Puede ser rígida y exigir cambios en los procesos. | Adaptada a las etapas del proceso de producción. |
| Disponibilidad de datos | Entre 8 y 12 horas después del turno. | En tiempo real después de una integración prolongada. | En tiempo real, en menos de 2 minutos después del registro. |
| Cumplimiento académico | No resuelve el problema de ingeniería. | No cumple con el desarrollo propio requerido. | Cumple mediante código abierto y evidencia en GitHub. |
| Decisión | Descartada. | Descartada. | Seleccionada. |

### Alternativa seleccionada

Se selecciona la construcción de una **aplicación web propia**, debido a que:

- Se adapta a las necesidades específicas de la planta.
- Tiene una inversión inicial moderada.
- Permite controlar el código y las versiones en GitHub.
- Facilita la incorporación de indicadores personalizados.
- Cumple con las condiciones académicas del proyecto.
- Permite consultar los datos en tiempo real.

## 5.7 Estimación de beneficios

Los beneficios se establecen comparando la situación actual con las metas esperadas después de implementar la aplicación.

| Beneficio | Situación actual | Meta con la aplicación | Indicador |
|---|---|---|---|
| Ahorro de tiempo administrativo | 1,5 horas diarias por turno para transcribir datos. | Menos de 15 minutos de captura por turno. | Reducción de al menos el 80 % del tiempo de digitación y consolidación. |
| Disponibilidad de información | Datos disponibles entre 8 y 12 horas después de la jornada. | Dashboard visible durante el turno. | Datos disponibles en menos de 2 minutos después del evento. |
| Reducción de mermas | Merma estimada entre el 4,5 % y el 5 %. | Meta de merma igual o inferior al 2,5 %. | Porcentaje de merma sobre la masa preparada. |
| Identificación de paradas | Paradas sin clasificación ni medición precisa. | Registro de causas mecánicas, eléctricas y operativas. | Minutos de inactividad y causas asignadas. |
| Apoyo a decisiones gerenciales | Decisiones basadas en datos del día anterior. | Decisiones durante el turno con cálculo de OEE. | Frecuencia de consulta del dashboard. |

Estas metas son estimaciones de prefactibilidad y deberán validarse durante el desarrollo, las pruebas y la implementación del proyecto.

## 5.8 Criterios de éxito

| Criterio | Indicador | Resultado esperado |
|---|---|---|
| Funcionamiento de la aplicación | Funcionalidades del Product Backlog implementadas. | 100 % de las funcionalidades del alcance operativas. |
| Disponibilidad de indicadores | Indicadores de producción, paros, mermas y OEE. | Indicadores disponibles y dinámicos. |
| Registro de información | Registros de producción ingresados correctamente. | Al menos 95 % de registros sin errores de validación. |
| Uso de la aplicación | Usuarios capacitados y con acceso. | 100 % de los usuarios previstos capacitados. |
| Reducción del tiempo de consolidación | Comparación del procesamiento antes y después. | Reducción mínima del 30 %. |
| Satisfacción de los usuarios | Encuesta de satisfacción y facilidad de uso. | Al menos 80 % de valoración positiva. |

# 8. GESTIÓN DEL PROYECTO BAJO EL MARCO DE TRABAJO SCRUM

Para el desarrollo de la aplicación web de monitoreo del proceso productivo de Arepas del Valle S.A.S. se adopta el marco de trabajo Scrum bajo un ciclo de vida adaptativo, definido en dos Sprints de dos semanas cada uno.

El Sprint 1 corresponde a la construcción del Producto Mínimo Viable (MVP), orientado a la captura y visualización de información operativa. El Sprint 2 incorpora las funcionalidades analíticas y gerenciales necesarias para la versión final.

Git y GitHub serán utilizados para el control de versiones, seguimiento del trabajo y trazabilidad de los avances realizados durante cada Sprint.

## 8.1 Equipo Scrum

El proyecto será ejecutado por un equipo de tres estudiantes:

| Integrante | Responsabilidad Scrum | Funciones principales |
|---|---|---|
| **Sayuri** | Scrum Master | Facilitar la aplicación de Scrum, coordinar Sprint Planning, Sprint Review y Retrospective, apoyar la solución de impedimentos y realizar seguimiento en GitHub Projects. |
| **Andrea** | Developer | Diseñar y construir la solución web, desarrollar la aplicación en Python/Streamlit, configurar la base de datos, integrar funcionalidades y administrar ramas y commits. |
| **Esteban** | QA / Aseguramiento de la calidad | Validar criterios de aceptación, realizar pruebas funcionales y de integridad de datos, verificar la Definition of Done y evaluar la usabilidad de los tableros. |

El **Product Owner** corresponde al profesor de la asignatura, quien actúa como referente para la validación y retroalimentación del producto. No forma parte del equipo ejecutor de tres estudiantes.

## 8.2 Product Backlog priorizado

El Product Backlog contiene las funcionalidades que serán desarrolladas para cumplir la visión del producto. Las historias HU-01 a HU-08 se distribuyen entre los dos Sprints según su prioridad y dependencia funcional.

| Prioridad | Historia | Descripción | Sprint |
|---:|---|---|---:|
| 1 | **HU-01** | Configuración del entorno y base de datos relacional | 1 |
| 2 | **HU-02** | Formulario web para el registro operativo de producción | 1 |
| 3 | **HU-03** | Registro de paradas de máquinas y causas | 1 |
| 4 | **HU-04** | Dashboard operativo de producción, cumplimiento y tiempos de paro | 1 |
| 5 | **HU-05** | Registro y control de mermas e indicadores de calidad | 2 |
| 6 | **HU-06** | Cálculo automatizado del OEE | 2 |
| 7 | **HU-07** | Dashboard ejecutivo/gerencial con filtros | 2 |
| 8 | **HU-08** | Exportación de reportes y pruebas integrales | 2 |

La prioridad responde a una lógica de dependencia: primero se desarrolla la infraestructura y captura de información y posteriormente los indicadores, análisis gerencial y reportes.

## 8.3 Estimación del trabajo

La estimación inicial se realizará mediante **puntos de historia**, utilizando una escala relativa tipo Fibonacci. Los Developers podrán ajustar las estimaciones durante la Sprint Planning de acuerdo con la complejidad, incertidumbre y dependencias.

| Historia | Estimación inicial | Sprint |
|---|---:|---:|
| HU-01 | 3 puntos | 1 |
| HU-02 | 5 puntos | 1 |
| HU-03 | 5 puntos | 1 |
| HU-04 | 13 puntos | 1 |
| HU-05 | 5 puntos | 2 |
| HU-06 | 13 puntos | 2 |
| HU-07 | 5 puntos | 2 |
| HU-08 | 8 puntos | 2 |

Durante la ejecución también se registrará el esfuerzo estimado y el esfuerzo real para evaluar la precisión de la planificación y generar aprendizaje para los siguientes Sprints.

## 8.4 Sprint 1 – Construcción del MVP

### Meta del Sprint

Construir un MVP funcional que permita digitalizar el registro de producción y paradas, almacenar la información en una base de datos y visualizar el comportamiento operativo mediante un dashboard.

### Sprint Backlog

| Historia | Actividades principales |
|---|---|
| **HU-01** | Configurar repositorio y entorno, establecer dependencias, crear estructura inicial, diseñar modelo relacional y configurar conexión con la base de datos. |
| **HU-02** | Diseñar formulario de registro, incorporar turno, producción, kilogramos de masa y paquetes producidos, establecer validaciones, conectar con la base de datos y realizar pruebas. |
| **HU-03** | Diseñar formulario de paradas, definir catálogo de causas, registrar inicio, finalización y duración, almacenar información y validar registros. |
| **HU-04** | Construir dashboard operativo con producción real frente a meta, tiempo muerto y tiempo acumulado, integrando los datos almacenados. |

**Actividades transversales:** integración del código, pruebas funcionales, revisión de criterios de aceptación, control de versiones y documentación.

### Plan de trabajo del Sprint 1

| Periodo | Actividades | Resultado esperado |
|---|---|---|
| **Semana 1** | Sprint Planning, configuración del entorno y base de datos, desarrollo de HU-01 y avance de HU-02 y HU-03. | Infraestructura funcional y formularios iniciales. |
| **Semana 2** | Finalización de HU-02 y HU-03, desarrollo de HU-04, integración, pruebas, revisión y retrospectiva. | MVP funcional v0.5. |

### Incremento esperado

Al finalizar el Sprint 1 se espera disponer del **Incremento 1 – Prototipo v0.5**, compuesto por:

- Aplicación web operativa.
- Base de datos transaccional.
- Dashboard de monitoreo de planta.
- Repositorio Git con trazabilidad de cambios.

El tablero permitirá consultar información de producción y paradas utilizando datos disponibles para las pruebas.

## 8.5 Sprint 2 – Analítica y versión final

### Meta del Sprint

Incorporar el control de mermas, indicadores de calidad y OEE, funcionalidades de análisis gerencial y generación de reportes, junto con las pruebas necesarias para disponer de la versión final.

### Sprint Backlog

| Historia | Actividades principales |
|---|---|
| **HU-05** | Diseñar módulo de mermas, registrar masa residual y unidades no conformes, establecer cálculos y porcentajes e integrar los datos al dashboard. |
| **HU-06** | Diseño de cálculo, calcular disponibilidad, rendimiento y calidad, consolidar el OEE y validar las fórmulas con datos de prueba. |
| **HU-07** | Construir dashboard ejecutivo con filtros por fecha, turno y línea, mostrando producción, paros, mermas y OEE. |
| **HU-08** | Implementar exportación de reportes, realizar pruebas integrales, corregir errores, comprobar criterios de aceptación y preparar la versión final. |

**Actividades transversales:** integrar autenticación y control de acceso, consolidar código, realizar pruebas finales, validar la Definition of Done y preparar la entrega.

La autenticación por roles será un requisito transversal de la versión **v1.0**. Los perfiles previstos son:

- Operador
- Supervisor
- Administrador

### Plan de trabajo del Sprint 2

| Periodo | Actividades | Resultado esperado |
|---|---|---|
| **Semana 3** | Sprint Planning, desarrollo de HU-05 y HU-06, integración de cálculos y pruebas iniciales. | Módulos de mermas y OEE funcionales. |
| **Semana 4** | Desarrollo de HU-07 y HU-08, integración final, pruebas integrales, revisión y retrospectiva. | Versión final v1.0. |

### Incremento esperado

El segundo incremento corresponde a la **versión final v1.0**, que integrará:

- Captura de información.
- Control de paradas.
- Control de mermas.
- Indicadores OEE.
- Dashboard operativo.
- Dashboard gerencial.
- Exportación de reportes.
- Control de acceso.
- Documentación técnica.

## 8.6 Definition of Done

Una historia de usuario se considerará terminada cuando cumpla simultáneamente con los siguientes criterios:

1. La funcionalidad está desarrollada e integrada al proyecto.
2. Cumple todos los criterios de aceptación de la historia.
3. Se realizaron las pruebas funcionales correspondientes.
4. Los datos se almacenan y procesan correctamente.
5. No existen errores críticos que impidan utilizar la funcionalidad.
6. Fue revisada por el responsable de QA.
7. El código está registrado en el repositorio mediante su respectivo commit.
8. La documentación técnica necesaria fue actualizada.
9. La tarjeta de GitHub Projects puede trasladarse al estado **Done**.

Una historia que solamente tenga código desarrollado, pero no haya sido probada o validada, no se considerará terminada.

## 8.7 Eventos Scrum considerados en el proyecto

| Evento | Aplicación en el proyecto |
|---|---|
| **Sprint Planning** | Al inicio de cada Sprint se establecerá la meta, se seleccionarán las historias y se definirá el plan de trabajo. |
| **Sprint Review** | Al finalizar cada Sprint se presentará el incremento desarrollado y se recibirá retroalimentación. |
| **Sprint Retrospective** | Después de la Review, el equipo analizará el proceso, dificultades y acciones de mejora. |
| **Daily Scrum** | Se realizará durante la ejecución de cada Sprint y su evidencia será registrada mediante grabaciones. |

Las grabaciones de los Daily Scrum serán incorporadas al repositorio de GitHub como evidencia de seguimiento y ejecución.

## 8.8 Tablero de seguimiento del proyecto

El seguimiento visual se realizará mediante **GitHub Projects**.

Flujo de estados:

**Backlog → Por hacer → En desarrollo → En pruebas → Terminado**

Cada tarjeta estará asociada a una historia de usuario y, cuando sea necesario, a las tareas técnicas requeridas.

El tablero permitirá:

- Visualizar el estado de cada historia.
- Identificar trabajo pendiente.
- Registrar responsables.
- Asociar historias a un Sprint.
- Realizar seguimiento a las pruebas.
- Vincular cambios del código con el trabajo realizado.

Las tarjetas utilizarán el identificador de la historia, por ejemplo: **HU-01, HU-02, HU-03**, etc.

## 8.9 Estrategia de control de versiones en GitHub

GitHub será utilizado como repositorio central del código fuente y documentación técnica.

| Elemento | Uso |
|---|---|
| **main** | Versión estable del proyecto. |
| **Ramas feature** | Desarrollo de funcionalidades asociadas a historias. |
| **Commits** | Cada avance relevante estará asociado a una historia o tarea. |
| **Pull Requests** | Integración de funcionalidades después de revisión y pruebas. |
| **GitHub Projects** | Seguimiento del Product Backlog y Sprint Backlogs. |

