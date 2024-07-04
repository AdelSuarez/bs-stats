import reflex as rx
from BS_App.state.State import State
from BS_App.components.card_profile import card_profile
from BS_App.components.button import button
from BS_App.views.brawlers import brawlers
from BS_App.views.battlelog_view import battlelog_view
from BS_App.components.message import message
from BS_App import constants


def profile() -> rx.Component:
    return rx.cond(
        State.success,
        rx.cond(
            State.is_visible_profile,
            rx.vstack(
                card_profile(),
                rx.hstack(
                    button(constants.BTN_BRAWLER),
                    button(constants.BTN_BATTLELOG),
                ),

                rx.cond(
                    State.current_container == constants.BTN_BRAWLER,
                    brawlers(),
                    rx.cond(
                        State.current_container == constants.BTN_BATTLELOG,
                        battlelog_view(),
                    ),
                ),
                align="center",
            ),
            rx.cond(
                State.loading,
                rx.spinner(size="3"),

            ),
        ),
        rx.cond(
            ~State.success,
            message(State.error_message),
            rx.cond(
                State.loading,
                rx.spinner(size="3"),

            ),
        )
    )
