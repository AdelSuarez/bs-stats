import reflex as rx
from BS_App.api.api import get_brawl_api
from BS_App import constants
from BS_App.model.Player import Player



class State(rx.State):


    current_container: str = constants.BTN_BRAWLER
    
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
                         clubName="",
                         list_brawlers=[],
                         list_battlelog=[]
                        )

    input_value: str = ''  # Almacena el valor ingresado
    # display_value: str = '' # Almacena el valor a mostrar en el heading
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

    def container_change(self, container: str):
        self.current_container = container

        

 

