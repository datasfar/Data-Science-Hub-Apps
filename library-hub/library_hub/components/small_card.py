import reflex as rx
import library_hub.styles.styles as styles

def small_card(title:str, description:str, image:str, link:str) -> rx.Component:
    return rx.box(
                rx.vstack(
                    rx.box(
                        rx.heading(
                            title, 
                            style=styles.Small_Card_Styles.TITLE
                        ),
                        rx.text(
                            description,
                            style=styles.Small_Card_Styles.DESCRIPTION
                        ),
                    ),
                    rx.image(
                        src=image,
                        style=styles.Small_Card_Styles.IMAGE
                    ),
                    rx.link(
                        rx.button(
                            rx.icon(
                                "github",
                                style=styles.Small_Card_Styles.BIG_BUTTON_ICON
                            ),
                            "Repositorio",
                            style=styles.Small_Card_Styles.BIG_BUTTON
                        ),
                        href=link
                    ),
                    style=styles.Small_Card_Styles.CHILDREN_BOX
                ),
                class_name="animate__animated animate__fadeInUp",
                style=styles.Small_Card_Styles.PARENT_BOX
            ),