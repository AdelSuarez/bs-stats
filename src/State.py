import reflex as rx
from api.api_bs import BSapi

class State(rx.State):
    input_value: str = ''  # Almacena el valor ingresado
    display_value: str = '' # Almacena el valor a mostrar en el heading
    is_visible: bool = False
    player_info: dict = {};
    list_brawlers: list[dict] = []


    def set_input_value(self, value: str):
        # Este método actualiza input_value cada vez que el usuario escribe en el input
        self.input_value = value

    def update_display_value(self):
        self.display_value = self.input_value
        self.player_info = BSapi().get_player_info(self.display_value)
        if self.player_info != {}:
            self.is_visible = True
            BSapi().get_icons()
            # print(self.player_info["brawlers"] )
            # for brawler in self.player_info["brawlers"]:
            #     print(brawler)
            #     self.list_brawlers.append(brawler)
            # print(State.list_brawlers),
