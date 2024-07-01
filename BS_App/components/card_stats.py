import reflex as rx
from BS_App.style.style import Size, Spacing
from BS_App.style.colors import Color


def card_stats(title: str, data: str, image: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src=f"/{image}",
                width="auto",
                height=Size.MEDIUM_BIG.value,
            ),
            rx.vstack(
                rx.text(
                    title,
                    font_size=Size.DEFAULT.value
                ),
                rx.text(data),
                align_items="center",
                spacing=Spacing.ZERO.value,
            ),
            justify="center",
            align_items="center",

        ),
        padding=Size.SMALL.value,
        border_radius=Size.SMALL.value,
        bg=Color.TERTIARY.value,
    ),
