from .BsApi import BsApi
from BS_App.model.Player import Player


BRAWL_API = BsApi()

# Obtenemos la información de un jugador con la intancia a la API
async def get_brawl_api(tag: str) -> Player:
    return await BRAWL_API.fetch_info(tag)