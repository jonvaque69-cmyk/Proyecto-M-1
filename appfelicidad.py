# La app de mi proyecto
# Para verla, en la terminal: streamlit run app.py
# Son los mismos pasos que en app_pisos.py y app_titanic.py. Si te atascas, busca el mismo paso allí.



# Paso 1. La página
# 1.1 Importa streamlit y pandas.

import streamlit as st # para la página
import pandas as pd  # para las tablas
import plotly.express as px

# 1.2 Pon el nombre de la pestaña del navegador, la página a todo lo ancho y un título que diga de qué va tu proyecto.

st.set_page_config(page_title="La Felicidad",page_icon="😊",layout="wide") # el nombre de la pestaña, el icono y la página a todo lo ancho
st.title("😊La Felicidad en el mundo en datos🌍") # el título de la página

# 1.3 Debajo, una o dos frases con st.write: qué pregunta responde la app y de dónde salen los datos.

st.markdown("### ¿Qué tienen los países más felices? ¿Cómo ha cambiado España?")
st.write("Te diremos cúal es el secreto de la felicidad...así que tu dirás...¿a qué país te irías?")
st.write("Los datos se han obtenido de huggingface del dataset World Happiness Report 2023, con datos elaborados entre los años 2015 y 2023.")


# Paso 2. Los datos
# 2.1 La función cargar_datos, con @st.cache_data encima, que lea "datos/datos_limpios.csv" y lo devuelva.
#     La limpieza ya está hecha en el cuaderno, así que la función solo lee y devuelve, como en la carta del bar.

@st.cache_data # lee y limpia el CSV una sola vez, no en cada clic
def cargar_datos():
    felicidad = pd.read_csv("felicidad_limpio.csv")
    return felicidad



# 2.2 Llama a la función y guarda la tabla en una variable con el nombre de tus datos.

felicidad = cargar_datos()
st.write("Tenemos",len(felicidad), "registros de países entre los años 2015 y 2023.")



# Paso 3. Los filtros
# 3.1 En la barra de la izquierda (with st.sidebar:), al menos dos filtros:
#     un desplegable o unos botones para una columna de texto, con "Todos" al principio,
#     y una barra para una columna de números.

with st.sidebar: #todo lo que pongamos aquí va en la barra de la izquierda
    st.header("Filtros") #un título para los filtros
    regiones= sorted(felicidad["region"].unique()) #las regiones ordenadas alfabéticamente
    regiones.insert(0, "Todas") #Añadimos la opción de todas
    region=st.selectbox("Región", regiones) #el desplegable de las regiones
    paises= sorted(felicidad["pais"].unique()) #los países ordenados alfabéticamente
    paises.insert(0, "Todos") #Añadimos la opción de todos
    pais=st.selectbox("País", paises) #el desplegable de los países
    anos_disponibles = sorted(felicidad["año"].unique())
    anos_seleccionados = st.multiselect("Años", options=anos_disponibles, default=anos_disponibles)
    puntuacion_min, puntuacion_max = st.slider("Puntuación de felicidad", 0.0, 8.0, (0.0, 8.0)) # la puntuación en un slider de dos puntas
    pib_min, pib_max = st.slider("PIB per cápita", 0.0, 2.21, (0.0, 2.21)) # el PIB per cápita en un slider de dos puntas
    esperanza_min, esperanza_max = st.slider("Esperanza de vida", 0.0, 1.15, (0.0, 1.15)) # la esperanza de vida en un slider de dos puntas
    corrupcion_min, corrupcion_max = st.slider("Corrupción", 0.0, 0.60, (0.0, 0.60)) # la corrupción en un slider de dos puntas

# Paso 4. Filtrar
# 4.1 Empieza con filtrados = tu tabla, y después aplica un filtro por cada widget, como en los pisos.
filtrados= felicidad #empezamos con todos los países y vamos filtrando

if region != "Todas":  # si se ha elegido una región en concreto
    filtrados= filtrados[filtrados["region"]==region]   #nos quedamos con los países de esa región

if pais != "Todos":  # si se ha elegido un país en concreto
    filtrados= filtrados[filtrados["pais"]==pais]   #nos quedamos con ese país

filtrados= filtrados[filtrados["año"].isin(anos_seleccionados)] #nos quedamos con los años seleccionados

filtrados=filtrados[(filtrados["puntuacion_felicidad"]>= puntuacion_min)] #nos quedamos con los países que tengan la puntuación mínima
filtrados=filtrados[(filtrados["puntuacion_felicidad"]<= puntuacion_max)] #nos quedamos con los países que tengan la puntuación máxima

