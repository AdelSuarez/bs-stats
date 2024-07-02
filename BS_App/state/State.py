import reflex as rx
from BS_App.api.api import get_brawl_api, get_battlelog
from BS_App import constants
from BS_App.model.Player import Player
from BS_App.model.Battlelog import Battlelog


class State(rx.State):

    is_loading_search: bool = False
    is_loading_battlelog: bool = False

    current_container: str = constants.BTN_BRAWLER

    info_player_battlelog: list[Battlelog] = []

    info_player: Player = Player(
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
    )

    is_visible_profile: bool = False

    input_value: str = ''  # Almacena el valor ingresado
    # display_value: str = '' # Almacena el valor a mostrar en el heading
    message_input: bool = False
    message_user_void: bool = False
    message_error_api: bool = False

    @rx.var
    def loading(self) -> bool:
        return self.is_loading_search

    @rx.var
    def loading_battlelog(self) -> bool:
        return self.is_loading_battlelog

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
        self.info_player_battlelog = []
        self.current_container: str = constants.BTN_BRAWLER
        self.is_visible_profile = False
        self.is_loading_search = False
        self.is_loading_battlelog = False

        yield
        if self.is_void():
            self.is_loading_search = True
            yield
            self.info_player = await get_brawl_api(self.input_value)

            if self.info_player:
                self.is_visible_profile = True

            self.is_loading_search = False
            yield

    async def update_display_value_battlelog(self):
        self.info_player_battlelog = await get_battlelog(self.input_value)

    async def container_change(self, container: str):

        self.current_container = container

        if self.info_player_battlelog == []:
            if container == constants.BTN_BATTLELOG:
                yield

                await self.update_display_value_battlelog()
                self.is_loading_battlelog = True
                yield
