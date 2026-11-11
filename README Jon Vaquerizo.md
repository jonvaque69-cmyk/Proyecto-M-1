La felicidad en el mundo en Data

    -A cualquier persona le puede interesar si busca cambiar de aires y ser feliz teniendo en cuenta distintos factores.

    -¿Qué tienen los países más felices? ¿Cómo ha cambiado España?

    -Le puede interesar a cualquier persona que valore la felicidad y que tenga interés en cambiar de país. También creo que le interesa a cada país a la hora de tener en cuenta los distintos factores para poder mejorar internamente.

·LOS DATOS

    -  De dónde salen: `https://huggingface.co/datasets/AhanaBiswas/WorldHappinessDataset2015-2023/resolve/main/World%20Happiness%20Dataset%202015-2023.csv`
    - Cuántos son: 1367 filas y 10 columnas
    - Qué es cada fila: País, Región, Puntuación felicidad, PIB per capita, Apoyo social, Esperanza vida saludable, Libertad, Generosidad, Corrupción, Año

    -Qué he limpiado y por qué:
    1º En 2 columnas observo que hay 1 hueco por cada una.
    2º Traduzco el nombre de las columnas a castellano.
    3º Relleno el hueco de cada columna con la mediana de su columna correspondiente.
    4º Al mirar con value_counts observo que hay países que se repiten bastantes veces. 
    5º Hay 1196 filas repetidas en la columna "País" pero al ser de años distintos no elimino ninguna.
    6º Ahora hago un describe de todo y observo en valores mínimos de muchas columnas que hay valores de 0.0000. Por lo que con estas columnas decido convertir los 0.0000 que hay en todas las filas en valores NaN Y así después relleno cada NaN con la mediana específica de su propia región geográfica.

·CONCLUSIONES DEL EDA

    1. Los pilares fundamentales y el "efecto amortiguador" de la economía
    El hallazgo: El PIB per cápita (0.73) y la esperanza de vida (0.68) actúan como los dos grandes motores universales de la felicidad.

    La conclusión: Una economía altamente desarrollada y unos servicios de salud sólidos tienen la capacidad de amortiguar deficiencias institucionales. Es decir, los ciudadanos de países prósperos logran mantener niveles elevados de bienestar percibido a pesar de que la corrupción o la desconfianza institucional sean notablemente más altas, demostrando que el bienestar material pesa mucho en el balance diario.

    2. La inercia y estabilidad del bienestar en economías consolidadas (El caso de España)
    El hallazgo: Al analizar la evolución temporal de España (2015-2023), el índice de felicidad se muestra inusualmente estanco y estable (franja constante de 6.3 a 6.4 puntos).

    La conclusión: El bienestar subjetivo en sociedades desarrolladas no responde de forma directa a las fluctuaciones coyunturales del PIB o a crisis económicas a corto plazo. Se trata de una métrica estructural que responde a factores culturales, redes de apoyo y estilos de vida consolidados a largo plazo, mostrando una gran resiliencia frente a los vaivenes macroeconómicos anuales.

    3. La fractura estructural y la desigualdad sistémica global
    El hallazgo: La profunda brecha geográfica que separa a bloques como North America & ANZ (~7.18) o Western Europe (~6.81) frente a Sub-Saharan Africa (~4.29) o South Asia (~4.47), con una diferencia de casi 3 puntos completos.

    La conclusión: La mínima discrepancia estadística entre la media y la mediana en cada bloque confirma que no estamos ante casos aislados o excepciones geográficas, sino ante una realidad sistémica. La felicidad a escala global está directamente condicionada por el acceso estructural a las oportunidades, el desarrollo humano y la estabilidad institucional compartida a escala regional.
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
