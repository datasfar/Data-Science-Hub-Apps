import streamlit as st
import pandas as pd

# Subir dataset y generar dataframe
st.header("Visualizador de datos")
st.write("Visualiza datos a partir de un documento .csv")

# Inicializar variables
dataframe = None
filtered_data = None

with st.sidebar:
    with st.expander("Subir CSV"):
        data_set = st.file_uploader("Sube un documento csv", type="csv")
    
    if data_set is not None:
        dataframe = pd.read_csv(data_set)

        # Dropear columnas
        with st.expander("Dropear Columnas"):
            st.write("Seleccione las columnas a eliminar:")
            columns_to_drop = [column for column in dataframe.columns if st.checkbox(column, key=column)]
            dataframe = dataframe.drop(columns=columns_to_drop, inplace=False)

        # Filtro a columna 
        with st.expander("Aplicar Filtros"):
            selected_column = st.selectbox("Columnas", options=dataframe.columns)
            st.write("Filtrar filas por valor en una columna:")
            selected_value = st.text_input("Valor a filtrar en la columna seleccionada")
            filtered_data = dataframe[dataframe[selected_column].astype(str) == selected_value]

# Mostrar dataframe y datos filtrados en la página principal
st.write("DataFrame completo:")

if dataframe is not None:
    st.write(dataframe)
else: 
    st.warning("Sube el archivo CSV para empezar el análisis.")

st.write("DataFrame filtrado:")

if filtered_data is not None:
    st.write(filtered_data)
else: 
    st.warning("Sube el archivo CSV para empezar el análisis.")

