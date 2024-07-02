import reflex as rx
from BS_App.model.Battlelog import Battlelog
from BS_App.style.style import Size, box_style, Spacing
from BS_App.style.colors import Color
from BS_App.components.battle_card_player import battle_card_player


def battle_card(battlelog: Battlelog) -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.vstack(
                rx.text(battlelog.eventMode),
                rx.text(battlelog.eventMap),
                spacing=Spacing.ZERO.value,
            ),
            rx.heading(battlelog.eventResult),
            rx.text(battlelog.battleType),
            width="100%",
            justify="between",
            align="center",
        ),

        rx.flex(
            rx.hstack(
                rx.foreach(
                    battlelog.list_teams[0],
                    lambda player: battle_card_player(player),

                ),
            ),
            rx.heading("vs"),
            rx.hstack(
                rx.foreach(
                    battlelog.list_teams[1],
                    lambda player: battle_card_player(player),

                ),
            ),
            width="100%",
            justify="between",
            align="center",
        ),
        padding=Size.DEFAULT.value,

        style=box_style,
        bg=Color.TERTIARY.value,
    )
