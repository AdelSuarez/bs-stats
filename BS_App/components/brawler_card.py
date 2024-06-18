import reflex as rx
import BS_App.model.Brawler as Brawler


def brawler_card(brawler: Brawler) -> rx.Component:
    return rx.card(
                rx.text(brawler.name, size="4"),
                rx.text(brawler.rarity, size="2")
            )