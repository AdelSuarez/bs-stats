import reflex as rx
from BS_App.state.State import State
from BS_App.style.style import form_helper_style, Spacing, Size


def search_bar() -> rx.Component:
    return rx.hstack(
            rx.avatar(fallback="#", size=Spacing.SMALL.value),
            rx.chakra.form_control(
                rx.input(
                    name="input",
                    placeholder="Buscar Perfil...",
                    on_blur=State.set_input_value,
                    size=Spacing.SMALL.value,
                    radius="large",
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

            rx.button(
                "Buscar",
                on_click=State.update_display_value,
                size=Spacing.SMALL.value, 
            ),

            margin=Size.DEFAULT.value

        )