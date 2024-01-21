from dash import Dash, clientside_callback, Input, Output, State

def home_callbacks(app:Dash):
    
    @app.callback(
        Output("home-protein-model-graphic-col","span"),
        Output("home-cheminformatics-graphic-col","span"),
        Output("home-omics-graphic-col","span"),
        Output("home-machine-learning-graphic-col","span"),
        Output("home-web-app-graphic-col","span"),
        Input("display", "children"))
    def _home_column_resize_from_display_callback(
        display:str):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.home.utils import column_resize_from_display
        callback = column_resize_from_display(display)
        return callback
    

    @app.callback(
        Output("portfolio-about-protein-modeling-store","data"),
        Input("home-protein-model-graphic-button", "n_clicks"),
        prevent_initial_call=True)
    def _hero_protein_tag_from_click_callback(
        click:str):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.home.utils import tag_from_click
        callback = tag_from_click()
        return callback
    

    @app.callback(
        Output("portfolio-about-cheminformatics-store","data"),
        Input("home-cheminformatics-graphic-button", "n_clicks"),
        prevent_initial_call=True)
    def _hero_cheminformatics_tag_from_click_callback(
        click:str):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.home.utils import tag_from_click
        callback = tag_from_click()
        return callback


    @app.callback(
        Output("portfolio-about-omics-store","data"),
        Input("home-omics-graphic-button", "n_clicks"),
        prevent_initial_call=True)
    def _hero_omics_tag_from_click_callback(
        click:str):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.home.utils import tag_from_click
        callback = tag_from_click()
        return callback


    @app.callback(
        Output("portfolio-about-machine-learning-store","data"),
        Input("home-machine-learning-graphic-button", "n_clicks"),
        prevent_initial_call=True)
    def _hero_ml_tag_from_click_callback(
        click:str):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.home.utils import tag_from_click
        callback = tag_from_click()
        return callback


    @app.callback(
        Output("portfolio-about-web-app-store","data"),
        Input("home-web-app-graphic-button", "n_clicks"),
        prevent_initial_call=True)
    def _hero_webapp_tag_from_click_callback(
        click:str):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.home.utils import tag_from_click
        callback = tag_from_click()
        return callback
    
    return