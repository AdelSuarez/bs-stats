import reflex as rx
from BS_App.model.Team import Team
from BS_App.style.style import Spacing
from BS_App.components.brawler_card_data import brawler_card_data


def battle_card_player(player: Team) -> rx.Component:
    return rx.vstack(
        rx.cond(
            player.starPlayer,
            rx.text(
                "STAR PLAYER",
                # color="#f4d03f",
                as_="span"
            ),
            rx.text(
                "-",
                as_="span"
            ),
        ),
        brawler_card_data(
            player.brawlTrophies,
            player.brawlImageUrl,
            player.brawlPower,
        ),
        rx.text(
            player.name,
            as_="span"
        ),
        spacing=Spacing.ZERO.value,

    )
