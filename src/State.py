import reflex as rx
from api.api_bs import BSapi

class State(rx.State):
    input_value: str = ''  # Almacena el valor ingresado
    display_value: str = '' # Almacena el valor a mostrar en el heading
    is_visible: bool = False
    player_info: dict = {}
    url_icon: str = ""
    is_loading: bool = True


    def set_input_value(self, value: str):
        # Este método actualiza input_value cada vez que el usuario escribe en el input
        self.input_value = value

    def update_display_value(self):
        self.display_value = self.input_value
        self.player_info = BSapi().get_player_info(self.display_value)
        if self.player_info != {}:
            self.is_visible = True
            icons =  BSapi().get_icons()
            for icon in icons["player"]:
                if str(self.player_info["icon"]["id"]) == str(icon):
                    self.url_icon = icons["player"][icon]["imageUrl"]
                    self.is_loading = False
            # BSapi().get_icons()
            # print(self.player_info["brawlers"] )
            # for brawler in self.player_info["brawlers"]:
            #     print(brawler)
            #     self.list_brawlers.append(brawler)
            # print(State.list_brawlers),


    # def update_display_value(self):
    #     self.display_value = self.input_value
    #     self.player_info = BSapi().get_player_info(self.display_value)
    #     if self.player_info:
    #         self.is_visible = True
    #         brawlers = [self.create_brawler(b) for b in self.player_info["brawlers"]]
    #         club = self.create_club(self.player_info.get("club")) if self.player_info.get("club") else None
    #         player = Player(self.player_info["tag"], self.player_info["name"], self.player_info["nameColor"], self.player_info["icon"]["id"], self.player_info["trophies"], self.player_info["highestTrophies"], self.player_info["expLevel"], self.player_info["expPoints"], self.player_info["isQualifiedFromChampionshipChallenge"], self.player_info["3vs3Victories"], self.player_info["soloVictories"], self.player_info["duoVictories"], self.player_info["bestRoboRumbleTime"], self.player_info["bestTimeAsBigBrawler"], club, brawlers)
    #         print(player.name)

    # def create_brawler(self, brawler_info):
    #     gadgets = [Gadget(g["id"], g["name"]) for g in brawler_info.get("gadgets", [])]
    #     starPowers = [StarPower(sp["id"], sp["name"]) for sp in brawler_info.get("starPowers", [])]
    #     gears = [Gear(g["id"], g["name"], g["level"]) for g in brawler_info.get("gears", [])]
    #     return Brawler(brawler_info["id"], brawler_info["name"], brawler_info["power"], brawler_info["rank"], brawler_info["trophies"], brawler_info["highestTrophies"], gears, starPowers, gadgets)

    # def create_club(self, club_info):
    #     return Club(club_info.get("tag", ""), club_info.get("name", ""))
