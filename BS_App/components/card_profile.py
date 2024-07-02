import reflex as rx
from BS_App.state.State import State
from BS_App.components.card_stats_profile import card_stats_profile
from BS_App.components.card_data_profile import card_data_profile
from BS_App.style.style import Spacing, Size, box_style
from BS_App.style.colors import TextColor


def card_profile() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.vstack(
                rx.avatar(
                    src=State.info_player.icon,
                    fallback="RX",
                    size="8"
                ),
                rx.text(
                    f'{State.info_player.tag}',
                    color=TextColor.TERTIARY.value,
                    font_size=Size.DEFAULT.value,
                    as_="span"
                ),
                spacing=Spacing.ZERO.value
            ),
            rx.vstack(
                rx.text(
                    f'{State.info_player.name}',
                    font_size=Size.MEDIUM_BIG.value,

                ),
                rx.vstack(
                    card_data_profile(
                        "/trophy.png", f'{State.info_player.trophies}'),
                    card_data_profile(
                        "/Info.webp", f'EXP: {State.info_player.expLevel}'),

                    rx.cond(
                        State.info_player.clubName != "",
                        card_data_profile(
                            "/Club.webp", f'{State.info_player.clubName}'),
                        card_data_profile("/NoClub.webp", "Sin Club")
                    ),

                    spacing=Spacing.VERY_SMALL.value
                ),
                spacing=Spacing.ZERO.value,

            ),
        ),

        rx.flex(

            card_stats_profile(
                "MÁXIMO DE TROFEOS", State.info_player.highestTrophies, "Ranking.webp"),
            card_stats_profile("VICTORIAS 3 VS 3",
                               State.info_player.Victories3vs3, "3v3.png"),
            card_stats_profile(
                "VICTORIAS EN SOLITARIO", State.info_player.SoloVictories, "Showdown.webp"),
            card_stats_profile(
                "VICTORIAS EN DÚO", State.info_player.DuoVictories, "Duo-Showdown.webp"),

            align="center",
            justify="center",
            spacing="2",

        ),
        style=box_style,
        align_items="center",  # Alinea los elementos horizontalmente al centro
    ),
