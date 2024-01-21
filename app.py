from google.oauth2.credentials import Credentials
from typing import Optional

def main(
    credentials:Optional[Credentials]=None):

    from dash import Dash, clientside_callback
    from portfolio.container.layout import layout_mantine_provider
    from portfolio.container.callbacks import container_callbacks
    from portfolio.pages.home.callbacks import home_callbacks
    from portfolio.pages.about.callbacks import about_callbacks
    from portfolio.pages.blog.callbacks import blog_callbacks
    # Initialize Dash App Layout and Server
    app = Dash(
        __name__,
        title='Portfolio',
        suppress_callback_exceptions=True,
        eager_loading=True,
        external_stylesheets=[
            "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
        ]
    )
    server = app.server
    app.layout = layout_mantine_provider
    # Initialize Dash App Callbacks
    container_callbacks(app)
    home_callbacks(app)
    about_callbacks(app)
    blog_callbacks(app,credentials)
    return app, server