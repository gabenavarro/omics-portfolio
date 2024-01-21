from dash.html import Div
from dash.dcc import Store
from dash_iconify import DashIconify
from dash_mantine_components import (
    SimpleGrid,
    Title,
    SegmentedControl,
    Group,
    Button,
    Space, 
    LoadingOverlay,
    ActionIcon,
    Stack, 
    Center
)
from portfolio.library.config import (
    grid_max_width, 
    blog_snippets
)
from portfolio.library.icons import (
    forward_icon, 
    backward_icon,
    exit_icon
)


blog_title = Div(
    children=[
        Space(h=40),
        Title(
            "Blog"
        ),
        Space(h=10),
    ],
    id="blog-title-div"
)


blog_segmented_control = Div(
    [
        SegmentedControl(
            data=[
                dict(
                    label="All",
                    value="all"
                ),
                dict(
                    label="Modeling",
                    value="modeling"
                ),
                # dict(
                #     label="Cheminformatics",
                #     value="cheminformatics"
                # ),
                dict(
                    label="Omics",
                    value="omics"
                ),
                dict(
                    label="ML",
                    value="ml"
                ),
                dict(
                    label="Development",
                    value="devops"
                )
            ],
            id="blog-tag-segmented-control",
            value="all",
            size="xs",
            radius="md"
        ),
        Space(h=40)
    ],
    id="blog-segmented-control-div"
)


_blog_grid_cards = [
    Button(
        children=[],
        style={
            'height':400,
            'width':350,
            'justifyContent': 'center', # Horizontally center children
            'alignItems': 'center',     # Vertically center children
            'background-color': 'transparent'
        },
        variant="white",
        fullWidth=True,
        radius=0,
        compact=True,
        id=f"blog-card-{index}-button"
    ) if index == "one" else Button(
        children=[],
        style={
            'height':400,
            'width':350,
            'justifyContent': 'center', # Horizontally center children
            'alignItems': 'center',     # Vertically center children
            'background-color': 'transparent'
            # "display":"None"
        },
        variant="white",
        fullWidth=True,
        radius=0,
        disabled=True,
        compact=True,
        id=f"blog-card-{index}-button"
    ) for index in blog_snippets
]


blog_controller_storage = Div(
    children=[
        Store(id="blog-article-count-store",data=0),
        Store(id="portfolio-blog-article-store")
    ]
)


blog_temporary_storage = Div(
    children=[]
)


blog_grid = SimpleGrid(
    children=_blog_grid_cards,
    id="blog-simple-grid",
    cols=3,
    spacing="xl",
    maw=grid_max_width
)



blog_navigation_button_group = Group(
    children=[
        ActionIcon(
            DashIconify(icon=backward_icon),
            radius="xl",
            variant="subtle",
            size="md",
            id="blog-article-navigation-backward-actionicon"
        ),
        ActionIcon(
            DashIconify(icon=forward_icon),
            radius="xl",
            variant="subtle",
            size="md",
            id="blog-article-navigation-forward-actionicon"
        )
    ],
    id="blog-navigation-button-group"
)


blog_article_div = Div(
    children=[],
    id="blog-article-div"
)

article_exit_button = ActionIcon(
    DashIconify(
        icon=exit_icon,
        flip="horizontal"
    ),
    radius="xl",
    variant="subtle",
    size="md",
    id="blog-article-exit-actionicon"
)

abstract_stack = Center(
    LoadingOverlay(
        Stack(
            children=[
                blog_title,
                blog_segmented_control,
                blog_grid,
                blog_navigation_button_group,
                article_exit_button,
                blog_article_div,
                blog_controller_storage
            ],
            align="flex-start"
        )
    )
)

