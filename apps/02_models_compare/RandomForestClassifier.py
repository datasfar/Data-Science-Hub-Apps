from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import streamlit as st

class RFC_Model():

    def __init__(self, x_train, y_train, df):

        # Creamos el modelo de machine learning y lo entrenamos con los datos cargados
        self.clf = RandomForestClassifier()
        self.clf.fit(x_train, y_train)

        # Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
        self.prediccion = self.clf.predict(df)
        self.prediccion_probabilistica = self.clf.predict_proba(df)

    def model_information(self):
        
        st.subheader('Algoritmo Random Forest Classifier')
        st.markdown(
            """El RandomForestClassifier es un algoritmo de aprendizaje automático utilizado para problemas de clasificación. Pertenece a la familia de modelos de ensamble, que combinan múltiples modelos más simples para mejorar el rendimiento predictivo.

Claves del funcionamiento de Random Forest Classifier (RFC):

1.- Ensamble de árboles de decisión: RandomForestClassifier se basa en la idea de construir múltiples árboles de decisión durante el entrenamiento y combinar sus predicciones para obtener una predicción más robusta y precisa.

2.- Aleatorización: La "aleatorización" es un aspecto crucial de RandomForest. Durante el entrenamiento de cada árbol de decisión, se utilizan subconjuntos aleatorios de las características y muestras del conjunto de datos. Esto ayuda a evitar el sobreajuste y a mejorar la generalización del modelo.

3.- Votación: Durante la predicción, cada árbol en el bosque emite una predicción y la clase más frecuente se elige como la predicción final del RandomForestClassifier. En problemas de clasificación binaria, se utiliza la mayoría de votos; en problemas de clasificación multiclase, se utiliza la clase con mayor cantidad de votos.

4.- Robustez y generalización: RandomForestClassifier tiende a ser robusto frente a datos ruidosos y funciona bien en una variedad de conjuntos de datos. También es menos propenso al sobreajuste en comparación con un solo árbol de decisión.

5.- Importancia de características: RandomForestClassifier puede proporcionar información sobre la importancia relativa de cada característica en la predicción. Esto puede ser útil para el análisis de características y la selección de características."""
        )
    
        st.subheader('Aplicación en código')
        st.code("""
# Importamos las librerias
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
        """)

        st.code("""
# Cargamos el dataset y dividimos los datos deseados
lirio = datasets.load_iris()
x = lirio.data
y = lirio.target
        """)

        st.code("""
# Creamos el modelo de machine learning y lo entrenamos con los datos cargados
clf = RandomForestClassifier()
clf.fit(x_train, y_train)
        """)
        
        st.code("""
# Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
prediccion = clf.predict(df)
prediccion_probabilistica = clf.predict_proba(df)
        """)
        

    def model_graphics(self, lirio):
            
        st.subheader('Predicción con RandomForestClassifier')

        # Mostrar la predicción
        st.write(f"Predicción: {lirio.target_names[self.prediccion][0]}")
        st.write(f"Probabilidades: {self.prediccion_probabilistica}")

        # Gráfico de la predicción probabilística
        fig, ax = plt.subplots()
        ax.bar(lirio.target_names, self.prediccion_probabilistica[0], color=['blue', 'green', 'red'])
        ax.set_ylabel('Probabilidad')
        ax.set_title('Probabilidad de cada tipo de lirio')
        st.pyplot(fig)