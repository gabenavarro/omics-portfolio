from dash.html import Div
from portfolio.pages.about.text import summary_text_content, amyris_text_content
from portfolio.library.icons import forward_icon, backward_icon
from portfolio.library.config import grid_max_width
from dash_iconify import DashIconify
from dash_mantine_components import (
    Grid,
    Col,
    Center,
    Title,
    Image,
    ActionIcon,
    Group,
    Stepper,
    StepperStep,
    Stack,
    Space,
    Divider
)
from portfolio.pages.about.images import *


about_temporary_storage = []

_summary_image = Col(
    children=[
        Space(h=75),
        Center(
            Image(
                src=portrait_image,
                maw=400
            ),
            style={
                "height":"auto",
            },
            p=25,
        )
    ],
    id="about-summary-portrait-col",
    span=6
)

_summary_text = Col(
    Center(
        Div(
            children=summary_text_content
        ),
        style={
            "height":"auto",
            'max-width':800
        },
        p=25
    ),
    id="about-summary-text-col",
    span=6
)

summary_grid = Center(
    Grid(
        children=[
            _summary_image,
            _summary_text
        ],
        justify="center",
        gutter="xl",
        maw=grid_max_width,
        p=25
    )
)


_work_history_title = Col(
    Title(
        "Work History",
        order=2,
        style={
            "height":50,
            'justifyContent': 'center', # Horizontally center children
            'alignItems': 'center',     # Vertically center children
        }
    ),
    span=12,
    id="about-workhistory-title-col",
    p=25
)

_work_history_stepper = Col(
    Stack(
        children=[
            Group(
                children=[
                    ActionIcon(
                        DashIconify(icon=backward_icon),
                        radius="xl",
                        variant="subtle",
                        size="md",
                        id="about-workhistory-backward-actionicon"
                    ),
                    ActionIcon(
                        DashIconify(icon=forward_icon),
                        radius="xl",
                        variant="subtle",
                        size="md",
                        id="about-workhistory-forward-actionicon"
                    )
                ]
            ),
            Stepper(
                active=3,
                orientation="horizontal",
                id="about-workhistory-stepper",
                children=[
                    StepperStep(
                        label="Mondelez", 
                        description="Consumer Packaged Goods, Nutrition"
                    ),
                    StepperStep(
                        label="Brightseed", 
                        description="Food Technology, Nutrition"
                    ),
                    StepperStep(
                        label="Hexagon", 
                        description="Synthetic Biology, Drug Discovery"
                    ),
                    StepperStep(
                        label="Amyris", 
                        description="Synthetic Biology, Sustainability"
                    ),
                ]
            )
        ],
        align="center",
        justify='center'
    ),
    id="about-workhistory-stepper-col",
    span=12
)


_work_history_text = Col(
    Center(
        Div(
            children=amyris_text_content,
            id="about-workhistory-text-div"
        ),
        style={
            "height":"auto",
            'max-width':800
        },
        p=25
    ),
    id="about-workhistory-text-col",
    span=8
)


_work_history_image = Col(
    Center(
        children=[
            Image(
                src=amyris_image,
                maw=400,
                id="about-workhistory-image"
            )
        ],
        style={
            "height":600,
        },
        p=25,
    ),
    id="about-workhistory-image-col",
    span=4
)



work_history_grid = Center(
    Grid(
        children=[
            _work_history_title,
            _work_history_stepper,
            _work_history_text,
            _work_history_image
        ],
        justify="center",
        gutter="xl",
        maw=grid_max_width,
        p=25
    )
)


_publication_title = Col(
    Title(
        "Publications & Patents",
        order=2,
        style={
            "height":50,
            'justifyContent': 'center', # Horizontally center children
            'alignItems': 'center',     # Vertically center children
        }
    ),
    span=12,
    id="about-publication-title-col",
    p=25
)


_publications_2021 = Col(
    Center(
        Div(
            children=[
                Title(
                    "2021",
                    order=3
                ),
                Divider(
                    variant="solid"
                ),
                Space(
                    h=25
                ),
                Image(
                    src=publication_2021,
                    className="fadeIn"
                ),
            ]
        ),
        p=25
    ),
    id="about-publication-2021-col",
    span=12
)


_publications_2016 = Col(
    Center(
        Div(
            children=[
                Title(
                    "2016",
                    order=3
                ),
                Divider(variant="solid"),
                Divider(variant="solid"),
                Space(h=25),
                Image(src=publication_2016a,className="fadeIn"),
                Space(h=30),
                Divider(variant="dashed"),
                Space(h=30),
                Image(src=publication_2016b,className="fadeIn"),
                Space(h=30),
                Divider(variant="dashed"),
                Space(h=30),
                Image(src=patent_2016,className="fadeIn"),
            ]
        ),
        p=25
    ),
    id="about-publication-2016-col",
    span=12
)



_publications_2015 = Col(
    Center(
        Div(
            children=[
                Title(
                    "2015",
                    order=3
                ),
                Divider(variant="solid"),
                Divider(variant="solid"),
                Space(h=25),
                Image(src=publication_2015a,className="fadeIn"),
                Space(h=30),
                Divider(variant="dashed"),
                Space(h=30),
                Image(src=publication_2015b,className="fadeIn"),
                Space(h=30),
                Divider(variant="dashed"),
                Space(h=30),
                Image(src=publication_2015c,className="fadeIn"),
                Space(h=30),
                Divider(variant="dashed"),
                Space(h=30),
                Image(src=patent_2015,className="fadeIn"),
            ]
        ),
        p=25
    ),
    id="about-publication-2015-col",
    span=12
)



_publications_2014 = Col(
    Center(
        Div(
            children=[
                Title(
                    "2014",
                    order=3
                ),
                Divider(variant="solid"),
                Divider(variant="solid"),
                Space(h=25),
                Image(src=publication_2014,className="fadeIn"),
                Space(h=30),
                Divider(variant="dashed"),
                Space(h=30),
                Image(src=patent_2014,className="fadeIn"),
            ]
        ),
        p=25
    ),
    id="about-publication-2014-col",
    span=12
)



_publications_2012 = Col(
    Center(
        Div(
            children=[
                Title(
                    "2012",
                    order=3
                ),
                Divider(variant="solid"),
                Divider(variant="solid"),
                Space(h=25),
                Image(src=publication_2012,className="fadeIn"),

            ]
        ),
        p=25
    ),
    id="about-publication-2012-col",
    span=12
)



_publications_2008 = Col(
    Center(
        Div(
            children=[
                Title(
                    "2008",
                    order=3
                ),
                Divider(variant="solid"),
                Divider(variant="solid"),
                Space(h=25),
                Image(src=publication_2008,className="fadeIn"),
            ]
        ),
        p=25
    ),
    id="about-publication-2008-col",
    span=12
)



publication_grid = Center(
    Grid(
        children=[
            _publication_title,
            _publications_2021,
            _publications_2016,
            _publications_2015,
            _publications_2014,
            _publications_2012,
            _publications_2008
        ],
        justify="center",
        gutter="xl",
        maw=grid_max_width,
        p=25
    )
)
