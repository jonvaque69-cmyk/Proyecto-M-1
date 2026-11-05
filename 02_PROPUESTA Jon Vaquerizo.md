# Propuesta del proyecto

Rellenadla y enseñádmela antes de empezar el EDA. Son diez minutos que os pueden ahorrar días.

Nombre: La felicidad en el mundo en datos

## 1. La idea

Título del proyecto: La felicidad por pais
(por ejemplo: "Los vinos que valen lo que cuestan")

¿Qué pregunta responde y a quién le interesa?
(por ejemplo: "A un restaurante le interesa saber qué vinos tienen buena nota sin ser caros, para su carta")
¿Qué tienen los países más felices? ¿Cómo ha cambiado España?


A cualquier persona le puede interesar si busca cambiar de aires y ser feliz. En caso de España le puede venir bien para tener en cuenta los datos e intentar mejorar algunas facetas.

## 2. Los datos

De dónde salen:
- [ ] Kaggle
- [ ] Hugging Face
- [ ] Datos míos (dónde los he encontrado):

Enlace a los datos:Los he cogido de Huggin Face del enlace que has puesto. 
Enlace: `https://huggingface.co/datasets/AhanaBiswas/WorldHappinessDataset2015-2023/resolve/main/World%20Happiness%20Dataset%202015-2023.csv`


Cuántas filas y columnas tienen: 1367 filas y 10 columnas

Qué es cada fila (un vino, un partido, una venta...):

País
Región
Puntuación felicidad
PIB per capita
Apoyo social
Esperanza vida saludable
Libertad
Generosidad
Corrupción
Año


Comprobado (los requisitos están en 03_DATOS.md):
- [ ] Son tabulares, en una sola tabla
- [ ] No los hemos usado en clase
- [ ] Tienen más de 1.000 filas
- [ ] Tienen al menos 6 columnas, con números y con texto
- [ ] Entiendo qué es cada columna
- [ ] Hay algo que limpiar
- [ ] Sé de dónde salen y se pueden usar
- [ ] El CSV limpio pesará menos de 100 MB

## 3. Tres preguntas que quiero responder

1.¿Mayor PIB por capita da mayor felicidad?
2.¿La Corrupción es un factor clave a tener en cuenta?
3.¿Tener mayor "libertad" conlleva ser mas feliz?

## 4. La app

¿Qué filtros pondrías en la barra de la izquierda?
Pais
Region
Puntuación felicidad con slider de 2 puntas
PIB per capita slider 2 puntas
Año con slider 2 puntas


¿Qué pregunta le harías al usuario al final? (como "¿Cuánto cobrarías por tu piso?")

De estos factores :PIB per capita, apoyo social, esperanza vida saludable, libertad, generosidad, corrupción . ¿Con qué 2 factores te quedarías?


¿Tienen coordenadas para hacer un mapa?
-Sí 


## 5. Plan B

Por si los datos principales no sirven, otros distintos:

Enlace:  `https://huggingface.co/datasets/hugginglearners/netflix-shows/resolve/main/netflix_titles.csv`

