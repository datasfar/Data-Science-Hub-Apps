# Importamos las librerias
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Titulo y subtitulo de la aplicacion
st.write("""

    # App de prediccion de tipos de lirios

    Predice el tipo de lirio usando scikit learn a partir de los parametros recibidos.
         
""")

# Titulo del sidebar
st.sidebar.header('Parametros sobre la flor')

# Definimos los parametros y creamos deslizadores para insertarlos
def parametros_flor():

    sepal_length = st.sidebar.slider('Longitud de sepalo', 4.0, 8.0, 6.0)
    sepal_width = st.sidebar.slider('Ancho de sepalo', 2.0, 5.0, 3.5)
    petal_length = st.sidebar.slider('Longitud de petalo', 1.0, 7.0, 3.0)
    petal_width = st.sidebar.slider('Ancho de petalo', 0.1, 3.0, 1.0)

    datos = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    # Creamos un data frame con los parametros insertados
    parametros = pd.DataFrame(datos, index=[0])

    # Devolvemos el dataframe parametros insertados
    return parametros

# Recogemos los parametros devueltos por la funcion
df = parametros_flor()

# Imprimimos una sub-cabecera y los parametros introducidos por el usuario
st.subheader('Parametros insertados por el usuario:')
st.write(df)

# Cargamos el modelo de datos y dividimos los datos deseados
lirio = datasets.load_iris()
x = lirio.data
y = lirio.target

# Creamos el modelo de machine learling y le insertamos los datos cargados
clf = RandomForestClassifier()
clf.fit(x, y)

# Utilizamos el modelo entrenado para predecir el tipo basandonos en los datos del usuario
# Almacenamos los datos arrojados por el modelo
prediccion = clf.predict(df)
prediccion_probabilistica = clf.predict_proba(df)

# Mostramos los resultados en la interface con una sub-cabecera identificativa
st.subheader('Tipo de lirio e indice:')
st.write(lirio.target_names)

st.subheader('Prediccion de tipo:')
st.write(lirio.target_names[prediccion])

st.subheader('Prediccion probabilistica:')
st.write(prediccion_probabilistica)



# Doc scikit-learn ==> https://scikit-learn.org/stable/user_guide.html
# Doc modelo ==> https://scikit-learn.org/stable/datasets/toy_dataset.html

# Docs streamlit ==> https://docs.streamlit.io/library/get-started
# Iniciar proyecto = python -m streamlit run prediccion_lirio.py
