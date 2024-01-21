def navbar_resize_from_display(
    display:str):

    display_width = display.split(",")[0]
    hidden={"display":"None"}
    visible={}
    if display_width in ["md","lg"]:
        callback = (
            visible,
            hidden
        )
    else:
        callback = (
            hidden,
            visible
        )
    return callback


def navbar_resize_span_from_display(
    display:str):

    display_width = display.split(",")[0]
    if display_width in ["md","lg"]:
        callback = (
            4,4,4
        )
    else:
        callback = (
            3,6,3
        )
    return callback


def navbar_resize_title_from_display(
    display:str):

    display_width = display.split(",")[0]
    if display_width in ["md","lg"]:
        callback = (
            "Gabriel Navarro, PhD"
        )
    else:
        callback = (
            "Navarro, PhD"
        )
    return callback



def container_content_from_display(
    context:str):

    from dash import no_update
    from portfolio.pages.home.layout import homepage_layout
    from portfolio.pages.about.layout import about_layout
    from portfolio.pages.blog.layout import blog_layout

    tag_store = "all"
    if context in ["container-home-menu-item","container-home-menu-button"]:
        container = homepage_layout
    elif context in ["container-about-menu-item","container-about-menu-button"]:
        container = about_layout
    elif context in ["container-blog-menu-item","container-blog-menu-button"]:
        tag_store = 'all'
        container = blog_layout
    elif context in ["portfolio-about-protein-modeling-store"]:
        container = blog_layout
        tag_store = 'protein-model'
    elif context in ["portfolio-about-cheminformatics-store"]:
        container = blog_layout
        tag_store = 'cheminformatics'
    elif context in ["portfolio-about-omics-store"]:
        container = blog_layout
        tag_store = 'omics'
    elif context in ["portfolio-about-machine-learning-store"]:
        container = blog_layout
        tag_store = 'machine-learning'
    elif context in ["portfolio-about-web-app-store"]:
        container = blog_layout
        tag_store = 'devops'

    callback = (
        container,
        tag_store
    )

    return callback


def temporary_store_from_display(context:str):

    from portfolio.pages.home.html import home_temporary_storage
    from portfolio.pages.about.html import about_temporary_storage
    from portfolio.pages.blog.html import blog_temporary_storage

    
    if context in ["container-home-menu-item","container-home-menu-button"]:
        storage = home_temporary_storage
    if context in ["container-about-menu-item","container-about-menu-button"]:
        storage = about_temporary_storage
    if context in ["container-blog-menu-item","container-blog-menu-button"]:
        storage = blog_temporary_storage
    if context in ["portfolio-about-protein-modeling-store"]:
        storage = blog_temporary_storage
    if context in ["portfolio-about-cheminformatics-store"]:
        storage = blog_temporary_storage
    if context in ["portfolio-about-omics-store"]:
        storage = blog_temporary_storage
    if context in ["portfolio-about-machine-learning-store"]:
        storage = blog_temporary_storage
    if context in ["portfolio-about-web-app-store"]:
        storage = blog_temporary_storage

    callback = (
        storage
    )
    return callback