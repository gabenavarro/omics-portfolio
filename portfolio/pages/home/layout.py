from dash.html import Div
from dash_mantine_components import Container
from portfolio.pages.home.html import (
    homepage_text_grid,
    homepage_graphic_grid
)

homepage_layout = Div(
    children=[
        homepage_text_grid,
        homepage_graphic_grid
    ]
)