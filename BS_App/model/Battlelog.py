import reflex as rx
from BS_App.model.Team import Team

class Battlelog(rx.Base):
    eventMode: str
    eventMap: str
    eventResult: str
    battleType: str
    list_teams: list[list[Team]]
    
