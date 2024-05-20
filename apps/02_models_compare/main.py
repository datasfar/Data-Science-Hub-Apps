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
st.sidebar.title("Comparador de modelos")
st.sidebar.write("Predice el tipo de lirio usando diferentes modelos de scikit-learn a partir de los parámetros recibidos.")
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
tab0, tab1, tab2, tab3, tab4 = st.tabs(["Inicio", "Random Forest Classifier", "Support Vector Classifier", "Logistic Regression", "Garussian NB"])

with tab0:

    st.subheader("Comparador de modelos")
    st.write("Esta aplicación con fines didacticos implementa 4 modelos de machine learning a un mismo dataset y genera predicciones en base a unos parametros introducidos por el usuario.")
    st.write("Se utilizan los modelos: Random Forest Classifier, Support Vector Classifier, Logistic Regression y Garussian NB, de la libreria sklearn. Los modelos se implementan sobre el Iris dataset de la misma libreria.")
    st.write("La aplicación describe el funcionamiento del modelo, junto con un resumen de las ventajas y limitaciones de su uso, además de un ejemplo de uso con el código básico para su implementación.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Random Forest Classifier")
        model_rfc = RFC_Model(x, y, df)
        st.metric("Precisión",model_rfc.accuracy)
        model_rfc.model_graphics(lirio)
        
    with col2:
        st.subheader("Support Vector Classifier")
        model_svc = SVC_Model(x, y, df)
        st.metric("Precisión",model_svc.accuracy)
        model_svc.model_graphics(lirio)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Logistic Regresion")
        model_lr = LR_Model(x, y, df)
        st.metric("Precisión",model_lr.accuracy)
        model_lr.model_graphics(lirio)

    with col4:
        st.subheader("Garussian Naive Bayes")
        model_gnb = GNB_Model(x, y, df)
        st.metric("Precisión",model_gnb.accuracy)
        model_gnb.model_graphics(lirio)


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
    model_gnb.model_graphics(lirio)