# Proyecto-final_accidentes_trafico

Los accidentes de tráfico son frecuentes en las sociedades desarrolladas. Dada su magnitud algunas personas los consideran como una auténtica epidemia de las sociedades actuales. El objetivo de este Dashboard es mostrar de una manera sencilla y visual todos los accidentes que han sido ocasionados en Madrid en el ao 2021. Estudiaremos varias variables y veremos cuales pueden afectar a que en un distrito haya un nulero mucho mayor de accidentes que en otro.

**Variables estudiadas**

- Nº Expediente : Es el número de expediente de cada accidente de trafico que tiene lugar en Madrid en 2021
- Fecha : Fecha en la que tiene lugar el accidente
- Hora : Hora en la que tiene lugar el accidente
- Día semana : Dia en el que ha tenido lugar el accidente
- Month : Mes en el que ha tenido lugar el accidente
- Distrito : Distrito de Madrid
- Tipo de accidente : Es el tipo de accidente que ha tenido lugar
- Tipo de vehículo : Es el tipo de vehiculo que ha estado implicado
- Tipo de persona : Es el tipo de persona que ha estado implicado
- Rango edad; sexo : De todas las personas implicadas
- Lesividad : Gravedad de la lesión, las consecuencias que ha tenido en cada persona implicada
- Latitud ; Longitud : Coordenadas donde ha tenido lugar el accidente
- Temperatura ; punto de condensación ; presión ; velocidad del viento : Datos de meterorologia tanto el min, avg y max del dia en el que transcurrió cada accidente
- Locales actividades : número de actividades en locales Abiertos con Tipo de acceso Puerta de calle y Agrupados, clasificados por Actividad. Dato por distrito.
- Población : Población de cada distrito
- Renta media : Renta media de cada distrito

**Working Plan**

1) Coger y analizar la información : Hemos extraido un fichero en formato Excel del Portal de Datos abiertos del Ayuntamiento de Madrid: https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=7c2843010d9c3610VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default

2) Limpieza / transfromación de la información: Hemos hecho una transformación de la información reemplazando nulos, homogeneizando las columnas, eliminando duplicados, cambiado el tipo de datos, eliminando alguna columna que no ibamos a utilizar y hemos creado columnas nuevas con información que hemos spliteado.

3) Alimentar la base de datos con información meteorológica de cada distrito mediante Selenium. Hemos scrapeado la web https://www.wunderground.com/history" y hecho limpieza previo al mergeo de ambos ficheros.

4) Generar dataframes para la Visualización : Hemos generado distintos dataframes utilizando agrupaciones y hemos generado varios gráficos que utilizamos para nuestro estudio y sacar conclusiones más adelante.

5) Dashboard : Hemos incluido nuestros datos limpios en Tableu y hemos incluido datos adicionales referente a los distritos, que hemos exportado de nuevo del Portal de Datos abiertos del Ayuntamiento de Madrid https://www.madrid.es/portales/munimadrid/es/Inicio/El-Ayuntamiento/Estadistica/Distritos-en-cifras/Distritos-en-cifras-Informacion-de-Distritos-/?vgnextfmt=default&vgnextoid=74b33ece5284c310VgnVCM1000000b205a0aRCRD&vgnextchannel=27002d05cb71b310VgnVCM1000000b205a0aRCRD


**Estructura de los archivos del proyecto**

La estructura del proyecto se compone de:
a. Una carpeta de notebooks:
1. Análisis Exploratorio.ipynb : Contiene una exploración del DataFrame
2. Transformación.ipynb : Contiene la limpieza de datos del excel incial de 2021_Accidentalidad
3. Selenium.ipynb : Contiene el escrapeo de una web de meteo y el mergeo con el DF principal limpio 
4. Visualización.ipynb : Gráficos del estudio

b. data folder: contiene la data inicial utilizada y las generadas para el estudio

c. Dashboard con las conclusiones
