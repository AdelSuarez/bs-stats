import reflex as rx
from BS_App.api.api_bs import BSapi


class State(rx.State):
    input_value: str = ''  # Almacena el valor ingresado
    display_value: str = '' # Almacena el valor a mostrar en el heading
    is_visible: bool = False # Para mostar los datos
    player_info: dict = {} # Guarda toda la informacion obtenida de la api
    url_icon_player: str = '' # Icono del jugador
    message_input:bool = False
    message_user_void:bool = False


    def set_input_value(self, value: str):
        # Este método actualiza input_value cada vez que el usuario escribe en el input
        self.input_value = value

    def is_void(self) -> bool:

        if len(self.input_value) == 0:
            self.message_input = True
        else:
            self.message_input = False
            

    async def update_display_value(self):
        self.is_void()
        self.display_value = self.input_value
        self.player_info = await BSapi().get_player_info(self.display_value)
        if isinstance(self.player_info, rx.state.MutableProxy):
            # Todos los iconos de una api de terceros 
            icons = await BSapi().get_icons()
            for icon in icons["player"]:
                # Verificamos el icono
                if str(self.player_info["icon"]["id"]) == str(icon):
                    self.url_icon_player = icons["player"][icon]["imageUrl"]
            self.is_visible = True
        elif self.player_info == "void":
            self.is_visible = False
            if not (self.message_input):
                self.message_user_void = True
        

 

