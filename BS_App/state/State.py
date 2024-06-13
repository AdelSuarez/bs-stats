import reflex as rx
from typing import Dict, Any
from BS_App.api.api import get_brawl_api
from BS_App.model.Player import Player


class State(rx.State):
    all_info: dict = {"visible": False, "info": {}}
    is_visible: bool = all_info["visible"]
    player_info: Dict[str, Any] = all_info["info"]
    url_icon_player: str = ''# Icono del jugador
    
    info_player = Player(is_visible=False, 
                         tag="", 
                         name="", 
                         icon="", 
                         trophies=0, 
                         highestTrophies=0, 
                         expLevel=0, 
                         Victories3vs3=0, 
                         SoloVictories=0, 
                         DuoVictories=0, 
                         clubName=""
                         )


    input_value: str = ''  # Almacena el valor ingresado
    display_value: str = '' # Almacena el valor a mostrar en el heading
    message_input: bool = False
    message_user_void: bool = False
    message_error_api: bool = False


    def set_input_value(self, value: str):
        # Este método actualiza input_value cada vez que el usuario escribe en el input
        self.input_value = value

    def is_void(self) -> bool:
        # Verifica si el input_value esta vacio
        if len(self.input_value) == 0:
            self.message_input = True
            return False
        else:
            self.message_input = False
            return True
        

    async def update_display_value(self):
        if self.is_void():
            self.info_player = await get_brawl_api(self.input_value)

    # async def update_display_value(self):
    #     if self.is_void():
    #         # Obtenemos la información del jugador 
    #         self.all_info = await get_brawl_api(self.input_value)
    #         if self.all_info["info"] != {} and self.all_info["info"] != "error_api":
    #             self.is_visible = self.all_info["visible"]
    #             self.player_info = self.all_info["info"]
    #             self.url_icon_player = self.player_info["icon"]["imageUrl"]
        # else:
        #     print("")
        # self.is_void()
        # self.display_value = self.input_value
        # self.player_info = await BsApi().get_player_info(self.display_value)
        # print(type(self.player_info))
        # if isinstance(self.player_info, rx.state.MutableProxy):
        #     # Todos los iconos de una api de terceros 
        #     icons = await BsApi().get_icons()
        #     for icon in icons["player"]:
        #         # Verificamos el icono
        #         if str(self.player_info["icon"]["id"]) == str(icon):
        #             self.url_icon_player = icons["player"][icon]["imageUrl"]
        #     self.is_visible = True
        #     # dict_user =  await BsApi().fetch_info(self.display_value)
        #     # print(dict_user["info"]["icon"]["imageUrl"])

        # elif self.player_info == "void":
        #     self.is_visible = False
        #     if not (self.message_input):
        #         self.message_user_void = True
        # elif self.player_info == "error_api":
        #     print("error")

        

 

