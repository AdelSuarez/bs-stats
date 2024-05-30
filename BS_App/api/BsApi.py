import aiohttp
import BS_App.constants as constants

class BsApi:
    def __init__(self):
        self.base_url = "https://api.brawlstars.com/v1/players/%23"
        self.api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImFjMjkxMzQ1LTA0NzYtNDg1MC05MzFmLTUyYjI3MTY3ZTJhMCIsImlhdCI6MTcxNzAzNDM3Niwic3ViIjoiZGV2ZWxvcGVyL2FmODJlOTc2LWNmMmYtZDMxMC1iMjFhLWFjZTlhZGJhMTZiNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTM4Ljg0LjQxLjE5Il0sInR5cGUiOiJjbGllbnQifV19.lj0tE1c6TtH2jOGv0wTKZXlEqq6y1x46fYWZFVj1SaAxlXV9DcIqGdN1MaPA9wyYjmJsl8vmrIN44oq3_rOT8A"

    async def get_player_info(self, player_tag):
        url = f"{self.base_url}{player_tag}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 404:
                    return "void"
                elif response.status == 403:
                    return "error_api"
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
