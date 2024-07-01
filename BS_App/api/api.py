from .BsApi import BsApi
from BS_App.model.Player import Player
from BS_App.model.Battlelog import Battlelog


BRAWL_API = BsApi()

# Obtenemos la información de un jugador con la intancia a la API


async def get_brawl_api(tag: str) -> Player:
    return await BRAWL_API.fetch_info(tag)

# Obtenemos la información de el registro de batallas de un jugador con la intancia a la API


async def get_battlelog(tag: str) -> list[Battlelog]:
    return await BRAWL_API.get_battlelog(tag)
