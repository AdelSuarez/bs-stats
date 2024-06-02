import aiohttp
import BS_App.constants as constants
import reflex as rx

class BsApi:
    def __init__(self):
        self.api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM3MDBkYWNlLWFlODQtNDkxMS04MTRlLWRjZTI1MWFmOTBlMSIsImlhdCI6MTcxNzI4Mjk4Niwic3ViIjoiZGV2ZWxvcGVyL2FmODJlOTc2LWNmMmYtZDMxMC1iMjFhLWFjZTlhZGJhMTZiNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTM4Ljg0LjQxLjIxOSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.KyqGEVvUqIa5hgn9aELzrC3CGMgXs74MT84E2sMrwxS18VauoflYdlIIBqDRpaGdOy1OCsgPUvtJt3sTyD05nQ"

    async def fetch_info(self, player_tag: str):
        url = f"{constants.BASE_URL_BSAPI}{player_tag}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                        

                    if response.status == 200:
                        player_info = await response.json()
                        # Todos los iconos de una api de terceros 
                        icons = await self.get_icons()
                        icon_info = player_info.get('icon')

                        if icon_info is not None:
                            for icon in icons["player"]:
                                # Verificamos el icono
                                if str(icon_info["id"]) == str(icon):
                                    icon_info["imageUrl"] = icons["player"][icon]["imageUrl"]
                                    return {"visible":True, "info": player_info, "error": ""}
            
                    elif response.status == 404:
                        print("Jugador no encontrado")
                        return {"visible": False, "info": {}, "error": "void"}
                    elif response.status == 403:
                        print("Error de autenticación")
                        return {"visible": False, "info": {}, "error": "api"}

                    else:
                        print(f"Error HTTP: {response.status}")

    async def get_icons(self):
        # URL base de la API
        base_url = 'https://api.brawlapi.com/v1'

        # Ruta para obtener íconos
        icons_endpoint = '/icons'

        async with aiohttp.ClientSession() as session:
            async with session.get(base_url + icons_endpoint) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    print(f"Error al obtener íconos. Código de estado: {response.status}")