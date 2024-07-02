import reflex as rx
from BS_App.model.Team import Team
from BS_App.style.style import Spacing
from BS_App.components.brawler_card_data import brawler_card_data


def battle_card_player(player: Team) -> rx.Component:
    return rx.vstack(
        brawler_card_data(
            player.brawlTrophies,
            player.brawlImageUrl,
            player.brawlPower,
        ),
        # rx.image(
        #     src=player.brawlImageUrl,
        #     width="100px",
        #     height="100px",
        # ),
        rx.text(
            player.name,
            as_="span"
        ),
        spacing=Spacing.ZERO.value,

    )
