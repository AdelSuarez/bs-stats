import reflex as rx
from BS_App.state.State import State
from BS_App.components.card_stats import card_stats
from BS_App.components.stats_profile import stats_profile
from BS_App.style.colors import Color
from BS_App.style import style
from BS_App.style.style import Spacing, Size, BOX_SHADOW
from BS_App.style.colors import Color, TextColor

def profile() -> rx.Component:
    return rx.cond(
        State.info_player.is_visible,
            rx.vstack(
                rx.vstack(
                    rx.hstack(
                        rx.vstack(
                            rx.avatar(
                                src=State.info_player.icon, 
                                fallback="RX", 
                                size="8"
                            ),
                            rx.chakra.span(
                                f'{State.info_player.tag}',
                                color=TextColor.TERTIARY.value,
                                font_size=Size.DEFAULT.value,
                            ),
                            spacing=Spacing.ZERO.value
                        ),
                        rx.vstack(
                            rx.text(
                                f'{State.info_player.name}',
                                font_size=Size.MEDIUM_BIG.value,
                                
                            ),
                            rx.vstack(
                                stats_profile("/trophy.png",f'{State.info_player.trophies}'),
                                stats_profile("/Info.webp", f'EXP: {State.info_player.expLevel}'),
                                stats_profile("/Club.webp", f'{State.info_player.clubName}'),

                                spacing=Spacing.VERY_SMALL.value
                            ),
                            spacing=Spacing.ZERO.value,

                        ),
                    ),

                    rx.flex(
                        
                        card_stats("MÁXIMO DE TROFEOS", State.info_player.highestTrophies, "Ranking.webp"),
                        card_stats("VICTORIAS 3 VS 3", State.info_player.Victories3vs3, "3v3.png"),
                        card_stats("VICTORIAS EN SOLITARIO", State.info_player.SoloVictories,"Showdown.webp"),
                        card_stats("VICTORIAS EN DÚO", State.info_player.DuoVictories,"Duo-Showdown.webp"),

                        align="center", 
                        justify="center",
                        spacing="2",

                    ),
                    bg=Color.WHITE.value,
                    border_radius=Size.SMALL.value,
                    padding=Size.SMALL.value,
                    box_shadow=BOX_SHADOW,
                    align_items="center",  # Alinea los elementos horizontalmente al centro
                ),

                rx.vstack(
                    rx.vstack(
                        rx.text(f'BRAWLERS'),
                        align="center",
                        height="100%", 
                        width="100%", 
                    ),
 
                    bg=Color.WHITE.value,
                    border_radius=Size.SMALL.value,
                    padding=10,
                    margin=10,
                    box_shadow=BOX_SHADOW,

                ),

                width="100%",
                height= "100%",
                direction="column",
                align="center",
                max_width=style.MAX_WIDTH,
            ),
            rx.cond(
                State.message_user_void,
                # message("Error con la api"),
                # message("Error con la api"),

                rx.box(
                    rx.heading('Jugador no existe', size="6",font_family= "Lilita One",font_weight="300",),
                    bg="#E6B0AA",
                    border_radius="10px",
                    width="30%",
                    margin="100px",
                    padding="20px",
                    text_align="center",
                    box_shadow=BOX_SHADOW,

                ),
            ),
        )