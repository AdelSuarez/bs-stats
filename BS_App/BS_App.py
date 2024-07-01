import reflex as rx
from BS_App.style import style
from BS_App.components.navbar import navbar
from BS_App.views.search_bar import search_bar
from BS_App.views.profile import profile

# TODO: Si es posible colocar como variable de entorno la api_key
scott = "CQ9JCL02"
adel = "V2Y98VYQ"
ivanna = "20CPPGUCR2"
TOP1 = "PR9U2JL"


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
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
    title="BS State"
)
