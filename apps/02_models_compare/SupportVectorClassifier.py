import streamlit as st
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class SVC_Model():

    def __init__(self, x, y, df):

        # Separamos los datos para entreno y test
        self.x_train, self.x_test, self.y_train,self.y_test = train_test_split(x, y, test_size=0.3, random_state=42)

        # Creamos el modelo de machine learning y lo entrenamos con los datos cargados
        self.clf_svc = SVC(probability=True)
        self.clf_svc.fit(x, y)

        # Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
        self.prediccion_svc = self.clf_svc.predict(df)
        self.prediccion_probabilistica_svc = self.clf_svc.predict_proba(df)

        # Metricas adicionales
        self.accuracy = accuracy_score(self.y_test, self.clf_svc.predict(self.x_test))

    def model_information(self):
        
        st.subheader('Algoritmo Support Vector Classifier')
        st.markdown("""
El Support Vector Classifier (SVC) es un algoritmo de aprendizaje automático, especialmente eficaz para problemas de clasificación. Está basado en el concepto de máquinas de vectores de soporte (SVM), que es una técnica de aprendizaje supervisado.

Claves del funcionamiento de Support Vector Classifier (SVC):

1.- Separación óptima: El objetivo principal del SVC es encontrar el hiperplano que mejor separa las clases en el espacio de características. Este hiperplano se define de manera que maximice la distancia entre los puntos de datos más cercanos de las clases diferentes, lo que se conoce como el margen.

2.- Margen y vectores de soporte: Los vectores de soporte son los puntos de datos más cercanos al hiperplano de separación y determinan la posición y la orientación del hiperplano. El margen es la distancia entre el hiperplano y los vectores de soporte.

3.- Kernel trick: El SVC puede manejar datos no linealmente separables utilizando el truco del kernel. Esto implica mapear los datos a un espacio dimensionalmente superior donde sean linealmente separables y luego encontrar el hiperplano óptimo en ese espacio. Los kernels comunes incluyen el lineal, el polinomial y el radial (o gaussiano).

4.- Regularización: Al igual que otros modelos de aprendizaje automático, el SVC puede estar sujeto a sobreajuste. La regularización se utiliza para controlar la complejidad del modelo y evitar el sobreajuste. Esto se logra a través del parámetro de regularización, comúnmente conocido como "C" en la implementación de SVC en la biblioteca scikit-learn.

5.- Eficiencia: Aunque SVC puede ser muy eficaz en muchos problemas de clasificación, su rendimiento puede verse afectado negativamente por grandes conjuntos de datos, ya que su complejidad computacional aumenta con el tamaño del conjunto de datos.
""")
        st.subheader("Ventajas:")
        st.markdown("""
- Manejo de Datos de Alta Dimensionalidad: SVC es muy eficaz en espacios de alta dimensionalidad y sigue siendo efectivo cuando el número de dimensiones es mayor que el número de muestras.
- Kernel Trick: Utiliza el kernel trick para manejar la clasificación no lineal. Puede utilizar diferentes funciones kernel como lineal, polinómico, radial (RBF), entre otros, para transformar los datos en un espacio de mayor dimensión donde sean separables linealmente.
- Separación Óptima: Encuentra el hiperplano que maximiza el margen entre las clases, lo que suele llevar a una mejor generalización en nuevos datos no vistos.
- Regularización: El parámetro de regularización (C) ayuda a evitar el sobreajuste, permitiendo un control sobre la suavidad del margen de decisión.
- Eficiencia Computacional: SVC puede ser muy eficiente y efectivo en conjuntos de datos de tamaño pequeño a mediano.  
    """)
        
        st.subheader("Limitaciones:")
        st.markdown("""
- Costoso Computacionalmente: El entrenamiento de SVC puede ser lento y consumir mucha memoria, especialmente con grandes conjuntos de datos, debido a la necesidad de calcular y almacenar la matriz de kernel.
- No Escalable a Datos Masivos: No se escala bien a conjuntos de datos muy grandes (por ejemplo, decenas de miles de muestras o más), donde otros algoritmos pueden ser más adecuados.
- Necesidad de Ajuste de Parámetros: La elección del kernel y la optimización de hiperparámetros como C y los parámetros del kernel (por ejemplo, gamma para RBF) requieren tiempo y experiencia, generalmente mediante validación cruzada.
- Sensibilidad a la Selección de Kernel: El rendimiento de SVC puede ser muy sensible a la elección del kernel. Un kernel inadecuado puede resultar en un rendimiento deficiente.
- Menos Interpretable: Los modelos SVM no son tan interpretables como otros modelos más simples, como los árboles de decisión. Aunque pueden proporcionar información sobre los vectores de soporte, la interpretación de las decisiones del modelo puede ser complicada.
- Impacto de Valores Atípicos: Los SVM pueden ser sensibles a los valores atípicos, ya que estos pueden afectar significativamente el hiperplano de separación. La regularización puede ayudar, pero los valores atípicos aún pueden tener un impacto considerable.
        """)

        st.subheader('Aplicación en código')
        st.code("""
    # Importamos las librerias
    from sklearn import datasets
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA
    from mlxtend.plotting import plot_decision_regions
    from sklearn.svm import SVC
        """)

        st.code("""
    # Cargamos el dataset y dividimos los datos deseados
    lirio = datasets.load_iris()
    x = lirio.data
    y = lirio.target
        """)

        st.code("""
    # Creamos el modelo de machine learning y lo entrenamos con los datos cargados
    clf_svc = SVC(probability=True)
    clf_svc.fit(x_train, y_train)
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
    prediccion_svc = clf_svc.predict(df)
    prediccion_probabilistica_svc = clf_svc.predict_proba(df)
        """)

        st.subheader('Predicción con SupportVectorClassifier')
        
    def model_graphics(self, lirio):

        # Mostrar la predicción
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Setosa:", f"{round(self.prediccion_probabilistica_svc[0,0], 5)}")
        with col2:
            st.metric("Vesicolor:", f"{round(self.prediccion_probabilistica_svc[0,1], 5)}")
        with col3:
            st.metric("Virginica:", f"{round(self.prediccion_probabilistica_svc[0,2], 5)}")

        # Gráfico de la predicción probabilística
        fig, ax = plt.subplots()
        ax.bar(lirio.target_names, self.prediccion_probabilistica_svc[0], color=['blue', 'green', 'red'])
        ax.set_ylabel('Probabilidad')
        ax.set_title('Probabilidad de cada tipo de lirio')
        st.pyplot(fig)















""""""

"""with tab2:
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
    plt.xlabel(f'{lirio.feature_names[0]}')
    plt.ylabel(f'{lirio.feature_names[2]}')
    plt.title('Frontera de decisión - Support Vector Classifier (SVC)')
    st.pyplot(plt)"""