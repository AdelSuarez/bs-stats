from .BsApi import BsApi

BRAWL_API = BsApi()

# Obtenemos la información de un jugador con la intancia a la API
async def get_brawl_api(tag: str):
    return await BRAWL_API.fetch_info(tag)