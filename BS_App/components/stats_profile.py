import reflex as rx
from BS_App.style.style import Size, Spacing
from BS_App.state.State import State

def stats_profile(image:str, text:str) -> rx.Component:
    return rx.hstack(
                rx.image(src=image, width=Size.MEDIUM.value, height=Size.MEDIUM.value),
                rx.chakra.span(
                    text,
                    font_size=Size.DEFAULT.value,
                ),
                spacing=Spacing.VERY_SMALL.value,
            )