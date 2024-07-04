import reflex as rx
from enum import Enum
from .colors import Color
from .fonts import Font, FontWeight

# usamos el enum para definir los valores de las constantes

# Constants
MAX_WIDTH = "1000px"
BOX_SHADOW = "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"


# Size
class Size(Enum):
    ZERO = "0px !important"
    VERY_SMALL = "0.3rem"
    SMALL = "0.5em"
    SMALL_MEDIUM = "0.85em"
    DEFAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    MEDIUM_BIG = "3em"
    VERY_BIG = "16em"

# Spacing


class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    MEDIUM_SMALL = "2"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    MEDIUM_LARGE = "6"
    BIG = "7"
    MEDIUM_BIG = "8"
    VERY_BIG = "9"


# Styles
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Lilita+One&display=swap"
]

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "background": Color.BG.value,
    rx.input: {
        "font_family": Font.DEFAULT.value,
    },
    rx.button: {
        "font_family": Font.DEFAULT.value,
        "cursor": "pointer",
    },
    rx.text: {
        "font_family": Font.DEFAULT.value,
        "font_weight": FontWeight.LIGHT.value,
    }
}

form_helper_style = dict(
    margin=Size.ZERO.value,
    padding_left=Size.DEFAULT.value,
)

btn_style = dict(
    bg=Color.PRIMARY.value,
    _hover={
        "bg": Color.HOVER_BTN
    },
)

text_data_brawler_style = dict(
    position="absolute",
    z_index="1",
    padding_x=Size.SMALL.value,
    bg=Color.BG_STATS.value,
    color=Color.WHITE.value

)


box_style = dict(
    bg=Color.WHITE.value,
    width="100%",
    max_width=MAX_WIDTH,
    margin_bottom=Size.SMALL.value,
    padding=Size.SMALL.value,
    border_radius=Size.SMALL.value,
    box_shadow=BOX_SHADOW
)

flex_card_brawler_style = dict(
    spacing=Spacing.SMALL.value,
    flex_wrap="wrap",
    justify="center",
    align="center"
)
