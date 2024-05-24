import reflex as rx

from rxconfig import config
import library_hub.styles.styles as styles

class State(rx.State):
    """The app state."""

    ...

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLES,
)


def index() -> rx.Component:
    return rx.container(
        rx.hstack( 
            rx.vstack(
                rx.vstack(
                    rx.image(
                        src="/aaa.png",
                        width="50%",
                    ),
                    rx.heading(
                        "DS APPS",
                        font_size="2em",
                        background = "linear-gradient(#8800FF, #CF00FF)",
                        background_clip= "text",
                        text_fill_color= "transparent" 
                    ),
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    gap="0",
                    padding="1em",
                    width="100%",
                    height="100%",
                    background_color="#13111C",
                    border_radius="12px"
                ),
                background="linear-gradient(to left, #8800FF, #CF00FF)",
                padding="3px",
                class_name="animate__animated animate__fadeInLeft",
                width="40%",
                height="320px",
                border_radius="15px",
                box_shadow="rgba(132, 59, 206, 0.35) 0px 4px 24px"
            ),
            rx.box(
                rx.vstack(
                    rx.heading(
                        "1 Problema, 4 Algoritmos", 
                        font_size="1.6em",
                        background = "linear-gradient(#8800FF, #CF00FF)",
                        background_clip= "text",
                        text_fill_color= "transparent" 
                    ),
                    rx.text(
                    "Sistema de predicción de tipos de lirio. Basado en 'Iris Dataset' de sklearn. Se aplican 4 algoritmos de machine learning y explica su implementación y funcionamiento.",
                    color="#ccccdd",
                    font_weight="400",
                    z_index= "2",
                    ),
                    rx.list.unordered(
                        rx.list.item("Logistic Regresion"),
                        rx.list.item("Random Forest Classifier"),
                        rx.list.item("Garussian Naives Bayes"),
                        rx.list.item("Support Vector Classifier"),
                        color="#ccccdd",
                    ),
                    rx.image(
                        src="/image1.png",
                        width="50%",
                        position="absolute",
                        left= "315px",
                        top= "77px",
                        z_index= "1",
                    ),
                    rx.hstack(
                        rx.button(
                            rx.icon(
                                "github",
                                padding="3px",
                                border_radius="2px",
                                background_color="rgba(255,255,255,.35)"
                            ),
                            "Repositorio",
                            font_size="1em",
                            background="linear-gradient(to right, #8800FF, #CF00FF)",
                            padding="1.1em",
                            color="white",
                            box_sizing="border-box",
                            _hover={
                                "background_image":"linear-gradient(76.35deg,#660ac2 15.89%,#850ac2 89.75%)",
                                "border":"1px solid #e286f9"
                            }
                        ),
                        rx.button(
                            "Live Demo",
                            rx.icon(
                                "move-up-right",
                            ),
                            font_size="1em",
                            background_color="#13111C",
                            padding="1.1em",
                            color="#7709C2",
                            box_sizing="border-box",
                            _hover={
                                "color":"#CD00FE",
                            }
                        ),
                    ),
                    position="relative",
                    top="0",
                    right="0",
                    padding="1em",
                    width="100%",
                    height="100%",
                    background_color="#13111C",
                    border_radius="12px",
                    overflow="hidden"
                ),
                background="linear-gradient(to right, #8800FF, #CF00FF)",
                padding="3px",
                class_name="animate__animated animate__fadeInRight",
                width="60%",
                height="320px",
                border_radius="15px",
                box_shadow="rgba(132, 59, 206, 0.35) 0px 4px 24px"
            ),
            margin_top="100px",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        background_color="#13111C"
    )



app.add_page(index)