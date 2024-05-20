# Importamos las librerías
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets


from RandomForestClassifier import RFC_Model
from SupportVectorClassifier import SVC_Model
from LogisticRegression import LR_Model
from GarussianNB import GNB_Model

# Título y subtítulo de la aplicación
st.sidebar.title("App de predicción de tipos de lirios")
st.sidebar.write("Predice el tipo de lirio usando scikit-learn a partir de los parámetros recibidos.")
st.sidebar.image("./assets/iris.jpeg")

st.sidebar.header('Parámetros sobre la flor')

# Definimos los parámetros y creamos deslizadores para insertarlos
def parametros_flor():
    sepal_length = st.sidebar.slider('Longitud de sépalo', 4.0, 8.0, 6.0)
    sepal_width = st.sidebar.slider('Ancho de sépalo', 2.0, 5.0, 3.5)
    petal_length = st.sidebar.slider('Longitud de pétalo', 1.0, 7.0, 3.0)
    petal_width = st.sidebar.slider('Ancho de pétalo', 0.1, 3.0, 1.0)

    datos = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }

    # Creamos un DataFrame con los parámetros insertados
    parametros = pd.DataFrame(datos, index=[0])

    # Devolvemos el DataFrame con los parámetros insertados
    return parametros

# Recogemos los parámetros devueltos por la función
df = parametros_flor()

# Cargamos el dataset y dividimos los datos deseados
lirio = datasets.load_iris()
x = lirio.data
y = lirio.target


# Creamos las pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Random Forest Classifier", "Support Vector Classifier", "Logistic Regression", "Garussian NB"])

with tab1:

    model_rfc = RFC_Model(x, y, df)
    model_rfc.model_information()
    model_rfc.model_graphics(lirio)

with tab2:

    model_svc = SVC_Model(x, y, df)
    model_svc.model_information()
    model_svc.model_graphics(lirio)

with tab3:

    model_lr = LR_Model(x, y, df)
    model_lr.model_information()
    model_lr.model_graphics(lirio)

with tab4:

    model_gnb = GNB_Model(x, y, df)
    model_gnb.model_information()