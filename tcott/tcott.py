"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


@rx.page(route="/", title="TCOTT")
def index() -> rx.Component:
    return rx.box(
        rx.container(
            rx.vstack(
                rx.image(
                    src="centerpiece.png",
                    # box_shadow="0px 0px 20px 0px rgba(0,0,0,0.69)",
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
                height="3em",
                mix_blend_mode="hard-light",
                margin="1em",
            ),
            rx.spacer(),
            rx.image(
                src="/cv.png",
                width="auto",
                height="2em",
                mix_blend_mode="hard-light",
                position="relative",
                margin="1em",
            ),
            padding="0.5em",
            position="fixed",
            left="0px",
            bottom="-0.5em",
            right="0px",
            background_color="hsl(300, 13%, 55%, 0.69)",
            backdrop_filter="blur(4px)",
        ),
        # width="100vw",
        # height="100vh",
        # border="2px dashed white",
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
app = rx.App()
app.compile()
