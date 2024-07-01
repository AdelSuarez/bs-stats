import reflex as rx
from BS_App.model.Brawler import Brawler


class Player(rx.Base):
    is_visible: bool
    tag: str
    name: str
    icon: str
    trophies: int
    highestTrophies: int
    expLevel: int
    Victories3vs3: int
    SoloVictories: int
    DuoVictories: int
    clubName: str
    list_brawlers: list[Brawler]
