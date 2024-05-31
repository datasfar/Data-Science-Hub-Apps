import reflex as rx
import library_hub.styles.styles as styles

def big_card(title:str, description:str, list_elements:list, image:str, link_repo:str, link_app:str) -> rx.Component:
    return rx.box(
                rx.vstack(
                    rx.box(
                        rx.heading(
                            title, 
                            style=styles.Big_Card_Styles.TITLE
                        ),
                        rx.text(
                            description,
                            style=styles.Big_Card_Styles.DESCRIPTION
                        ),
                        rx.list.unordered(
                            rx.list.item(list_elements[0]),
                            rx.list.item(list_elements[1]),
                            rx.list.item(list_elements[2]),
                            rx.list.item(list_elements[3]),
                            style=styles.Big_Card_Styles.LIST
                        ),
                        rx.image(
                            src=image,
                            style=styles.Big_Card_Styles.IMAGE
                        ),
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.icon(
                                    "github",
                                    style=styles.Big_Card_Styles.BIG_BUTTON_ICON
                                ),
                                "Repositorio",
                                style=styles.Big_Card_Styles.BIG_BUTTON
                            ),
                            href=link_repo
                        ),
                        rx.link(
                            rx.button(
                                "Live Demo",
                                rx.icon(
                                    "move-up-right",
                                ),
                                style=styles.Big_Card_Styles.SMALL_BUTTON
                            ),
                            href=link_app
                        ),
                    ),
                    style=styles.Big_Card_Styles.CHILDREN_BOX
                ),
                class_name="animate__animated animate__fadeInRight",
                style=styles.Big_Card_Styles.PARENT_BOX
                
            ),