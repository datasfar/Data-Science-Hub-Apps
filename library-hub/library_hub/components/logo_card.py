import reflex as rx
import library_hub.styles.styles as styles

def logo_card() -> rx.Component:
    return rx.vstack(
                rx.vstack(
                    rx.image(
                        src="/aaa.png",
                        style=styles.Logo_Card_Styles.IMAGE,
                    ),
                    rx.heading(
                        "DS APPS",
                        style=styles.Logo_Card_Styles.TITLE
                    ),
                    style=styles.Logo_Card_Styles.CHILDREN_BOX
                ),
                class_name="animate__animated animate__fadeInLeft",
                style=styles.Logo_Card_Styles.PARENT_BOX
            )