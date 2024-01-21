from dash import Dash, clientside_callback, Input, Output, State, callback_context
from google.oauth2.credentials import Credentials
from portfolio.library.config import blog_snippets
from typing import List, Dict, Optional

def blog_callbacks(
    app:Dash,
    credentials:Optional[Credentials]=None):
    
    # @app.callback(
    #     Output("about-summary-portrait-col","span"),
    #     Output("about-summary-text-col","span"),
    #     Output("about-workhistory-stepper-col","span"),
    #     Output("about-workhistory-stepper","orientation"),
    #     Output("about-workhistory-text-col","span"),
    #     Output("about-workhistory-image-col","span"),
    #     Input("display", "children"))
    # def _about_column_resize_from_display_callback(
    #     display:str):
    #     """Resize hero page column span based on size of user window"""
    #     from portfolio.pages.about.utils import column_resize_from_display
    #     callback = column_resize_from_display(display)
    #     return callback

    @app.callback(
        Output("blog-article-count-store","data"),
        Input("blog-article-navigation-backward-actionicon","data"),
        Input("blog-article-navigation-forward-actionicon","data"),
        State("blog-article-count-store","data"),
        prevent_initial_call=True)
    def _blog_navigation_count_from_clicks_callback(
        backward:str,
        forward:str,
        count:int):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import navigation_count_from_clicks
        context = callback_context.triggered[0]['prop_id'].split('.')[0]
        callback = navigation_count_from_clicks(context,count)
        return callback


    @app.callback(
        Output("blog-tag-segmented-control","value"),
        Input("portfolio-blog-tag-store","data"))
    def _blog_tag_value_from_store_callback(
        tag:str):
        """Blog tag filter"""
        from portfolio.pages.blog.utils import tag_value_from_store
        callback = tag_value_from_store(tag)
        return callback    
    

    @app.callback(
        Output("portfolio-blog-article-store","data"),
        Input("blog-tag-segmented-control","value"),
        Input("blog-article-count-store","data"),
        prevent_initial_call=True)
    def _blog_article_data_from_tag_value_callback(
        tag:str,
        offset:int):
        """Retrieve blog articles with tag filter"""
        from portfolio.pages.blog.utils import article_data_from_tag_value
        callback = article_data_from_tag_value(tag,offset,credentials)
        return callback
    

    @app.callback(
        [Output(f"blog-controller-{index}-store","data") for index in blog_snippets],
        Input("portfolio-blog-article-store","data"))
    def _blog_controller_store_from_article_data_callback(
        data:List[Dict[str,str]]):
        """Distribute articles to individual cards"""
        from portfolio.pages.blog.utils import controller_store_from_article_data
        callback = controller_store_from_article_data(data)
        return callback


    @app.callback(
        Output("blog-card-one-button","children"),
        Output("blog-card-one-button","disabled"),
        Input("blog-controller-one-store","data"))
    def _blog_blog_card_one_from_controller_one_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback

    @app.callback(
        Output("blog-card-two-button","children"),
        Output("blog-card-two-button","disabled"),
        Input("blog-controller-two-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_two_from_controller_two_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    

    @app.callback(
        Output("blog-card-three-button","children"),
        Output("blog-card-three-button","disabled"),
        Input("blog-controller-three-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_three_from_controller_three_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    
    @app.callback(
        Output("blog-card-four-button","children"),
        Output("blog-card-four-button","disabled"),
        Input("blog-controller-four-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_four_from_controller_four_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    
    @app.callback(
        Output("blog-card-five-button","children"),
        Output("blog-card-five-button","disabled"),
        Input("blog-controller-five-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_five_from_controller_five_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    
    @app.callback(
        Output("blog-card-six-button","children"),
        Output("blog-card-six-button","disabled"),
        Input("blog-controller-six-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_six_from_controller_six_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    
    @app.callback(
        Output("blog-card-seven-button","children"),
        Output("blog-card-seven-button","disabled"),
        Input("blog-controller-seven-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_seven_from_controller_seven_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    
    @app.callback(
        Output("blog-card-eight-button","children"),
        Output("blog-card-eight-button","disabled"),
        Input("blog-controller-eight-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_eight_from_controller_eight_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    
    @app.callback(
        Output("blog-card-nine-button","children"),
        Output("blog-card-nine-button","disabled"),
        Input("blog-controller-nine-store","data"),
        prevent_initial_call=True)
    def _blog_blog_card_nine_from_controller_nine_callback(
        tag:str):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_card_from_controller_data
        callback = blog_card_from_controller_data(tag)
        return callback
    
    @app.callback(
        [Output(f"blog-card-{index}-button-store","data") for index in blog_snippets],
        [Input(f"blog-card-{index}-button","n_clicks") for index in blog_snippets],
        prevent_initial_call=True)
    def _blog_abstract_layout_store_from_clicks_callback(
        card_one_button:int,
        card_two_button:int,
        card_three_button:int,
        card_four_button:int,
        card_five_button:int,
        card_six_button:int,
        card_seven_button:int,
        card_eight_button:int,
        card_nine_button:int):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import abstract_layout_store_from_clicks
        context = callback_context.triggered[0]['prop_id'].split('.')[0]
        callback = abstract_layout_store_from_clicks(context)
        return callback
    
    @app.callback(
        Output("blog-article-exit-store","data"),
        Input("blog-article-exit-actionicon","n_clicks"),
        prevent_initial_call=True)
    def _blog_article_layout_store_from_clicks_callback(
        exit_button:int):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import article_layout_store_from_clicks
        context = callback_context.triggered[0]['prop_id'].split('.')[0]
        callback = article_layout_store_from_clicks(context)
        return callback
    

    @app.callback(
        Output("blog-title-div","style"),
        Output("blog-segmented-control-div","style"),
        Output("blog-simple-grid","style"),
        Output("blog-navigation-button-group","style"),
        Output("blog-article-div","children"),
        Output("blog-article-exit-actionicon","style"),
        Input("blog-article-exit-store","data"),
        Input("blog-tag-segmented-control","value"),
        [Input(f"blog-card-{index}-button-store","data") for index in blog_snippets],
        [State(f"blog-controller-{index}-store","data") for index in blog_snippets],
        prevent_initial_call=True)
    def _blog_layout_from_selection_callback(
        exit_button:int,
        segment_control:str,
        card_one_button:int,
        card_two_button:int,
        card_three_button:int,
        card_four_button:int,
        card_five_button:int,
        card_six_button:int,
        card_seven_button:int,
        card_eight_button:int,
        card_nine_button:int,
        controller_one_store:Dict[str,str],
        controller_two_store:Dict[str,str],
        controller_three_store:Dict[str,str],
        controller_four_store:Dict[str,str],
        controller_five_store:Dict[str,str],
        controller_six_store:Dict[str,str],
        controller_seven_store:Dict[str,str],
        controller_eight_store:Dict[str,str],
        controller_nine_store:Dict[str,str]):
        """Card content from controller data"""
        from portfolio.pages.blog.utils import blog_layout_from_selection
        context = callback_context.triggered[0]['prop_id'].split('.')[0]
        callback = blog_layout_from_selection(
            context,
            card_one_button,
            card_two_button,
            card_three_button,
            card_four_button,
            card_five_button,
            card_six_button,
            card_seven_button,
            card_eight_button,
            card_nine_button,
            controller_one_store,
            controller_two_store,
            controller_three_store,
            controller_four_store,
            controller_five_store,
            controller_six_store,
            controller_seven_store,
            controller_eight_store,
            controller_nine_store,
        )
        return callback
    