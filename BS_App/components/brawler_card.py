import reflex as rx
import BS_App.model.Brawler as Brawler
from BS_App.style.style import Size
from BS_App.components.brawler_card_data import brawler_card_data


def brawler_card(brawler: Brawler) -> rx.Component:
    return rx.box(
        brawler_card_data(
            brawler.trophies,
            brawler.imageUrl,
            brawler.power
        ),

        rx.text(
            brawler.name,
            font_size=Size.SMALL_MEDIUM.value,
            padding_x=Size.VERY_SMALL.value,
            as_="span",
        ),
        bg=brawler.rarityColor,
        padding=Size.VERY_SMALL.value,
        border_radius=Size.SMALL.value,
        width="auto",
        height="auto",


    )
