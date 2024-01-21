from dash import Dash, clientside_callback, Input, Output, State, callback_context


def container_callbacks(app:Dash):

    clientside_callback(
        """(wBreakpoint, w) => {
            console.log("Only updating when crossing the threshold")
            return `${wBreakpoint},${w}`
        }""",
        Output("display", "children"),
        Input("breakpoints", "widthBreakpoint"),
        State("breakpoints", "width")
    )

    @app.callback(
        Output("container-wide-menu","style"),
        Output("container-long-menu","style"),
        Input("display", "children"))
    def _container_navbar_resize_from_display_callback(
        display:str):
        """Resize navbar based on size of user window"""
        from portfolio.container.utils import navbar_resize_from_display
        callback = navbar_resize_from_display(display)
        return callback
    
    @app.callback(
        Output("container-navbar-menu-col","span"),
        Output("container-navbar-title-col","span"),
        Output("container-navbar-icon-col","span"),
        Input("display", "children"))
    def _container_navbar_resize_span_from_display_callback(
        display:str):
        """Resize navbar based on size of user window"""
        from portfolio.container.utils import navbar_resize_span_from_display
        callback = navbar_resize_span_from_display(display)
        return callback
    
    @app.callback(
        Output("container-navbar-title","children"),
        Input("display", "children"))
    def _container_navbar_resize_title_from_display_callback(
        display:str):
        """Resize navbar based on size of user window"""
        from portfolio.container.utils import navbar_resize_title_from_display
        callback = navbar_resize_title_from_display(display)
        return callback
    

    @app.callback(
        Output("portfolio-container","children"),
        Output("portfolio-blog-tag-store","data"),
        Input("container-home-menu-item", "n_clicks"),
        Input("container-home-menu-button", "n_clicks"),
        Input("container-blog-menu-item", "n_clicks"),
        Input("container-blog-menu-button", "n_clicks"),
        Input("container-about-menu-item", "n_clicks"),
        Input("container-about-menu-button", "n_clicks"),
        Input("portfolio-about-protein-modeling-store","data"),
        Input("portfolio-about-cheminformatics-store","data"),
        Input("portfolio-about-omics-store","data"),
        Input("portfolio-about-machine-learning-store","data"),
        Input("portfolio-about-web-app-store","data"),
        prevent_initial_call=True)
    def _container_container_content_from_display_callback(
        home_menu:int,
        home_button:int,
        blog_menu:int,
        blog_button:int,
        about_menu:int,
        about_button:int,
        model_button:int,
        chem_button:int,
        omics_button:int,
        ml_button:int,
        wad_button:int):
        context = callback_context.triggered[0]['prop_id'].split('.')[0]

        from portfolio.container.utils import container_content_from_display
        callback = container_content_from_display(context)
        return callback
    
    @app.callback(
        Output("portfolio-context-store-div","children"),
        Input("container-home-menu-item", "n_clicks"),
        Input("container-home-menu-button", "n_clicks"),
        Input("container-blog-menu-item", "n_clicks"),
        Input("container-blog-menu-button", "n_clicks"),
        Input("container-about-menu-item", "n_clicks"),
        Input("container-about-menu-button", "n_clicks"),
        Input("portfolio-about-protein-modeling-store","data"),
        Input("portfolio-about-cheminformatics-store","data"),
        Input("portfolio-about-omics-store","data"),
        Input("portfolio-about-machine-learning-store","data"),
        Input("portfolio-about-web-app-store","data"),
        prevent_initial_call=True)
    def _container_temporary_store_from_display_callback(
        home_menu:int,
        home_button:int,
        blog_menu:int,
        blog_button:int,
        about_menu:int,
        about_button:int,
        model_button:int,
        chem_button:int,
        omics_button:int,
        ml_button:int,
        wad_button:int):
        context = callback_context.triggered[0]['prop_id'].split('.')[0]

        from portfolio.container.utils import temporary_store_from_display
        callback = temporary_store_from_display(context)
        return callback
    
    return