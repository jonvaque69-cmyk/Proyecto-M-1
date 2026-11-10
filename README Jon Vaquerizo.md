# Título del proyecto
La felicidad en el mundo en Data

Una frase: qué es y para quién.
A cualquier persona le puede interesar si busca cambiar de aires y ser feliz teniendo en cuenta distintos factores.

## La pregunta

¿Qué tienen los países más felices? ¿Cómo ha cambiado España?

Le puede interesar a cualquier persona que valore la felicidad y que tenga interés en cambiar de país. También creo que le interesa a cada país a la hora de tener en cuenta los distintos factores para poder mejorar internamente.

## Los datos

- De dónde salen: `https://huggingface.co/datasets/AhanaBiswas/WorldHappinessDataset2015-2023/resolve/main/World%20Happiness%20Dataset%202015-2023.csv`
- Cuántos son: 1367 filas y 10 columnas
- Qué es cada fila: País, Región, Puntuación felicidad, PIB per capita, Apoyo social, Esperanza vida saludable, Libertad, Generosidad, Corrupción, Año

## Qué he limpiado y por qué
1º En 2 columnas observo que hay 1 hueco por cada una.
2º Traduzco el nombre de las columnas a castellano.
3º Relleno el hueco de cada columna con la mediana de su columna correspondiente.
4º Al mirar con value_counts observo que hay países que se repiten bastantes veces. 
5º Hay 1196 filas repetidas en la columna "País" pero al ser de años distintos no elimino ninguna.
6º Ahora hago un describe de todo y observo en valores mínimos de muchas columnas que hay valores de 0.0000. Por lo que con estas columnas decido convertir los 0.0000 que hay en todas las filas en valores NaN Y así después relleno cada NaN con la mediana específica de su propia región geográfica.



1-Un país con una economía muy fuerte, unos ingresos altísimos por habitante y unos servicios públicos muy robustos (gracias a un gran PIB) puede amortiguar o "compensar" una peor percepción institucional o de corrupción. Los ciudadanos, al tener su bienestar material, salud y estabilidad económica cubiertos, pueden registrar puntuaciones de felicidad elevadas a pesar de que la corrupción sea notablemente más alta.

2- Al analizar la evolución temporal de España (2015-2023), se observa un fenómeno de alta estabilidad en el índice de felicidad, el cual se mantiene anclado en una franja constante de 6.3 a 6.4 puntos. Esto contrasta con las fluctuaciones de variables económicas individuales (como el crecimiento del PIB), evidenciando que el bienestar subjetivo en sociedades desarrolladas responde a factores culturales e institucionales a largo plazo más que a variaciones coyunturales a corto plazo.

3-La fractura estructural de la felicidad por bloques socioeconómicos y regionales: El análisis de las tendencias centrales revela una brecha geográfica profunda y persistente en los niveles de bienestar global. Regiones como North America and ANZ (~7.18) y Western Europe (~6.81) encabezan holgadamente la clasificación, mientras que Sub-Saharan Africa (~4.29) y South Asia (~4.47) se sitúan en el extremo opuesto, separadas por casi 3 puntos sobre 10.

Asimismo, la mínima discrepancia observada entre la media y la mediana en cada bloque refleja que el nivel de felicidad no depende de casos aislados dentro de un continente, sino que está condicionado por las oportunidades estructurales, el desarrollo humano y la estabilidad institucional compartidas a escala regional.
## La app

![La app](capturas/app.png)



(Qué se puede hacer en la app, en dos o tres frases.)

Enlace: (si la has publicado en Streamlit Community Cloud)

## Cómo ejecutarlo

1. Crear un entorno e instalar las librerías: `pip install -r requirements.txt`
2. El EDA está en `eda.ipynb`.
3. La app se abre con `streamlit run app.py`.

## Autor
Jon Vaquerizo 

(Tu nombre y tu LinkedIn o tu GitHub.)
