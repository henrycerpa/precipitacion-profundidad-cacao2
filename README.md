# PYTHON BASICO 
## PRACTICA 2
## Estudio de condiciones para plantaciones de cacao

En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Para el 2030, se busca luchar contra la desertificación, rehabilitar las tierras y los suelos degradados, incluidas de las tierras afectadas por la desertificación, la sequía y las inundaciones, y procurar lograr un mundo con una degradación neutra del suelo.

El Ministerio de Agricultura y Desarrollo Rural busca recuperar los suelos para el cultivo del cacao. Para poder cumplir con esto han iniciado el análisis para las características del entorno donde se tiene previsto iniciar las plantaciones. Para esta tarea lo requieren a usted y se facilita una tabla que describe si el entorno es apto o no.

| CARACTERISTICAS | SUMAMENTE APTO | MODERADAMENTE APTO | MARGINALMENTE APTO | NO APTO |
| --- | --- | --- | --- | --- |
| Altura sobre el nivel del mar (m.s.n.m) | 400 - 800 | < 400 o 801 - 999 | 1000 - 1200 | > 1200 |
| Temperatura media anual (°C) | 25 - 28 | 29 - 30 o 24 - 21 | 31 - 32 o 20 - 18 | < 18 o > 32 |
| Precipitación anual (mm) | 1800 - 2599 | 2600 - 3199 o 1799 - 1500	| 3200 - 3800 o 1499 - 1200 |	< 1200 o > 3800 |
| Profundidad efectiva del suelo (cm)	| > 100	| 50 - 100	| 25 - 50	| < 25 |

Para esta nueva fase se requiere un estudio más a fondo, por lo cual, el programa debe tener múltiples lecturas de la precipitación anual y profundidad efectiva del suelo de las zonas que se están analizando y arroje los siguientes resultados:

-	Promedio de la precipitación anual formateado a dos cifras decimales
-	Promedio de la profundidad efectiva del suelo formateado a dos cifras decimales
-	Conteo de las categorías resultantes

El número de lecturas que el programa tendrá en cuenta debe ser una variable de entrada.
El criterio para la conclusión será el siguiente:

-	Si ambas variables se encuentran dentro de la misma categoría se escogerá la categoría.
-	Si están en categorías diferentes se escogerá la peor de ellas.


Ejemplo 1:
| Entrada esperada | Salida esperada |
| --- | --- |
| 3	| 2020.00 |
| 2900 73	| 87.67 |
| 750 40	| sumamente apto 1 |
| 2410 150	| moderadamente apto 1 |
| 	| marginalmente apto 0 |
| 	| no apto 1 |


Ejemplo 2:
| Entrada esperada | Salida esperada |
| --- | --- |
| 2	| 1812.50 |
| 1900 101	| 90.50 |
| 1725 80 | sumamente apto 1 |
| 	| moderadamente apto 1 |
| 	| marginalmente apto 0 |
| 	| no apto 0 |
