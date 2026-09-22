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
