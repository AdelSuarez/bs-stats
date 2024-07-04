import reflex as rx
from BS_App.model.Battlelog import Battlelog
from BS_App.style.style import Size, box_style, Spacing, flex_card_brawler_style
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
            rx.flex(
                rx.foreach(
                    battlelog.list_teams[0],
                    lambda player: battle_card_player(player),

                ),
                **flex_card_brawler_style,
            ),
            rx.heading(
                "vs",
                margin_x=Size.BIG.value
            ),
            rx.flex(
                rx.foreach(
                    battlelog.list_teams[1],
                    lambda player: battle_card_player(player),

                ),
                **flex_card_brawler_style,
            ),
            width="100%",
            justify="between",
            align="center",
        ),
        padding=Size.DEFAULT.value,

        style=box_style,
        bg="#eaeded",
    )
