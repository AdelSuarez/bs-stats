import reflex as rx
from style import style
from src.State import State

# TODO: Si es posible colocar como variable de entorno la api_key
scott = "CQ9JCL02"
adel = "V2Y98VYQ"
ivanna = "20CPPGUCR2"


# TODO: mejorar el codigo si lo necesita con respecto a la clase State
def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            name="input",
            placeholder="Buscar Perfil...",
            on_change=State.set_input_value,
            size="3",
            radius="large"
            ),
        rx.button(
            "Buscar",
            on_click=State.update_display_value,
            size='3' 
            ),
    )

def card_stats(title:str, data:str) -> rx.Component:
    return rx.card(
                rx.flex(
                    rx.heading(title, size="4"),
                    rx.text(State.player_info[data]),
                    direction="column",
                    justify="center",
                    align_items="center",
                    width="100%",
                    height="100%",
                ),
                margin=10,
            ),

def card_brawler_info(brawler: dict) -> rx.Component:
    return rx.card(
                # rx.flex(
                    rx.heading(brawler['name'], size="4"),
                    # rx.text(f'Power: {brawler["power"]}'),
                    # rx.text(f'Rank: {brawler["rank"]}'),
                    # rx.text(f'Trophies: {brawler["trophies"]}'),

                    direction="column",
                    justify="center",
                    align_items="center",
                    width="100%",
                    height="100%",
                # ),
                margin=10,
            ),


def user_profile() -> rx.Component:
    return rx.cond(
        State.is_visible,
            rx.flex(

                rx.box(
                    rx.cond(
                        State.is_loading,
                        rx.chakra.spinner(color="blue", size="lg"),
                        rx.avatar(src=State.url_icon,fallback="RX", size="5"),
                    ),
                    rx.heading(f'{State.player_info["name"]} | {State.player_info["trophies"]}', size="4"),
                    rx.flex(
                        
                        card_stats("MÁXIMO DE TROFEOS", "highestTrophies"),
                        card_stats("VICTORIAS 3 VS 3", "3vs3Victories"),
                        card_stats("VICTORIAS EN SOLITARIO", "soloVictories"),
                        card_stats("VICTORIAS EN DÚO", "duoVictories"),

                        width="90%",

                        align="center",
                        justify="center",

                    ),
                    width="90%",
                    height="100%",
                    bg=style.WHITE,
                    border_radius="15px",
                    padding=10,
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                    align_items="center",  # Alinea los elementos horizontalmente al centro
                    display="flex",  # Establece el tipo de display como Flex para habilitar Flexbox
                    flex_direction="column",
                ),
                rx.box(
                    # card_brawler_info(), 
                    #     State.list_brawlers["brawlers"],print()
                    # ),
                    # rx.heading(
                    #     State.player_info["name"], from typing import List, Dict

                    #     size="4", 
                    #     ),
                    # rx.heading(                    State.list_brawlers["brawlers"].foreach( lambda b: print(b)),

                    #     State.player_info["trophies"], 
                    #     size="4", 
                    #     ),
                    width="90%",
                    height= "350%",
                    bg=style.WHITE,
                    border_radius="15px",
                    padding=10,
                    margin=10,
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",

                ),

                width="90%",
                height= "90%",
                direction="column",
                align="center",
                justify="center",

                
                # bg="red",
            ),


            
        )


#TODO: Mejorar la interfaz y los componentes para que no se vean en una sola funcion
@rx.page(title="SC.Stats")
def index() -> rx.Component:
    return rx.vstack(
            rx.heading(
                "Estadisticas BS",
                size="9",
                # font_family= "Lilita One",
                style={
                    "margin":"20px"
                }
                ),
            rx.divider(width="90%"),
            rx.vstack(
                action_bar(),
                style={
                    "margin":"10px"
                },
                align="center",

            ),
        user_profile(),
        align="center",
        height="100vh", 
        width="100vw", 
    )   



app = rx.App(style=style.global_style,stylesheets=[
 "https://fonts.googleapis.com/css2?family=Lilita+One&display=swap",
 ],)
app.add_page(index)
