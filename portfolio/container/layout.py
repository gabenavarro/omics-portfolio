from dash_mantine_components import MantineProvider
from portfolio.container.html import (
    navbar_div,
    main_container,
    store_div,
    breakpoints_div
)


theme = {
    "colorScheme": "light",
    "fontFamily": "'Inter', sans-serif",
    "primaryColor": "gray",
}


layout_mantine_provider = MantineProvider(
    theme=theme,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        navbar_div,
        main_container,
        store_div,
        breakpoints_div
    ],
    id="portfolio-mantine-provider"
)
