import reflex as rx
from BS_App.style.style import Size, Spacing


def card_data_profile(image: str, text: str) -> rx.Component:
    return rx.hstack(
        rx.image(
            src=image,
            width="auto",
            height=Size.MEDIUM.value
        ),
        rx.text(
            text,
            font_size=Size.DEFAULT.value,
            as_="span"
        ),
        spacing=Spacing.VERY_SMALL.value,
    )
