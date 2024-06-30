import reflex as rx
from BS_App.state.State import State
from BS_App.style import style
from BS_App.style.style import Size
from BS_App.components.battle_card import battle_card

def battlelog_view() -> rx.Component:
    return rx.vstack(
        rx.text(
                "Battle Log",
                font_size=Size.MEDIUM.value
            ),
        rx.foreach(
            State.info_player_battlelog,
            battle_card
        ),

        align="center",
        justify="center",
        
        style=style.box_style,
        width="1000px",
    )