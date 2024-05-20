from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import streamlit as st
from sklearn.metrics import accuracy_score

class RFC_Model():

    def __init__(self, x, y, df):

        # Separamos los datos para entreno y test
        self.x_train, self.x_test, self.y_train,self.y_test = train_test_split(x, y, test_size=0.3, random_state=42)

        # Creamos el modelo de machine learning y lo entrenamos con los datos cargados
        self.clf = RandomForestClassifier()
        self.clf.fit(x, y)

        # Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
        self.prediccion = self.clf.predict(df)
        self.prediccion_probabilistica = self.clf.predict_proba(df)

        # Metricas adicionales
        self.accuracy = accuracy_score(self.y_test, self.clf.predict(self.x_test))

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

        st.subheader("Ventajas:")
        st.markdown("""
- Reducción del Sobreajuste: Al promediar múltiples árboles de decisión, el RandomForestClassifier tiende a reducir el riesgo de sobreajuste en comparación con un solo árbol de decisión.
- Precisión Alta: Generalmente proporciona una precisión alta en tareas de clasificación debido a su capacidad para capturar relaciones no lineales en los datos.
- Datos Grandes y de Alta Dimensionalidad: Puede manejar grandes conjuntos de datos y muchas características sin requerir una selección exhaustiva de características.
- Manejo de Datos Faltantes: Puede manejar datos faltantes de manera más efectiva que otros algoritmos, debido a la imputation inherente en los árboles.
- Evaluación de Características: Proporciona una estimación de la importancia de cada característica en la predicción, lo que puede ser útil para el análisis y la selección de características.
        """)

        st.subheader("Limitaciones:")
        st.markdown("""
- Consumo de Memoria: Puede ser intensivo en términos de memoria, especialmente con conjuntos de datos grandes y un gran número de árboles.
- Tiempo de Entrenamiento: Entrenar un gran número de árboles puede ser computacionalmente costoso y lento en comparación con modelos más simples.
- Dificultad para Interpretar: Aunque es más interpretable que algunos modelos de caja negra como los métodos de ensamble basados en redes neuronales, sigue siendo menos interpretable que un solo árbol de decisión o modelos lineales.
- Escalabilidad Limitada: A pesar de la paralelización, puede enfrentar problemas de escalabilidad en conjuntos de datos extremadamente grandes, donde otros métodos más ligeros pueden ser preferibles.
        """)

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
# Generamos los datos a predecir
df = {
        'sepal_length': 6.4,
        'sepal_width': 3.5,
        'petal_length': 6.4,
        'petal_width': 3.2
    }
# Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
prediccion = clf.predict(df)
prediccion_probabilistica = clf.predict_proba(df)
        """)
        
        st.subheader('Predicción con RandomForestClassifier')

    def model_graphics(self, lirio):


        # Mostrar la predicción
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Setosa:", f"{round(self.prediccion_probabilistica[0,0], 5)}")
        with col2:
            st.metric("Vesicolor:", f"{round(self.prediccion_probabilistica[0,1], 5)}")
        with col3:
            st.metric("Virginica:", f"{round(self.prediccion_probabilistica[0,2], 5)}")

        # Gráfico de la predicción probabilística
        fig, ax = plt.subplots()
        ax.bar(lirio.target_names, self.prediccion_probabilistica[0], color=['blue', 'green', 'red'])
        ax.set_ylabel('Probabilidad')
        ax.set_title('Probabilidad de cada tipo de lirio')
        st.pyplot(fig)