import reflex as rx
from enum import Enum
from .colors import Color
from .fonts import Font


# Constants
MAX_WIDTH = "1200px"


# Size
class Size(Enum):
    ZERO = "0px !important"
    DEFAULT = "1em"
    MEDIUM = "2em"
    VERY_BIG = "16em"

# Spacing
class Spacing(Enum):
    ZERO = "0"
    VERY_SMALL = "1"
    MEDIUM_SMALL= "2"
    SMALL = "3"
    DEFAULT = "4"
    LARGE = "5"
    BIG = "6"
    MEDIUM_BIG = "7"
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
    }
}

form_helper_style = dict(
    margin=Size.ZERO.value,
    padding_left=Size.DEFAULT.value,
)