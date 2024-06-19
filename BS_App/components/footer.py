import reflex as rx
from BS_App.style.style import Size
from BS_App.style.colors import Color

def footer() -> rx.Component:
    return rx.hstack(
                rx.text(
                    "© 2021 Brawl Stars",
                ), 
                width="100%",
                bg=Color.PRIMARY.value,
                color=Color.BG.value,
                font_size=Size.DEFAULT.value,

                # align="center",
                # justify="center",
                position="fixed",
                bottom="0",
            )