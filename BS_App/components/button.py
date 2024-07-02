import reflex as rx
from BS_App.state.State import State
from BS_App.style.colors import Color


def button(type: str):
    return rx.button(
        type,
        on_click=State.container_change(type),
        size="3",
        bg=rx.cond(
            State.current_container == type,
            Color.HOVER_BTN.value,
            Color.PRIMARY.value
        ),
        # loading=State.is_loading_button,
    )
