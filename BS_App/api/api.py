from .BsApi import BsApi

BRAWL_API = BsApi()

async def get_brawl_api(tag: str):
    return await BRAWL_API.fetch_info(tag)