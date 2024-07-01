import reflex as rx
from BS_App.state.State import State
from BS_App.components.brawler_card import brawler_card
from BS_App.style import style
from BS_App.style.style import Size


def brawlers() -> rx.Component:
    return rx.vstack(
        rx.text(
            'BRAWLERS',
            font_size=Size.MEDIUM.value
        ),

        rx.flex(
            rx.foreach(
                State.info_player.list_brawlers,
                brawler_card
            ),
            spacing="3",
            flex_wrap="wrap",
            align="center",
            justify="center",
        ),
        align="center",
        justify="center",
        style=style.box_style
    )
