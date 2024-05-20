from sklearn.linear_model import LogisticRegression
import streamlit as st
import matplotlib.pyplot as plt

class LR_Model():

    def __init__(self, x_train, y_train, df):

        # Crea una instancia del modelo de regresión logística
        self.model_lr = LogisticRegression(max_iter=1000)

        # Entrena el modelo de regresión logística
        self.model_lr.fit(x_train, y_train)

        # Realiza la predicción con los datos de entrada del usuario
        self.prediction_lr = self.model_lr.predict(df)
        self.prediction_proba_lr = self.model_lr.predict_proba(df)

    def model_information(self):
        
        st.subheader('Algoritmo Logistic Regression')
        st.markdown("""
La regresión logística es un algoritmo de aprendizaje supervisado utilizado para problemas de clasificación binaria. Aunque el nombre contiene "regresión", la regresión logística se utiliza para la clasificación, no para la regresión. Es uno de los algoritmos de clasificación más simples y ampliamente utilizados en el aprendizaje automático.

Claves del funcionamiento de Logistic Regression (LR):

1.- Función de hipótesis: En la regresión logística, se utiliza una función de hipótesis logística para modelar la probabilidad de que una instancia pertenezca a una clase particular. La función logística también es conocida como función sigmoide.

2.- Clasificación binaria: La regresión logística se utiliza principalmente para problemas de clasificación binaria, donde hay dos clases etiquetadas, como "positiva" y "negativa", "sí" y "no", etc.

3.- Entrenamiento: Durante el entrenamiento, el objetivo es ajustar los parámetros del modelo para que la función de hipótesis prediga correctamente las etiquetas de clase de los datos de entrenamiento. Esto se realiza mediante técnicas de optimización como el descenso de gradiente.

4.- Función de coste: Para entrenar el modelo, se utiliza una función de coste que mide la discrepancia entre las predicciones del modelo y las etiquetas reales. Una función de coste comúnmente utilizada en la regresión logística es la entropía cruzada (o pérdida logarítmica).

5.- Decision Boundary: En la regresión logística, el límite de decisión es la frontera que separa las clases en el espacio de características. Esta frontera se define por la probabilidad de que una instancia pertenezca a una clase u otra, y suele ser una línea (en el caso de clasificación binaria) o un hiperplano (en el caso de clasificación multiclase).

6.- Regularización: Al igual que otros modelos de aprendizaje automático, la regresión logística puede estar sujeta a sobreajuste. Se puede aplicar regularización para controlar la complejidad del modelo y evitar el sobreajuste.
[INFO OVR One vs Rest]
        """)
    
        st.subheader('Aplicación en código')
        st.code("""
# Importamos las librerias
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
        """)

        st.code("""
# Cargamos el dataset y dividimos los datos deseados
lirio = datasets.load_iris()
x = lirio.data
y = lirio.target
        """)

        st.code("""
# Crea una instancia del modelo de regresión logística
model_lr = LogisticRegression(max_iter=1000)

# Entrena el modelo de regresión logística
model_lr.fit(x, y)
        """)
        
        st.code("""
# Realiza la predicción con los datos de entrada del usuario
prediction_lr = model_lr.predict(df)
prediction_proba_lr = model_lr.predict_proba(df)
        """)

    def model_graphics(self, lirio):
            
        st.subheader('Predicción con LogisticRegression')

        # Mostrar la predicción
        st.write(f"Predicción: {lirio.target_names[self.prediction_lr][0]}")
        st.write(f"Probabilidades: {self.prediction_proba_lr}")

        # Gráfico de la predicción probabilística
        fig, ax = plt.subplots()
        ax.bar(lirio.target_names, self.prediction_proba_lr[0], color=['blue', 'green', 'red'])
        ax.set_ylabel('Probabilidad')
        ax.set_title('Probabilidad de cada tipo de lirio')
        st.pyplot(fig)