filtrados= filtrados[(filtrados["pib_per_capita"]>= pib_min)] #nos quedamos con los países que tengan el PIB mínimo
filtrados=filtrados[(filtrados["pib_per_capita"]<= pib_max)] #nos quedamos con los países que tengan el PIB máximo

filtrados= filtrados[(filtrados["esperanza_vida"]>= esperanza_min)] #nos quedamos con los países que tengan la esperanza de vida mínima
filtrados= filtrados[(filtrados["esperanza_vida"]<= esperanza_max)] #nos quedamos con los países que tengan la esperanza de vida máxima

filtrados= filtrados[(filtrados["corrupcion"]>= corrupcion_min)] #nos quedamos con los países que tengan la corrupción mínima
filtrados= filtrados[(filtrados["corrupcion"]<= corrupcion_max)] #nos quedamos con los países que tengan la corrupción máxima


# Paso 5. Si no queda nada
# 5.1 Si filtrados está vacía, saca un aviso con st.warning y para el programa con st.stop().

if len(filtrados)==0: # si no hay ningún país que cumpla los filtros
    st.warning("No hay ningún país que cumpla los filtros seleccionados.")  #aviso
    st.stop() #y paramos la ejecución para que no de error al calcular las métricas

# Paso 6. Las métricas
# 6.1 Tres métricas en columnas, con los números más importantes para tu pregunta.
col1, col2, col3, col4= st.columns(4)  # cuatro columnas para las métricas

total_paises = filtrados["pais"].nunique() # Contamos cuántos países únicos hay en total en el dataset filtrados
with col1:
    st.metric("Total países", total_paises) #total de países filtrados
    
with col2:
    st.metric("Nota felicidad más alta:", round(filtrados["puntuacion_felicidad"].max(),2)) #la nota de felicidad más alta


with col3:
    st.metric("PIB per cápita más alto:", round(filtrados["pib_per_capita"].max(),2)) #el PIB per cápita más alto


espana = felicidad[felicidad["pais"] == "Spain"] #Filtramos los datos de España del DataFrame original
with col4:
    st.markdown("### España(Media)")
    st.metric("Felicidad",round(espana["puntuacion_felicidad"].mean(),2)) #calculamos y mostramos la nota de felicidad media de España
    st.metric("PIB",round(espana["pib_per_capita"].mean(),2)) # Calculamos y mostramos el PIB medio de españa 


# Paso 7. Las pestañas
tab1, tab2, tab3, tab4= st.tabs(["Países", "Factores clave", "Mapa", "Evolución país"]) #cuatro pestañas
# 7.1 Al menos dos pestañas: una con la tabla filtrada y otra con dos gráficos.
with tab1: #pestaña 1
    st.header("Los países filtrados") #titulo pestaña
    st.dataframe(filtrados) #la tabla de los países filtrados

    



with tab2:
    st.header("Análisis de Factores Clave & Felicidad")
    st.markdown("Explora cómo se relacionan los factores socioeconómicos con la puntuación de felicidad según tus filtros actuales.")

    
    gcol1, gcol2, gcol3 = st.columns(3) # Creamos 3 columnas en la pestaña para poner los 3 gráficos uno al lado del otro

    with gcol1:
        st.subheader("PIB per cápita")
        fig_pib = px.scatter(filtrados, x="pib_per_capita", y="puntuacion_felicidad",hover_name="pais",labels={"pib_per_capita": "PIB per cápita", "puntuacion_felicidad": "Felicidad"})
        st.plotly_chart(fig_pib, use_container_width=True)

    with gcol2:
        st.subheader("Esperanza de Vida")
        fig_esp = px.scatter(filtrados, x="esperanza_vida", y="puntuacion_felicidad",hover_name="pais",labels={"esperanza_vida": "Esperanza de vida", "puntuacion_felicidad": "Felicidad"})
        st.plotly_chart(fig_esp, use_container_width=True)

    with gcol3:
        st.subheader("Corrupción")
        fig_corr = px.scatter(filtrados, x="corrupcion", y="puntuacion_felicidad",hover_name="pais",labels={"corrupcion": "Percepción de corrupción", "puntuacion_felicidad": "Felicidad"})
        st.plotly_chart(fig_corr, use_container_width=True)

# 7.2 Si tus datos tienen latitud y longitud, otra pestaña con el mapa.

