from google.oauth2.credentials import Credentials
from typing import List, Dict, Optional

def tag_value_from_store(
    tag_store:str):

    if tag_store == "protein-model":
        tag_value = "modeling"
    elif tag_store == "cheminformatics":
        tag_value = "cheminformatics"
    elif tag_store == "omics":
        tag_value = "omics"
    elif tag_store == "machine-learning":
        tag_value = "ml"
    elif tag_store == "devops":
        tag_value = "devops"
    else:
        tag_value = "all"

    callback = (
        tag_value
    )
    return callback


def navigation_count_from_clicks(
    context:str,
    count:int):

    from dash import no_update

    placeholder = count
    if context == "blog-article-navigation-forward-actionicon":
        count += 1
    if context == "blog-article-navigation-backward-actionicon":
        count -= 0
    
    if count < 0:
        count = 0

    if placeholder == count:
        count = no_update
    
    callback = (
        count
    )
    return callback


def article_data_from_tag_value(
    tag:str,
    offset:int,
    credentials:Optional[Credentials]=None):

    from portfolio.library.connect import table_from_bigquery
    from portfolio.library.json import BQ_CONFIG, QUERY_TAG_KEY


    if tag == "all":
        query = """
        SELECT blog_title, blog_date, blog_abstract, blog_markdown, blog_image, blog_image_source, tag_id
        FROM `%s.%s.%s`
        ORDER BY `%s` DESC
        LIMIT 9 OFFSET %s
        """%(
            BQ_CONFIG['portfolio-project-id'],
            BQ_CONFIG['portfolio-dataset-id'],
            BQ_CONFIG['portfolio-blog-table-id'],
            "blog_date",
            offset * 9
        )
    else:
        query = """
        SELECT blog_title, blog_date, blog_abstract, blog_markdown, blog_image, blog_image_source, tag_id
        FROM `%s.%s.%s`
        WHERE tag_id IN (%s)
        ORDER BY `%s` DESC
        LIMIT 9 OFFSET %s
        """%(
            BQ_CONFIG['portfolio-project-id'],
            BQ_CONFIG['portfolio-dataset-id'],
            BQ_CONFIG['portfolio-blog-table-id'],
            ",".join([str(i) for i in QUERY_TAG_KEY[tag]]),
            "blog_date",
            offset * 9
        )
        
    article_data = table_from_bigquery(query,credentials).to_dict('records')
    callback = (
        article_data
    )

    return callback


def controller_store_from_article_data(
    article_data:List[Dict[str,str]]):

    from portfolio.library.config import blog_snippets
    from dash.exceptions import PreventUpdate

    if article_data is not None:
        callback = [[] for _ in range(len(blog_snippets))]
        for index, article in enumerate(article_data):
            callback[index] = article
    else:
        raise PreventUpdate
    
    return callback


def blog_card_from_controller_data(
    controller_data:Dict[str,str]):

    from datetime import datetime
    from portfolio.library.json import TAG_KEY
    from dash_mantine_components import (
        Badge, 
        Text,
        Image,
        Card,
        Group
    )

    disabled = True
    children = []
    if controller_data:
        src = controller_data['blog_image']
        title = controller_data['blog_title']
        badges = [Badge(i) for i in TAG_KEY[str(controller_data['tag_id'])]]
        date = datetime.strptime(controller_data['blog_date'], '%Y-%m-%dT%H:%M:%S').strftime('%B %d, %Y')
        abstract = controller_data['blog_abstract']

        disabled = False
        children = Card(
            [
                Image(
                    src=src,
                    height=160,
                    radius="md",
                ),
                Text(
                    title,
                    weight=750,
                    style={
                        "width":325,
                        "text-wrap": "pretty"
                    }
                ),
                Group(
                    children=badges,
                    position="apart",
                    mt="md",
                    mb="xs",
                ),
                Text(
                    children=[date],
                    weight=750,
                    size="sm",
                    color="dimmed",
                ),
                Text(
                    children=[abstract],
                    size="sm",
                    weight=350,
                    # color="dimmed",
                    style={
                        "width":300,
                        "text-wrap": "pretty",
                    }
                )
            ],
            withBorder=False,
            radius="md",
            style={"width": 350},
        )
        

    callback = (
        children,
        disabled
    )
    return callback


def abstract_layout_store_from_clicks(
    context:str):

    from portfolio.library.config import blog_snippets

    blog_buttons = [f"blog-card-{index}-button" for index in blog_snippets]
    callback = [True if context == i else False for i in blog_buttons]

    return callback


def article_layout_store_from_clicks(
    context:str):

    from dash import no_update
    callback = [no_update]
    if context == "blog-article-exit-actionicon":
        callback[0] = "on"

    return callback


def blog_layout_from_selection(
    context:str,
    card_one_button:bool,
    card_two_button:bool,
    card_three_button:bool,
    card_four_button:bool,
    card_five_button:bool,
    card_six_button:bool,
    card_seven_button:bool,
    card_eight_button:bool,
    card_nine_button:bool,
    controller_one_store:Dict[str,str],
    controller_two_store:Dict[str,str],
    controller_three_store:Dict[str,str],
    controller_four_store:Dict[str,str],
    controller_five_store:Dict[str,str],
    controller_six_store:Dict[str,str],
    controller_seven_store:Dict[str,str],
    controller_eight_store:Dict[str,str],
    controller_nine_store:Dict[str,str]):

    import logging
    from dash.exceptions import PreventUpdate
    from dash_mantine_components import Image, Stack
    from portfolio.library.config import (
        blog_max_width,
        simple_hide_style,
        simple_show_style
    )
    from portfolio.library.blog import (
        blog_section_from_markdown_string, 
        blog_div_from_blog_sections
    )

    if context in ["blog-article-exit-store","blog-tag-segmented-control"]:
        callback = (
            simple_show_style,
            simple_show_style,
            simple_show_style,
            simple_show_style,
            [],
            simple_hide_style
        )
    else:
        controller_data = None
        if card_one_button:
            controller_data = controller_one_store
        elif card_two_button:
            controller_data = controller_two_store
        elif card_three_button:
            controller_data = controller_three_store
        elif card_four_button:
            controller_data = controller_four_store
        elif card_five_button:
            controller_data = controller_five_store
        elif card_six_button:
            controller_data = controller_six_store
        elif card_seven_button:
            controller_data = controller_seven_store
        elif card_eight_button:
            controller_data = controller_eight_store
        elif card_nine_button:
            controller_data = controller_nine_store
        else:
            logging.info(
                """blog_layout_from_selection
                ---
                context: %s
                controller_data: %s
                """%(
                    context,
                    controller_data
                )
            )
            raise PreventUpdate

        if controller_data:
            src = controller_data['blog_image']
            markdown = controller_data['blog_markdown']
            sections = blog_section_from_markdown_string(markdown)
            divs = blog_div_from_blog_sections(sections)
            image = Image(
                src=src,
                height=250,
                width="100%",
                radius="md",
                className="fadeOut"
            )
            children=[image] + divs
            artile_stack = Stack(
                children=children,
                maw=blog_max_width
            )
            callback = (
                simple_hide_style,
                simple_hide_style,
                simple_hide_style,
                simple_hide_style,
                artile_stack,
                simple_show_style
            )
        else:
            raise PreventUpdate

    return callback