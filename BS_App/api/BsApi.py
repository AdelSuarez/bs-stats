import aiohttp
import BS_App.constants as constants
from BS_App.model.Player import Player
from BS_App.model.Brawler import Brawler
from BS_App.model.Battlelog import Battlelog
from BS_App.model.Team import Team


class BsApi:

    async def fetch_info(self, player_tag: str) -> Player:

        # Toda la informacion para conectarse a la API
        url = f"{constants.BASE_URL_BSAPI}{player_tag}"

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {constants.API_KEY}"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:

                if response.status == 200:

                    player_info = await response.json()
                    # Todos los iconos de una api de terceros
                    icons_players = await self.__get_data_brawApi('/icons')
                    info_brawlers = await self.__get_data_brawApi('/brawlers')

                    for icon in icons_players["player"]:
                        # Verificamos el icono
                        if str(player_info["icon"]["id"]) == str(icon):
                            # Obtenemos la información de los brawlers

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
                                clubName=player_info['club']['name'] if player_info.get(
                                    'club', {}) else "",
                                list_brawlers=self.__data_upload(
                                    player_info["brawlers"], info_brawlers["list"]),
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

    async def get_battlelog(self, player_tag: str) -> list[Battlelog]:
        url = f"{constants.BASE_URL_BSAPI}{player_tag}/battlelog"
        count: int = 0
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {constants.API_KEY}"
        }
        list_battlelog: list[Battlelog] = []

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:

                if response.status == 200:
                    info = await response.json()
                    for battle in info["items"]:
                        if count == 8:
                            break
                        list_battlelog.append(Battlelog(eventMode=battle["event"]["mode"],
                                                        eventMap=battle["event"]["map"],
                                                        eventResult=battle["battle"].get(
                                                            "result", "-"),
                                                        battleType=battle["battle"].get(
                                                            "type", "Tipo de batalla no disponible"),
                                                        list_teams=await self.__get_teams(battle["battle"]["teams"])
                                                        )
                                              )
                        count += 1
                else:
                    print(f"Error al obtener datos. Código de estado: {
                          response.status}")

        return list_battlelog

    async def __get_data_brawApi(self, endpoint: str) -> dict:
        # Realizamos la petición a la API para obtener los íconos
        async with aiohttp.ClientSession() as session:
            async with session.get(constants.BASE_URL_BRAWLAPI + endpoint) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error al obtener datos. Código de estado: {
                          response.status}")

    def __data_upload(self, list_player: dict, list_brawlApi: dict) -> list[Brawler]:
        list_brawlers: list[Brawler] = []

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
        return list_brawlers

    # async def _get_teams(self, teams: list[dict]):
    #     list_teams: list[list[Team]] = []
    #     brawler_imageUrl = ""
    #     info_brawlers = await self._get_data_brawApi('/brawlers')

    #     # Crear un diccionario para mapear ID de brawler a su imagen
    #     brawler_images = {brawler["id"]: brawler["imageUrl2"] for brawler in info_brawlers["list"]}

    #     for team in teams:
    #         list_team: list[Team] = []
    #         for player in team:
    #             # Usar el diccionario para obtener la imagen directamente
    #             brawler_imageUrl = brawler_images.get(player["brawler"]["id"], "")

    #             list_team.append(Team(tag=player["tag"],
    #                                 name=player["name"],
    #                                 brawlId=player["brawler"]["id"],
    #                                 brawlName=player["brawler"]["name"],
    #                                 brawlPower=player["brawler"]["power"],
    #                                 brawlTrophies=player["brawler"]["trophies"],
    #                                 brawlImageUrl=brawler_imageUrl
    #                                 )
    #                             )
    #         list_teams.append(list_team)

    async def __get_teams(self, teams: list[dict]) -> list[list[Team]]:
        info_brawlers = await self.__get_data_brawApi('/brawlers')
        # Crear un diccionario para mapear ID de brawler a su imagen
        brawler_images = {brawler["id"]: brawler["imageUrl2"]
                          for brawler in info_brawlers["list"]}

        list_teams = [
            [
                Team(
                    tag=player["tag"],
                    name=player["name"],
                    brawlId=player["brawler"]["id"],
                    brawlName=player["brawler"]["name"],
                    brawlPower=player["brawler"]["power"],
                    brawlTrophies=player["brawler"]["trophies"],
                    brawlImageUrl=brawler_images.get(
                        player["brawler"]["id"], "")
                )
                for player in team
            ]
            for team in teams
        ]

        return list_teams
