import reflex as rx

from rxconfig import config
import library_hub.styles.styles as styles

from library_hub.components.logo_card import logo_card
from library_hub.components.big_card import big_card
from library_hub.components.medium_card import medium_card
from library_hub.components.small_card import small_card

from library_hub.components.card_3d import card_3d # 3D Card testing

class State(rx.State):
    """The app state."""

    ...

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES,
)


def index() -> rx.Component:
    return rx.container(

        # 1º ROW
        rx.hstack( 
            logo_card(),
            big_card(
                title="1 Problema, 4 Algoritmos",
                description="Sistema de predicción de tipos de lirio. Basado en 'Iris Dataset' de sklearn. Se aplican 4 algoritmos de machine learning y explica su implementación y funcionamiento.",
                list_elements=["Logistic Regresion","Random Forest Classifier","Garussian Naives Bayes","Support Vector Classifier"],
                image="/image1.png",
                link_repo="https://reflex.dev/docs/library/forms/button/#button",
                link_app="https://reflex.dev/docs/library/forms/button/#button"
            ),
            margin_top="100px",
            margin_bottom="24px",
            spacing="5",
            justify="center",
        ),

        # 2º ROW
        rx.hstack( 
            medium_card(
                title="Clasificador de Perros y Gatos",
                description="Sistema de clasificación de imágenes de perros y gatos en tiempo real.",
                list_elements=["Redes Neuronales Convolucionales", "TensorFlow y Keras"],
                image="/image3.png",
                link_repo="https://reflex.dev/docs/library/forms/button/#button",
                link_app="https://reflex.dev/docs/library/forms/button/#button"
            ),
            medium_card(
                title="Clasificador de Números Manuscritos",
                description="Sistema de clasificación de imágenes de perros y gatos en tiempo real.",
                list_elements=["Redes Neuronales Convolucionales", "TensorFlow y Keras"],
                image="/image3.png",
                link_repo="https://reflex.dev/docs/library/forms/button/#button",
                link_app="https://reflex.dev/docs/library/forms/button/#button"
            ),
            margin_bottom="24px",
            spacing="5",
            justify="center",
        ),

        # 3º ROW
        rx.hstack( 
            big_card(
                title="1 Problema, 4 Algoritmos",
                description="Sistema de predicción de tipos de lirio. Basado en 'Iris Dataset' de sklearn. Se aplican 4 algoritmos de machine learning y explica su implementación y funcionamiento.",
                list_elements=["Logistic Regresion","Random Forest Classifier","Garussian Naives Bayes","Support Vector Classifier"],
                image="/image1.png",
                link_repo="https://reflex.dev/docs/library/forms/button/#button",
                link_app="https://reflex.dev/docs/library/forms/button/#button"
            ),
            small_card(
                title="Web Scraper",
                description="Obtiene información concreta de una página web y lo convierte a csv.",
                image="/image2.png",
                link="https://reflex.dev/docs/library/forms/button/#button"
            ),
            margin_bottom="24px",
            spacing="5",
            justify="center",
        ),

        background_color="#13111C"
    )



app.add_page(index)