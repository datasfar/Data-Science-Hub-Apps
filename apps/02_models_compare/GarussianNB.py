import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

class GNB_Model():

    def __init__(self, x, y, df):

        # Separamos los datos para entreno y test
        self.x_train, self.x_test, self.y_train,self.y_test = train_test_split(x, y, test_size=0.3, random_state=42)

        # Inicializar el clasificador GaussianNB
        self.model_gnb = GaussianNB()

        # Entrenar el modelo
        self.model_gnb.fit(self.x_train, self.y_train)

        # Realiza la predicción con los datos de entrada del usuario
        self.prediction_gnb = self.model_gnb.predict(df)
        self.prediction_proba_gnb = self.model_gnb.predict_proba(df)

        # Metricas adicionales
        self.accuracy = accuracy_score(self.y_test, self.model_gnb.predict(self.x_test))
        self.confusion = confusion_matrix(self.y_test, self.model_gnb.predict(self.x_test))
        self.classification = classification_report(self.y_test, self.model_gnb.predict(self.x_test))

    
    def model_information(self):

        st.subheader('Algoritmo Garussian NB')
        st.markdown("""
GaussianNB es una implementación del algoritmo Naive Bayes, específicamente para datos que siguen una distribución normal (gaussiana). Es uno de los clasificadores más simples y eficientes, especialmente adecuado para problemas de clasificación con datos continuos. 

Claves del funcionamiento de Garussian NB (GNB):

1.- Modelo de Probabilidades: GaussianNB se basa en el teorema de Bayes, que utiliza la probabilidad condicional para hacer predicciones. La fórmula del teorema de Bayes es:

        """)
        st.latex(r"""P(C|X) = \frac{P(X|C) \cdot P(C)}{P(X)}""")
        st.markdown("""
        donde:

    - 𝑃(𝐶∣𝑋)es la probabilidad posterior de la clase 𝐶 dada la observación 𝑋.
    - 𝑃(𝑋∣𝐶)es la probabilidad de observar 𝑋 dado que la clase es 𝐶.
    - 𝑃(𝐶) es la probabilidad previa de la clase 𝐶.
    - 𝑃(𝑋) es la probabilidad previa de observar 𝑋.
        
2.- Asunción de Independencia: Una de las características clave del Naive Bayes es la asunción de independencia condicional, que supone que las características son independientes entre sí dado el valor de la clase. Aunque esta asunción rara vez es cierta en la práctica, el modelo sigue funcionando bien en muchos casos.

3.- Distribución Gaussiana: En GaussianNB, se asume que las características continúas siguen una distribución normal (gaussiana). Esto significa que la probabilidad condicional  𝑃(𝑋𝑖∣𝐶) para una característica 𝑋𝑖 dada la clase 𝐶 se modela como:
        """)
        st.latex(r"""P(X_i|C) = \frac{1}{\sqrt{2\pi\sigma_C^2}} \exp\left(-\frac{(X_i - \mu_C)^2}{2\sigma_C^2}\right)""")
        st.markdown("""
donde 𝜇𝐶 y 𝜎𝐶 son la media y la desviación estándar de la característica 𝑋𝑖 para la clase 𝐶.
        """)
        
        st.subheader("Ventajas:")
        st.markdown("""
- Eficiencia Computacional: GaussianNB es extremadamente rápido en el entrenamiento y la predicción, ya que solo requiere calcular estadísticas simples (media y desviación estándar) para cada característica y clase.
- Pocos Parámetros a Ajustar: No requiere muchos hiperparámetros, lo que simplifica el proceso de entrenamiento y ajuste.
- Rendimiento en Datos Pequeños: Funciona bien incluso con conjuntos de datos pequeños, donde otros algoritmos más complejos podrían sobreajustar.
- Simplicidad: Es fácil de implementar y entender, lo que lo hace adecuado para problemas rápidos y prototipado.
        """)

        st.subheader("Limitaciones:")
        st.markdown("""
- Asunción de Independencia: La suposición de que las características son independientes puede no ser válida en muchos problemas reales, lo que puede afectar negativamente al rendimiento.
- Sensibilidad a la Distribución de Datos: Si los datos no siguen una distribución normal, el rendimiento de GaussianNB puede verse afectado.
        """)
    
        st.subheader('Aplicación en código')
        st.code("""
# Importamos las librerias
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import datasets
        """)

        st.code("""
# Cargamos el dataset y dividimos los datos deseados
lirio = datasets.load_iris()
x = lirio.data
y = lirio.target
        """)

        st.code("""
# Separamos los datos para entreno y test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Inicializar el clasificador GaussianNB
model_gnb = GaussianNB()

# Entrenar el modelo
model_gnb.fit(x_train, y_train)
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
prediction_gnb = model_gnb.predict(df)
prediction_proba_gnb = model_gnb.predict_proba(df)
        """)
        
        st.subheader('Predicción con GarussianNB')

    def model_graphics(self, lirio):

        # Mostrar la predicción
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Setosa:", f"{round(self.prediction_proba_gnb[0,0], 5)}")
        with col2:
            st.metric("Vesicolor:", f"{round(self.prediction_proba_gnb[0,1], 5)}")
        with col3:
            st.metric("Virginica:", f"{round(self.prediction_proba_gnb[0,2], 5)}")


        # Gráfico de la predicción probabilística
        fig, ax = plt.subplots()
        ax.bar(lirio.target_names, self.prediction_proba_gnb[0], color=['blue', 'green', 'red'])
        ax.set_ylabel('Probabilidad')
        ax.set_title('Probabilidad de cada tipo de lirio')
        st.pyplot(fig)




  