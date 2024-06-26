import reflex as rx
from BS_App.model.Battlelog import Battlelog
from BS_App.style import style
from BS_App.style.colors import Color



def battle_card(battlelog: Battlelog) -> rx.Component:
    return rx.hstack(
        rx.flex(
            rx.vstack(
                rx.text(battlelog.eventMode),
                rx.text(battlelog.eventMap),
                spacing=style.Spacing.ZERO.value,
            ),
            rx.heading(battlelog.eventResult),
            rx.text(battlelog.battleType),
            width="100%",
            justify="between",
            align="center",
        ),

        # justify="center",
        # align_items="center",
        style=style.box_style,
        bg=Color.TERTIARY.value,
    )