with tab3:
    st.header("🗺️ Mapa Mundial de Felicidad")
    st.markdown("Visualización geográfica de los países seleccionados en tus filtros.")

    #Comprobamos que hay datos en el filtro para que el mapa no falle
    if not filtrados.empty:
        
        #Creamos el mapa interactivo con Plotly Express
        fig_mapa = px.choropleth(
            filtrados,
            locations="pais",          # Columna con el nombre del país
            locationmode="country names", # Le indica a Plotly que use nombres de países estándar
            color="puntuacion_felicidad", # Columna numérica que determina el color del país
            hover_name="pais",         # Nombre que aparece al pasar el ratón
            color_continuous_scale="Inferno", # Escala de colores (puedes cambiarla, ej: "Blues", "RdYlGn", "Plasma")
            labels={"puntuacion_felicidad": "Felicidad"}
        )

        #Ajustamos el diseño para que el mapa ocupe bien la pantalla y sea estético
        fig_mapa.update_layout(
            geo=dict(
                showframe=False,       # Quita el marco exterior del mapa
                showcoastlines=True,   # Muestra las líneas de costa
                projection_type="natural earth" # Proyección mundial realista y limpia
            ),
            margin={"r":0,"t":0,"l":0,"b":0} # Reduce los márgenes vacíos alrededor
        )

        #Lo mostramos en Streamlit abarcando todo el ancho
        st.plotly_chart(fig_mapa, use_container_width=True)
        
    else:
        st.warning("No hay datos disponibles para los filtros seleccionados.")



# Paso 8. Una pregunta para el usuario
# 8.1 Una última pestaña con una pregunta, como "¿Cuánto cobrarías por tu piso?" o "¿Te habrías salvado?":
#     el usuario elige algo y la app le contesta con lo que dicen los datos.

with tab4:
    st.header("📈 Evolución Histórica Comparativa")
    st.markdown("Selecciona hasta dos países para comparar su evolución temporal de forma independiente de los filtros globales.")

    
    lista_paises = sorted(felicidad["pais"].unique()) #Obtenemos la lista limpia de todos los países disponibles del dataset 'felicidad'

    dcol1, dcol2 = st.columns(2) #Creamos dos columnas para poner los desplegables de selección lado a lado

    with dcol1:
        default_p1 = lista_paises.index("Spain") if "Spain" in lista_paises else 0 #pongo este if con el else a 0 por seguridad
        pais_1 = st.selectbox("Selecciona el primer país:", lista_paises, index=default_p1, key="evol_pais_1")

    with dcol2:
        default_p2 = lista_paises.index("Portugal") if "Portugal" in lista_paises else 1 #pongo este if con el else a 1 por seguridad
        pais_2 = st.selectbox("Selecciona el segundo país:", lista_paises, index=default_p2, key="evol_pais_2")

    
    df_comparativa = felicidad[felicidad["pais"].isin([pais_1, pais_2])] #Filtramos el DataFrame 'felicidad' exclusivamente para los dos países seleccionados

    #Comprobamos que hay datos para pintar
    if not df_comparativa.empty: #si no está vacía
        
        st.markdown("---")
        
        # Fila 1: Felicidad y PIB
        r1_col1, r1_col2 = st.columns(2)
        
        with r1_col1:
            st.subheader("Evolución de la Felicidad")
            fig_evo_fel = px.line(df_comparativa,x="año",y="puntuacion_felicidad",color="pais",markers=True,labels={"año": "Año", "puntuacion_felicidad": "Felicidad", "pais": "País"},color_discrete_sequence=["#f3041c", "#8fee14"])
            st.plotly_chart(fig_evo_fel, use_container_width=True)

        with r1_col2:
            st.subheader("Evolución del PIB")
            fig_evo_pib = px.line(df_comparativa,x="año",y="pib_per_capita",color="pais",markers=True,labels={"año": "Año", "pib_per_capita": "PIB per cápita", "pais": "País"},color_discrete_sequence=["#f3041c", "#8fee14"])
            st.plotly_chart(fig_evo_pib, use_container_width=True)

        r2_col1, r2_col2 = st.columns(2)#Fila 2: Esperanza de Vida y Corrupción

        with r2_col1:
            st.subheader("Evolución de la Esperanza de Vida")
            fig_evo_esp = px.line(df_comparativa,x="año",y="esperanza_vida",color="pais",markers=True,labels={"año": "Año", "esperanza_vida": "Esperanza de vida", "pais": "País"},color_discrete_sequence=["#f3041c", "#8fee14"])
            st.plotly_chart(fig_evo_esp, use_container_width=True)

        with r2_col2:
            st.subheader("Evolución de la Corrupción")
            fig_evo_corr = px.line(df_comparativa,x="año",y="corrupcion",color="pais",markers=True,labels={"año": "Año", "corrupcion": "Percepción de corrupción", "pais": "País"},color_discrete_sequence=["#f3041c", "#8fee14"])
            st.plotly_chart(fig_evo_corr, use_container_width=True)

    else:
        st.warning("Selecciona al menos un país válido para ver la comparativa.") #si la lista  del if no t está vacá salta a esta alarma
