import reflex as rx
from BS_App.state.State import State
from BS_App.components.brawler_card import brawler_card
from BS_App.style import style
from BS_App.style.colors import Color
from BS_App.style.style import Size, BOX_SHADOW
from BS_App.style.colors import Color


def brawlers() -> rx.Component:
    return rx.vstack(
                    rx.text(f'BRAWLERS'),

                    rx.flex(
                        rx.foreach(
                            State.info_player.list_brawlers,
                            brawler_card
                        ),
                        spacing = "1",
                        flex_wrap="wrap",
                        height="100%", 
                        width="100%", 
                    ),
                    align="center",

                    bg=Color.WHITE.value,
                    border_radius=Size.SMALL.value,
                    padding=10,
                    margin=10,
                    box_shadow=BOX_SHADOW,
                    max_width=style.MAX_WIDTH,
                ),