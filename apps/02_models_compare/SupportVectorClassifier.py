import streamlit as st
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.svm import SVC

class SVC_Model():

    def __init__(self, x_train, y_train, df):

        # Creamos el modelo de machine learning y lo entrenamos con los datos cargados
        self.clf_svc = SVC(probability=True)
        self.clf_svc.fit(x_train, y_train)

        # Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
        self.prediccion_svc = self.clf_svc.predict(df)
        self.prediccion_probabilistica_svc = self.clf_svc.predict_proba(df)

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
    # Utilizamos el modelo entrenado para predecir el tipo basándonos en los datos del usuario
    prediccion_svc = clf_svc.predict(df)
    prediccion_probabilistica_svc = clf_svc.predict_proba(df)
        """)
        
    def model_graphics(self, lirio):

        st.subheader('Predicción con SupportVectorClassifier')

        # Mostrar la predicción
        st.write(f"Predicción: {lirio.target_names[self.prediccion_svc][0]}")
        st.write(f"Probabilidades: {self.prediccion_probabilistica_svc}")

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