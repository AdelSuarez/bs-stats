import reflex as rx
import BS_App.model.Brawler as Brawler
from BS_App.style.style import Size


def brawler_card(brawler: Brawler) -> rx.Component:
    return rx.box(
        rx.image(
            src=brawler.imageUrl,
            width="100px",
            height="100px",
            border_radius=Size.SMALL.value,

        ),
        rx.text(
            brawler.name,
            font_size=Size.SMALL_MEDIUM.value
        ),
        bg=brawler.rarityColor,
        padding=Size.SMALL.value,
        border_radius=Size.SMALL.value,
        width="auto",
        height="auto",
        aling="center",

    )
