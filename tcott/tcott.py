"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx  # upm package(reflex)

from tcott import styles
from tcott.pages import *  # noqa

app = rx.App(overlay_component=None, style=styles.base_style)
app.compile()
