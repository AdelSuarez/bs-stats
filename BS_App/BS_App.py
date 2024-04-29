import reflex as rx
from style import style
from src.State import State

# TODO: Si es posible colocar como variable de entorno la api_key
scott = "CQ9JCL02"
adel = "V2Y98VYQ"
ivanna = "20CPPGUCR2"


# TODO: mejorar el codigo si lo necesita con respecto a la clase State
def action_bar() -> rx.Component:
    return rx.chakra.hstack(
        rx.flex(
            rx.avatar(fallback="#", size="3"),
            rx.chakra.form_control(
                rx.input(
                    name="input",
                    placeholder="Buscar Perfil...",
                    on_blur=State.set_input_value,
                    size="3",
                    radius="large",
                    style={"width": "200px"}
                    ),
                rx.cond(
                        State.message_input,
                        rx.chakra.form_error_message(
                            "Introduce el Codigo",
                            style={"fontSize": "15px", "margin": "0px", "padding-left":"15px"}
                        ),
                        rx.chakra.form_helper_text(
                            "Codigo de jugador",
                            style={"fontSize": "15px", "margin": "0px", "padding-left":"15px"}
                            ),
                    ),
                is_invalid=State.message_input,
                is_required=True,
            ),

            rx.button(
                "Buscar",
                on_click=State.update_display_value,
                size='3' 
            ),
            spacing="2",
        )
    )

def card_stats(title:str, data:str, image:str) -> rx.Component:
    return rx.card(
                rx.flex(

                    rx.image(src=f"/{image}", width="50px", height="50px"),
                    rx.flex(
                        rx.heading(title, size="4", font_family= "Lilita One",font_weight="300",),
                        rx.text(State.player_info[data], font_family= "Lilita One",font_weight="300",),
                        direction="column",
                        justify="center",
                        align_items="center",
                        width="100%",
                        height="100%",
                    ),
                    justify="center",
                    spacing="2",

                )
                
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
                    rx.avatar(src=State.url_icon_player, fallback="RX", size="5"),
                    rx.flex(
                        rx.heading(f'{State.player_info["name"]} | {State.player_info["trophies"]}', size="4",font_family= "Lilita One",font_weight="300",),
                        rx.image(src=f"/trophy.png", width="20px", height="20px"),
                        justify="center",
                        spacing="1",
                    ),

                    rx.flex(
                        
                        card_stats("MÁXIMO DE TROFEOS", "highestTrophies", "Ranking.webp"),
                        card_stats("VICTORIAS 3 VS 3", "3vs3Victories", "3v3.png"),
                        card_stats("VICTORIAS EN SOLITARIO", "soloVictories","Showdown.webp"),
                        card_stats("VICTORIAS EN DÚO", "duoVictories","Duo-Showdown.webp"),

                        width="90%",
                        align="center", 
                        justify="center",
                        spacing="2",

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
 
                    width="90%",
                    height= "350%",
                    bg=style.WHITE,
                    border_radius="15px",
                    padding=10,
                    margin=10,
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",

                ),

                width="80%",
                height= "90%",
                direction="column",
                align="center",
                justify="center",

                
                # bg="red",
            ),
            rx.cond(
                State.message_user_void,
                rx.box(
                    rx.heading('Jugador no existe', size="6",font_family= "Lilita One",font_weight="300",),
                    bg="#E6B0AA",
                    border_radius="10px",
                    width="30%",
                    margin="100px",
                    padding="20px",
                    text_align="center",
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",

                )
            )
        )


#TODO: Mejorar la interfaz y los componentes para que no se vean en una sola funcion
@rx.page(title="SC.Stats")
def index() -> rx.Component:
    return rx.vstack(
            rx.heading(
                "Estadisticas BS",
                size="9",
                font_family= "Lilita One",
                font_weight="300",
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
