import reflex as rx

def message(text: str) -> rx.Component:
    return rx.box(
                rx.text(
                    text, 
                    size="6",
                    font_family= "Lilita One",
                    font_weight="300",
                ),
                bg="#E6B0AA",
                border_radius="10px",
                width="30%",
                margin="100px",
                padding="20px",
                text_align="center",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",

            )