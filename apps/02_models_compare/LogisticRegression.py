from sklearn.linear_model import LogisticRegression
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class LR_Model():

    def __init__(self, x, y, df):

        # Separamos los datos para entreno y test
        self.x_train, self.x_test, self.y_train,self.y_test = train_test_split(x, y, test_size=0.3, random_state=42)

        # Crea una instancia del modelo de regresión logística
        self.model_lr = LogisticRegression(max_iter=1000)

        # Entrena el modelo de regresión logística
        self.model_lr.fit(x, y)

        # Realiza la predicción con los datos de entrada del usuario
        self.prediction_lr = self.model_lr.predict(df)
        self.prediction_proba_lr = self.model_lr.predict_proba(df)

        # Metricas adicionales
        self.accuracy = accuracy_score(self.y_test, self.model_lr.predict(self.x_test))

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
        """)
        st.subheader("One vs Rest (OVR)")
        st.markdown("""
"One-vs-Rest" (también conocido como "One-vs-All"), es una estrategia comúnmente utilizada en problemas de clasificación multiclase con algoritmos de clasificación binaria, como la regresión logística. 

Por ejemplo, supongamos que tienes un problema de clasificación con tres clases: A, B y C. Para aplicar OVR, entrenarías tres clasificadores binarios:
                        
- Clasificador A-vs-Rest: Predice si una muestra es de la clase A o no.
- Clasificador B-vs-Rest: Predice si una muestra es de la clase B o no.
- Clasificador C-vs-Rest: Predice si una muestra es de la clase C o no.
        """)

        st.subheader("Ventajas:")
        st.markdown("""
- Interpretación Sencilla: Los coeficientes de regresión pueden interpretarse directamente como el cambio en la probabilidad logarítmica de la variable dependiente para un cambio unitario en la variable independiente.
- Eficiencia Computacional: El tiempo de entrenamiento es rápido, especialmente para conjuntos de datos de tamaño moderado a grande.
- Manejo de Variables Categóricas y Continuas: Puede manejar tanto variables categóricas como continuas sin necesidad de preprocesamiento adicional.
- Regularización: Permite la incorporación de términos de regularización para evitar el sobreajuste, lo que lo hace útil en conjuntos de datos con características redundantes o altamente correlacionadas.
- Probabilidades de Clase: Puede predecir probabilidades de clase directamente, lo que facilita la interpretación y el ajuste de umbrales de clasificación.
- Escalabilidad: Se puede escalonar fácilmente para problemas de clasificación multiclase utilizando estrategias como One-vs-Rest (OVR) o One-vs-One (OVO).
        """)

        st.subheader("Limitaciones:")
        st.markdown("""
- Linealidad: La regresión logística asume una relación lineal entre las variables independientes y el logaritmo de la razón de probabilidades. Esto puede ser una limitación en problemas con relaciones no lineales.
- Sensibilidad a Valores Atípicos: Los valores atípicos pueden tener un impacto significativo en los coeficientes de regresión y, por lo tanto, en las predicciones, especialmente en conjuntos de datos pequeños.
- Suposiciones de Independencia: La regresión logística asume independencia entre las observaciones. Si hay dependencia entre las muestras, esto puede llevar a estimaciones sesgadas.
- Limitado a Problemas de Clasificación Binaria: Aunque se puede extender a problemas de clasificación multiclase, su rendimiento puede ser superado por otros algoritmos en situaciones donde la separabilidad de las clases es difícil.
- Requiere Limpieza de Datos: Como otros algoritmos de aprendizaje automático, la regresión logística requiere datos limpios y bien estructurados para obtener buenos resultados.
- Necesidad de Selección de Características: Para obtener un buen rendimiento, es importante seleccionar cuidadosamente las características relevantes y eliminar las irrelevantes o redundantes.
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
# Generamos los datos a predecir
df = {
        'sepal_length': 6.4,
        'sepal_width': 3.5,
        'petal_length': 6.4,
        'petal_width': 3.2
    }
                
# Realiza la predicción con los datos de entrada del usuario
prediction_lr = model_lr.predict(df)
prediction_proba_lr = model_lr.predict_proba(df)
        """)
        st.subheader('Predicción con LogisticRegression')
    
    def model_graphics(self, lirio):
        
        # Mostrar la predicción
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Setosa:", f"{round(self.prediction_proba_lr[0,0], 5)}")
        with col2:
            st.metric("Vesicolor:", f"{round(self.prediction_proba_lr[0,1], 5)}")
        with col3:
            st.metric("Virginica:", f"{round(self.prediction_proba_lr[0,2], 5)}")

        # Gráfico de la predicción probabilística
        fig, ax = plt.subplots()
        ax.bar(lirio.target_names, self.prediction_proba_lr[0], color=['blue', 'green', 'red'])
        ax.set_ylabel('Probabilidad')
        ax.set_title('Probabilidad de cada tipo de lirio')
        st.pyplot(fig)