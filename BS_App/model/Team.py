import reflex as rx 
from typing import Optional

class Team(rx.Base):
    tag: str
    name: str
    brawlId: str
    brawlName: Optional[str] = None 
    brawlPower: int
    brawlTrophies: int
    brawlImageUrl: str