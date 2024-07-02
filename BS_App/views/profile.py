import reflex as rx
from BS_App.state.State import State
from BS_App.components.card_profile import card_profile
from BS_App.components.button import button
from BS_App.views.brawlers import brawlers
from BS_App.views.battlelog_view import battlelog_view
from BS_App import constants
from BS_App.style.style import BOX_SHADOW


def profile() -> rx.Component:
    return rx.cond(
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
        # rx.cond(
        #     State.message_user_void,
        #     # message("Error con la api"),
        #     # message("Error con la api"),

        #     rx.box(
        #         rx.heading('Jugador no existe', size="6",
        #                    font_family="Lilita One", font_weight="300",),
        #         bg="#E6B0AA",
        #         border_radius="10px",
        #         width="30%",
        #         margin="100px",
        #         padding="20px",
        #         text_align="center",
        #         box_shadow=BOX_SHADOW,

        #     ),
        # ),
    )
