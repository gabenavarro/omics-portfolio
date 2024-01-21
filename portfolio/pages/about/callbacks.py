from dash import Dash, clientside_callback, Input, Output, State, callback_context

def about_callbacks(app:Dash):
    
    @app.callback(
        Output("about-summary-portrait-col","span"),
        Output("about-summary-text-col","span"),
        Output("about-workhistory-stepper-col","span"),
        Output("about-workhistory-stepper","orientation"),
        Output("about-workhistory-text-col","span"),
        Output("about-workhistory-image-col","span"),
        Input("display", "children"))
    def _about_column_resize_from_display_callback(
        display:str):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.about.utils import column_resize_from_display
        callback = column_resize_from_display(display)
        return callback


    @app.callback(
        Output("about-workhistory-stepper","active"),
        Output("about-workhistory-text-div","children"),
        Output("about-workhistory-image","src"),
        Input("about-workhistory-backward-actionicon","n_clicks"),
        Input("about-workhistory-forward-actionicon","n_clicks"),
        State("about-workhistory-stepper","active"),
        prevent_initial_call=True)
    def _about_stepper_content_from_click_callback(
        backward_click:int,
        forward_click:int,
        stepper:int):
        """Resize hero page column span based on size of user window"""
        from portfolio.pages.about.utils import stepper_content_from_click
        context = callback_context.triggered[0]['prop_id'].split('.')[0]
        callback = stepper_content_from_click(stepper,context)
        return callback
