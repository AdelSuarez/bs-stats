import reflex as rx
from BS_App.state.State import State
from BS_App.components.card_stats import card_stats
from BS_App.style.colors import Color
from BS_App.style import style
from BS_App.style.style import Spacing, Size
from BS_App.style.colors import Color

def profile() -> rx.Component:
    return rx.cond(
        State.is_visible,
            rx.vstack(
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.avatar(src=State.url_icon_player, fallback="RX", size="8"),
                            rx.chakra.span(
                                f'{State.player_info["tag"]}',
                                color=Color.ACCENT.value,
                                font_size=Size.DEFAULT.value,
                            ),
                            spacing=Spacing.ZERO.value
                        ),
                        rx.vstack(
                            rx.text(
                                f'{State.player_info["name"]}',
                                font_size=Size.MEDIUM_BIG.value,
                                
                            ),
                            rx.vstack(

                                rx.hstack(
                                    rx.image(src=f"/trophy.png", width=Size.MEDIUM.value, height=Size.MEDIUM.value),
                                    rx.chakra.span(
                                        f'{State.player_info["trophies"]}',
                                        font_size=Size.DEFAULT.value,
                                    ),
                                    spacing=Spacing.VERY_SMALL.value,
                                ),
                                rx.hstack(
                                    rx.image(src=f"/Info.webp", width=Size.MEDIUM.value, height=Size.MEDIUM.value),
                                    rx.chakra.span(
                                        f'EXP: {State.player_info["expLevel"]}',
                                        font_size=Size.DEFAULT.value,
                                    ),
                                    spacing=Spacing.VERY_SMALL.value,
                                ),
                                spacing=Spacing.VERY_SMALL.value
                            ),
                            spacing=Spacing.ZERO.value,

                        ),
                    ),

                    rx.flex(
                        
                        card_stats("MÁXIMO DE TROFEOS", "highestTrophies", "Ranking.webp"),
                        card_stats("VICTORIAS 3 VS 3", "3vs3Victories", "3v3.png"),
                        card_stats("VICTORIAS EN SOLITARIO", "soloVictories","Showdown.webp"),
                        card_stats("VICTORIAS EN DÚO", "duoVictories","Duo-Showdown.webp"),

                        align="center", 
                        justify="center",
                        spacing="2",

                    ),
                    bg=Color.WHITE.value,
                    border_radius=Size.SMALL.value,
                    padding=10,
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                    align_items="center",  # Alinea los elementos horizontalmente al centro
                ),




                
                rx.vstack(
                    rx.vstack(
                        rx.heading(f'BRAWLERS', size="4",font_family= "Lilita One",font_weight="300",),
                        align="center",
                        height="100%", 
                        width="100%", 
                    ),
 
                    # width="100%",
                    # height= "350%",
                    bg=Color.WHITE.value,
                    border_radius="15px",
                    padding=10,
                    margin=10,
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",

                ),

                width="100%",
                height= "100%",
                direction="column",
                align="center",
                # justify="center",

                # bg="red",
                max_width=style.MAX_WIDTH,
                # spacing=2,
            ),
            rx.cond(
                State.message_user_void,
                # message("Error con la api"),
                rx.box(
                    rx.heading('Jugador no existe', size="6",font_family= "Lilita One",font_weight="300",),
                    bg="#E6B0AA",
                    border_radius="10px",
                    width="30%",
                    margin="100px",
                    padding="20px",
                    text_align="center",
                    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",

                ),
            ),
        )