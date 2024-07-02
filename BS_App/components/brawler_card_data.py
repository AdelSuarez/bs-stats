import reflex as rx
from BS_App.style.style import Size, text_data_brawler_style, Spacing


def brawler_card_data(trophies: int, imageUrl: str, power: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src="/trophy.png",
                width="auto",
                height=Size.SMALL_MEDIUM.value
            ),

            rx.text(
                trophies,
                font_size=Size.SMALL_MEDIUM.value,
                as_="span"

            ),
            style=text_data_brawler_style,
            align="center",
            top="0",
            left="0",
            border_radius=f'{Size.SMALL.value} 0 0 0',
            spacing=Spacing.VERY_SMALL.value,
        ),
        rx.image(
            src=imageUrl,
            width="100px",
            height="100px",
            border_radius=Size.SMALL.value,

        ),
        rx.text(
            f'POWER {power}',
            font_size=Size.SMALL_MEDIUM.value,

            style=text_data_brawler_style,
            bottom="0",
            right="0",
            border_radius=f'0 0 {Size.SMALL.value} 0',
            as_="span"

        ),
        position="relative",
        width="100px",
        height="100px",
        border_radius=Size.SMALL.value,

    ),
