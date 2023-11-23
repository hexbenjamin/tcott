"""The home page."""

import reflex as rx  # upm package(reflex)

from tcott.templates import template


@template(route="/", title="tcott")
def index() -> rx.Component:
    """The settings page.

    Returns:
        The UI for the settings page.
    """
    return rx.vstack(
        rx.heading("TCOTT", font_size="3em"),
        rx.text("the trees! they be changin'!"),
        rx.text(
            "You can edit this page in ",
            rx.code("tcott/pages/index.py"),
        ),
    )