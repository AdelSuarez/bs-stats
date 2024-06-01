import reflex as rx
from BS_App.style.style import Size

def navbar() -> rx.Component:
    return rx.hstack(
                rx.text(
                    "Estadisticas BS",
                    font_size=Size.MEDIUM_BIG.value,
                    margin_left=Size.DEFAULT.value,

                ),
                bg="#45B39D",
                position="sticky",
                top="0",
                z_index="999",              
                width="100%",
                padding_x=Size.SMALL.value,
            )