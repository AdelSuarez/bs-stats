import reflex as rx

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
