import aiohttp
import BS_App.constants as constants
from BS_App.model.Player import Player
from BS_App.model.Brawler import Brawler

class BsApi:
    def __init__(self):
        self.api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjgyZmE0MGU0LTA4ZjMtNDQ3Ni1hYTJhLTYwNTQ2YWNjYzA3NCIsImlhdCI6MTcxODc1Mjk2Niwic3ViIjoiZGV2ZWxvcGVyL2FmODJlOTc2LWNmMmYtZDMxMC1iMjFhLWFjZTlhZGJhMTZiNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTI5LjIyMi4xLjE2OCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.rU91rozECo3yWJKrwKJ4c2gcg_da4UW27lShZb7hB-CKEq4XhFnc5-LwKwDbCdrNNs_QZTLGOoJsO7MQxWR1QA"

    async def fetch_info(self, player_tag: str) -> Player:

        # Toda la informacion para conectarse a la API
        url = f"{constants.BASE_URL_BSAPI}{player_tag}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        list_brawlers = []

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                
                if response.status == 200:

                    player_info = await response.json()
                    # Todos los iconos de una api de terceros 
                    # obtenemos la informacion
                    icons_players = await self.get_data_brawApi('/icons')
                    info_brawlers = await self.get_data_brawApi('/brawlers')

                    for icon in icons_players["player"]:
                        # Verificamos el icono
                        if str(player_info["icon"]["id"]) == str(icon):
                            # Obtenemos la información de los brawlers
                            self._data_upload(player_info["brawlers"], info_brawlers["list"], list_brawlers)
                            # retornamos la información del jugador
                            return Player(
                                    is_visible=True,
                                    tag=player_info['tag'], 
                                    name=player_info['name'], 
                                    icon=icons_players["player"][icon]["imageUrl"], 
                                    trophies=player_info['trophies'], 
                                    highestTrophies=player_info['highestTrophies'], 
                                    expLevel=player_info['expLevel'], 
                                    Victories3vs3=player_info['3vs3Victories'], 
                                    SoloVictories=player_info['soloVictories'], 
                                    DuoVictories=player_info['duoVictories'],
                                    clubName=player_info['club']['name'] if player_info.get('club', {}) else "",
                                    list_brawlers=list_brawlers
                                )

        
                # Verificamos si el jugador no fue encontrado
                elif response.status == 404:
                    print("Jugador no encontrado")
                    return {"visible": False, "info": {}, "error": "void"}
                elif response.status == 403:
                    # Error de autenticación con la api
                    print("Error de autenticación")
                    return {"visible": False, "info": {}, "error": "api"}

                else:
                    print(f"Error HTTP: {response.status}")

    async def get_data_brawApi(self, endpoint: str) -> dict:
        # URL base de la API

        # Ruta para obtener íconos
        # Realizamos la petición a la API para obtener los íconos
        async with aiohttp.ClientSession() as session:
            async with session.get(constants.BASE_URL_BRAWLAPI + endpoint) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error al obtener datos. Código de estado: {response.status}")

    
    def _data_upload(self,list_player:dict, list_brawlApi: dict, list_brawlers:dict) -> dict:
        for brawler in list_player:
            for brawler_data in list_brawlApi:
                if brawler["id"] == brawler_data["id"]:
                    list_brawlers.append(Brawler(name=brawler["name"], 
                                                imageUrl=brawler_data["imageUrl2"],
                                                rarity=brawler_data["rarity"]["name"],
                                                rarityColor=brawler_data["rarity"]["color"], 
                                                type=brawler_data["class"]["name"]
                                                )
                                            )