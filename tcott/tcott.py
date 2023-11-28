"""tcott moment"""
# from rxconfig import config

import reflex as rx


from tcott import style


class State(rx.State):
    """The app state."""

    img_names = [
        "centerpiece",
        "frame01",
        "frame02",
        "frame03",
        "frame04",
        "frame05",
        "frame06",
        "frame07",
    ]

    current_index: int = 0

    def next_image(self) -> None:
        """Go to the next image."""
        self.current_index += 1
        if self.current_index >= len(self.img_names):
            self.current_index = 0

    def prev_image(self) -> None:
        """Go to the previous image."""
        self.current_index -= 1
        if self.current_index < 0:
            self.current_index = len(self.img_names) - 1

    @rx.var
    def get_image(self):
        """Get the current image."""
        return f"frames/{self.img_names[self.current_index]}.png"


@rx.page(route="/", title="T.C.O.T.T.")
def index() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            # rx.hstack(
            #     rx.icon_button(
            #         icon=rx.icon(tag="chevron_up"),
            #         size="2em",
            #         **style.ARROW_BUTTONS,
            #     ),
            # ),
            rx.hstack(
                rx.icon_button(
                    icon=rx.icon(tag="chevron_left"),
                    size="3em",
                    **style.ARROW_BUTTONS,
                    on_click=State.prev_image,
                ),
                rx.container(
                    rx.image(
                        src=State.get_image,
                    ),
                    contain="layout",
                    width="75vw",
                    height="60vh",
                    center_content=True,
                    justify_content="center",
                ),
                rx.icon_button(
                    icon=rx.icon(tag="chevron_right"),
                    size="3em",
                    **style.ARROW_BUTTONS,
                    on_click=State.next_image,
                ),
                justify_content="space-between",
                align_items="center",
                width="90vw",
                height="90%",
            ),
            # rx.hstack(
            #     rx.icon_button(
            #         icon=rx.icon(tag="chevron_down"),
            #         size="2em",
            #         **style.ARROW_BUTTONS,
            #     ),
            # ),
            height="92%",
            align_items="center",
            justify_content="center",
            padding="1.5em",
        ),
        rx.hstack(
            rx.image(
                src="/dmcl.png",
                left="1em",
                **style.LOGO_STYLE,
            ),
            rx.spacer(),
            rx.image(
                src="/cv.png",
                right="0.75em",
                **style.LOGO_STYLE,
            ),
            padding="0.5em",
            spacing="2.25em",
            height="8%",
            position="fixed",
            left="0px",
            bottom="0px",
            right="0px",
            background_color="hsl(300, 13%, 55%, 0.69)",
            backdrop_filter="blur(4px)",
        ),
        padding="1.5em",
        position="fixed",
        **style.STICKY_EDGES,
        id="page",
    )


# Add state and page to the app.
app = rx.App(overlay_component=None, style=style.APP_STYLE)
app.compile()
