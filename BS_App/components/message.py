import reflex as rx
from BS_App.style.style import BOX_SHADOW
from BS_App.style.style import Size



def message(text: str, color:str) -> rx.Component:
    return rx.box(
                rx.text(text),
                border_radius=Size.SMALL.value,
                bg=color,
                width="30%",
                margin="100px",
                padding="20px",
                text_align="center",
                box_shadow=BOX_SHADOW,
            )