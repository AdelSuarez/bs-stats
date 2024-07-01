import reflex as rx
from typing import Optional


class Brawler(rx.Base):
    name: Optional[str] = None
    imageUrl: str
    rarity: str
    rarityColor: str
    type: str
