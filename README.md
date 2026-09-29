# Empresa caso de estudio: Arepas del Valle S.A.S.

**Marco Metodológico de Gestión:** Metodología Ágil - SCRUM

**Asignatura:** Gerencia de Proyectos (Periodo 2026-2)

**Integrantes:** Jerson Esteban Ceballlos Leal, Andrea Carolina Montes Barragan y Sayuri Alexandra Moreno Espinosa.

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

El proyecto se ubica dentro de una estructura jerárquica de iniciativas de modernización y digitalización de los procesos productivos de Arepas del Valle S.A.S.:

| Nivel | Nombre propuesto | Relación con el proyecto |
|---|---|---|
| **Portafolio** | **Portafolio de Modernización Operacional y Transformación Digital** | Orienta las iniciativas relacionadas con la modernización y transformación digital de la empresa. |
| **Programa** | **Programa de Digitalización y Eficiencia de Procesos Productivos** | Agrupa iniciativas orientadas a mejorar y digitalizar los procesos productivos. |
| **Proyecto** | **Desarrollo de una aplicación web de Dashboard para el monitoreo de indicadores del proceso de producción de arepas** | Es el proyecto desarrollado por el equipo y tiene como objetivo centralizar el registro y seguimiento de información de producción, calidad y tiempos de paro. |

# 4. ELECCIÓN Y CLASIFICACIÓN DEL PROYECTO

## 4.1 Tipo de proyecto

El proyecto corresponde a un **desarrollo de software a la medida y transformación digital**. Consiste en construir una aplicación web para registrar, procesar y visualizar información operativa de la planta, relacionada con producción, tiempos de paro, mermas e indicadores.

La solución digitaliza el flujo de información sin modificar físicamente las máquinas ni el producto. El desarrollo será gestionado y versionado mediante **Git y GitHub**.

## 4.2 Ciclo de vida: metodología Scrum

Se utilizará una metodología ágil basada en **Scrum**, organizada en dos Sprints relacionados con las fechas de entrega del proyecto.

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

La inversión inicial estimada para el desarrollo del proyecto es de **$6.000.000 COP**, correspondiente a desarrollo, base de datos, diseño, pruebas, capacitación y mantenimiento inicial.

Los beneficios económicos estimados son:

| Beneficio | Estimación mensual |
|---|---:|
| Ahorro de tiempo de supervisión | $750.000 COP |
| Disminución de mermas de masa | $1.900.000 COP |
| **Beneficio mensual estimado** | **$2.650.000 COP** |

Con estas estimaciones, el período de recuperación preliminar de la inversión es de aproximadamente **2,3 meses**.

> Los valores corresponden a estimaciones académicas de prefactibilidad y deberán validarse durante el desarrollo y las pruebas del proyecto.

## 5.3 Viabilidad operativa

El proyecto será desarrollado mediante roles Scrum:

| Integrante | Rol |
|---|---|
| Sayuri | Scrum Master |
| Andrea | Developer |
| Esteban | QA |

Los supervisores registrarán la información operativa y la gerencia consultará los datos e indicadores mediante la aplicación.

El registro de un dato individual se estima en menos de **40 segundos**. Este tiempo corresponde al ingreso de un registro y no al tiempo total de captura y consolidación del turno.

## 5.4 Viabilidad legal

El proyecto tendrá en cuenta la **Ley 1581 de 2012 de Colombia** para el manejo de información personal y establecerá perfiles de acceso según las funciones de los usuarios.

El software será desarrollado por el equipo y se utilizarán tecnologías y librerías de código abierto, respetando sus respectivas condiciones de licencia.

## 5.5 Viabilidad social

El proyecto busca reducir tareas repetitivas de registro manual y facilitar el acceso a información operativa para supervisores y gerencia.

Se contempla la participación del personal durante las pruebas y capacitación, con el propósito de facilitar la adopción de la herramienta y presentar la digitalización como apoyo a la mejora del proceso.

## 5.6 Análisis de construir o comprar

Se analizaron tres alternativas:

| Alternativa | Característica principal |
|---|---|
| Mantener el proceso actual | Continuar con planillas físicas y consolidación en Excel. |
| Comprar software | Utilizar una solución comercial para el seguimiento de producción. |
| **Construir aplicación propia** | Desarrollar una solución a la medida utilizando Python, Streamlit y GitHub. |

La alternativa considerada para el proyecto es la **construcción de una aplicación propia**, debido a que permite adaptar la solución al proceso estudiado, controlar el código y desarrollar los indicadores requeridos dentro del proyecto académico.

## 5.7 Estimación de beneficios

| Beneficio | Situación actual | Meta con la aplicación |
|---|---|---|
| Tiempo administrativo | 1,5 horas diarias por turno para transcripción y consolidación. | Menos de 15 minutos de captura por turno y reducción de al menos el 80 % del tiempo destinado a digitación y consolidación. |
| Disponibilidad de información | Datos disponibles entre 8 y 12 horas después de la jornada. | Información disponible durante el turno, con registros visibles en menos de 2 minutos después del evento. |
| Mermas | Estimación entre 4,5 % y 5 %. | Meta igual o inferior al 2,5 %. |
| Paradas | Sin clasificación ni medición precisa. | Registro de causas y tiempos de inactividad. |
| Toma de decisiones | Información del día anterior. | Consulta de información durante el turno. |

Estas metas son estimaciones de prefactibilidad y deberán validarse durante el desarrollo y las pruebas.

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
| Esteban | QA |

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

**Periodo:** Inicio del proyecto hasta el **29/09/2026**.

El Sprint 1 corresponde al primer incremento del proyecto y está orientado a la construcción del Producto Mínimo Viable.

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

## 8.5 Sprint 2: Analítica e indicadores

**Fecha de cierre:** **30/10/2026**, correspondiente a la segunda entrega del proyecto.

El Sprint 2 corresponde al segundo incremento del proyecto y está orientado a incorporar las capacidades de analítica e indicadores definidas para la versión final.

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

La solución corresponde a una aplicación web orientada a la captura, almacenamiento, procesamiento y visualización de información del proceso productivo de **Arepas del Valle S.A.S.**

La arquitectura se organiza en cuatro componentes:

1. **Presentación:** interfaz web desarrollada en Streamlit para registrar información y consultar indicadores.
2. **Lógica y procesamiento:** desarrollada en Python 3.11 para validar registros, procesar información y calcular indicadores.
3. **Datos:** base de datos relacional. Durante el desarrollo se utilizará SQLite y PostgreSQL se contempla para escenarios multiusuario.
4. **Control de versiones:** Git y GitHub para gestionar el desarrollo y mantener la trazabilidad de los cambios.

La estructura de datos contempla información de:

| Entidad | Información principal |
|---|---|
| **Turnos** | Fecha, turno y línea de producción |
| **Producción** | Kilogramos de masa, paquetes producidos y meta |
| **Paradas** | Inicio, finalización, duración y causa |
| **Mermas** | Masa residual, unidades no conformes y motivo |
| **Usuarios** | Perfil y permisos para la versión final |

### Flujo general

```text
Usuario de planta
      ↓
Interfaz web
      ↓
Validación de datos
      ↓
Base de datos
      ↓
Procesamiento de indicadores
      ↓
Dashboard
      ↓
Toma de decisiones

Estos objetivos ya fueron establecidos en el diagnóstico y **Business Case** del proyecto.
