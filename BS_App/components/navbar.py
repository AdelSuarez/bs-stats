import reflex as rx
from BS_App.style.style import Size , BOX_SHADOW
from BS_App.style.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
                rx.text(
                    "Estadisticas BS",
                    font_size=Size.MEDIUM_BIG.value,
                    margin_left=Size.DEFAULT.value,
                    # color=Color.WHITE.value,
                ),
                bg=Color.PRIMARY.value,
                position="sticky",
                top="0",
                z_index="999",              
                width="100%",
                padding_x=Size.SMALL.value,
                box_shadow=BOX_SHADOW,
                
            )