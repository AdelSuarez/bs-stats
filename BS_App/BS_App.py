import reflex as rx
from BS_App.style import style, colors
from BS_App.state.State import State
from BS_App.components.message import message
from BS_App.components.card_stats import card_stats
from BS_App.views.header import header
from BS_App.views.search_bar import search_bar
from BS_App.views.profile import profile

# TODO: Si es posible colocar como variable de entorno la api_key
scott = "CQ9JCL02"
adel = "V2Y98VYQ"
ivanna = "20CPPGUCR2"
TOP1="PR9U2JL"


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



def index() -> rx.Component:
    return rx.vstack(
            header(),
            search_bar(),
            profile(),
            align="center",
            height="100vh", 
            width="100vw", 
        )   

app = rx.App(
    stylesheets=style.STYLESHEETS,
    style=style.BASE_STYLE,
)
app.add_page(
    index,
    title= "BS State"  
)
