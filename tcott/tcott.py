"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from tcott import styles
from tcott.pages import *

import reflex as rx  # upm package(reflex)



app = rx.App(overlay_component=None, style=styles.base_style)
app.compile()
