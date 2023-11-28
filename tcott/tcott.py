"""tcott moment"""
# from rxconfig import config

import reflex as rx

class State(rx.State):
    """The app state."""

    pass


@rx.page(route="/", title="T.C.O.T.T.")
def index() -> rx.Component:
    return rx.box(
        rx.container(
            rx.vstack(
                rx.image(
                    src="centerpiece.png",
                    width="auto",
                    height="66vh",
                ),
            ),
            center_content=True,
            position="relative",
            top="0px",
            left="0px",
            bottom="0px",
            right="0px",
        ),
        rx.hstack(
            rx.image(
                src="/dmcl.png",
                width="auto",
                height="6vh",
                mix_blend_mode="hard-light",
                position="relative",
                margin="1em",
            ),
            rx.spacer(),
            rx.image(
                src="/cv.png",
                width="auto",
                height="3vh",
                mix_blend_mode="hard-light",
                position="relative",
                right="1em",
            ),
            padding="0.5em",
            position="fixed",
            left="0px",
            bottom="-0.5em",
            right="0px",
            background_color="hsl(300, 13%, 55%, 0.69)",
            backdrop_filter="blur(4px)",
        ),
        background_image="url('purple_bricks.png')",
        background_repeat="repeat",
        padding="2.5em",
        position="fixed",
        top="0px",
        left="0px",
        bottom="0px",
        right="0px",
    )


# Add state and page to the app.
app = rx.App(overlay_component=None)
app.compile()
