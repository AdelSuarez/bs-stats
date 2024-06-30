import reflex as rx
from BS_App.state.State import State
from BS_App.style.colors import Color
from BS_App.style.style import Size
from BS_App.style.style import form_helper_style,btn_style ,Spacing, Size


def search_bar() -> rx.Component:
    return rx.hstack(
            rx.hstack(

                rx.box(
                    "#",
                    bg=Color.SECONDARY.value,
                    padding=Size.SMALL.value,
                    border_radius="10px 0 0 10px",
                ),
                rx.chakra.form_control(
                    rx.chakra.input(
                        name="input",
                        placeholder="Buscar Perfil...",
                        on_blur=State.set_input_value,
                        bg=Color.WHITE.value,
                        size="md",
                        border_radius="0 10px 10px 0",
                        focus_border_color=Color.PRIMARY.value,
                        width= Size.VERY_BIG.value,
                        ),
                    rx.cond(
                            State.message_input,
                            rx.chakra.form_error_message(
                                "Introduce el Codigo",
                                style=form_helper_style,
                            ),
                            rx.chakra.form_helper_text(
                                "Codigo de jugador",
                                style=form_helper_style,
                                ),
                        ),
                    is_invalid=State.message_input,
                    is_required=True,
                ),
                justify="center",
                spacing=Spacing.ZERO.value,
            ),
            rx.button(
                "Buscar",
                on_click=State.update_display_value,
                loading=State.loading,
                size="3",
                style=btn_style,
            ),

            margin=Size.DEFAULT.value

        )