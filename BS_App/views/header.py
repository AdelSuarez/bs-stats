import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
            rx.heading(
                "Estadisticas BS",
                size="9",
                font_family= "Lilita One",
                font_weight="300",
                margin="20px"
            ),
            rx.divider(width="90%"),
            
            align="center",
            width="100%",
        )