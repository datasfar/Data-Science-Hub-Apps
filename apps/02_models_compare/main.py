# Importamos las librerías
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from mlxtend.plotting import plot_decision_regions

# Título y subtítulo de la aplicación
st.title("App de predicción de tipos de lirios")
st.write("Predice el tipo de lirio usando scikit-learn a partir de los parámetros recibidos.")

# Título del sidebar
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

# Aplicamos PCA para reducir las dimensiones a 2 componentes
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x)

# Transformamos los datos de entrada del usuario usando el mismo PCA
df_pca = pca.transform(df)

# Creamos las pestañas
tab1, tab2, tab3, tab4 = st.tabs(["RandomForestClassifier", "SVC", "Tab3", "Tab4"])

with tab1:
    st.subheader('Predicción con RandomForestClassifier')

    # Creamos el modelo de machine learning y lo entrenamos con los datos cargados
    clf = RandomForestClassifier()
    clf.fit(x, y)

    # Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
    prediccion = clf.predict(df)
    prediccion_probabilistica = clf.predict_proba(df)

    # Mostrar la predicción
    st.write(f"Predicción: {lirio.target_names[prediccion][0]}")
    st.write(f"Probabilidades: {prediccion_probabilistica}")

    # Gráfico de la predicción probabilística
    fig, ax = plt.subplots()
    ax.bar(lirio.target_names, prediccion_probabilistica[0], color=['blue', 'green', 'red'])
    ax.set_ylabel('Probabilidad')
    ax.set_title('Probabilidad de cada tipo de lirio')
    st.pyplot(fig)

with tab2:
    st.subheader('Frontera de decisión - Support Vector Classifier (SVC)')
    
    # Creamos el modelo de machine learning y lo entrenamos con los datos cargados
    clf_svc = SVC(probability=True)
    clf_svc.fit(x_pca, y)

    # Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
    prediccion_svc = clf_svc.predict(df_pca)
    prediccion_probabilistica_svc = clf_svc.predict_proba(df_pca)

    # Mostrar la predicción
    st.write(f"Predicción: {lirio.target_names[prediccion_svc][0]}")
    st.write(f"Probabilidades: {prediccion_probabilistica_svc}")

    # Graficamos la frontera de decisión
    plt.figure(figsize=(10, 6))
    plot_decision_regions(x_pca, y, clf_svc)
    plt.xlabel('Componente Principal 1')
    plt.ylabel('Componente Principal 2')
    plt.title('Frontera de decisión - Support Vector Classifier (SVC)')
    st.pyplot(plt)
