from dash.html import Div
from portfolio.pages.about.html import (
    summary_grid,
    work_history_grid,
    publication_grid
)

about_layout = Div(
    children=[
        summary_grid,
        work_history_grid,
        publication_grid
    ]
)