import reflex as rx
from BS_App.style import style
from BS_App.style.style import Size

def battlelog() -> rx.Component:
    return rx.vstack(
        rx.text(
                "Battle Log",
                font_size=Size.MEDIUM.value
            ),
        rx.text("No battles yet"),
        style=style.box_style,
        align="center",
        justify="center",
    )