from dash_iconify import DashIconify
from dash.html import Div
from dash.dcc import Store
from dash_breakpoints import WindowBreakpoints
from portfolio.library.icons import github_icon
from portfolio.pages.home.layout import homepage_layout
from dash_mantine_components import (
    Title,
    Container,
    Header,
    Menu,
    MenuTarget,
    MenuDropdown,
    MenuItem,
    ActionIcon,
    Button,
    ButtonGroup,
    Space,
    Anchor,
    Col,
    Grid,
    Center
)
from portfolio.library.config import (
    blog_snippets
)

_navbar_title = Col(
    children=[
        Center(
            Title(
                "Gabriel Navarro, PhD", 
                order=2,
                id="container-navbar-title"
            ),
            style={
                "height":50
            }
        )
    ],
    span=4,
    id="container-navbar-title-col"
)


_navbar_long_menu = Menu(
    children=[
        MenuTarget(
            ActionIcon(
                DashIconify(
                    icon="solar:menu-dots-linear"
                )
            )
        ),
        MenuDropdown(
            [
                MenuItem(
                    "Home", 
                    id="container-home-menu-item"
                ),
                MenuItem(
                    "Blog", 
                    id="container-blog-menu-item"
                ),
                MenuItem(
                    "About", 
                    id="container-about-menu-item"
                )
            ]
        )
    ],
    transition="rotate-left",
    transitionDuration=150,
    position="bottom-start",
    trigger="hover",
    id="container-long-menu",
    style={
        "display":"None"
    }
)


_navbar_wide_menu = ButtonGroup(
    children=[
        Button(
            "Home",
            variant="white",
            id="container-home-menu-button",
            className="sparkle u-hover--sparkle"
        ),
        Button(
            "Blog",
            variant="white",
            id="container-blog-menu-button",
            className="sparkle u-hover--sparkle"
        ),
        Button(
            "About",
            variant="white",
            id="container-about-menu-button",
            className="sparkle u-hover--sparkle"
        )
    ],
    id="container-wide-menu"
)

_navbar_menu = Col(
    Div(
        children=[
            _navbar_long_menu,
            _navbar_wide_menu
        ],
        style={
            'height':50,
            'display': 'flex',         # Enable flexbox
            'flex-direction': 'column',# Stack children vertically
            'justify-content': 'center',# Center children vertically
            'padding-left': 25,
        }
    ),
    span=4,
    id="container-navbar-menu-col"
)


_navbar_icons = Col(
    Div(
        children=[
            Anchor(
                DashIconify(icon=github_icon, width=30),
                href="https://github.com/gabenavarro",
                target="_blank",
            )
        ],
        style={
            'display': 'flex',
            'justify-content': 'flex-end',
            'padding-right': 25,
            'padding-top': 10
        }
    ),
    span=4,
    id="container-navbar-icon-col"
)


navbar_div = Div(
    children=[
        Header(
            Grid(
                children=[
                    _navbar_menu,
                    _navbar_title,
                    _navbar_icons
                ]
            ),
            height="50px",
            fixed="True"
        ),
        Space(h=50)
    ]
)


main_container = Container(
    children=[homepage_layout],    
    id="portfolio-container",
    fluid=True,
    p=0
)


store_div = Div(
    children=[
        Div(
            id="portfolio-context-store-div"
        ),
        # Global
        Store(id="portfolio-blog-tag-store"),
        Store(id="portfolio-about-protein-modeling-store"),
        Store(id="portfolio-about-cheminformatics-store"),
        Store(id="portfolio-about-omics-store"),
        Store(id="portfolio-about-machine-learning-store"),
        Store(id="portfolio-about-web-app-store"),
        # Blog
        Store(id="blog-article-exit-store"),
    ] + [
        Store(
            id=f"blog-controller-{index}-store"
        ) for index in blog_snippets
    ] + [
        Store(
            id=f"blog-card-{index}-button-store"
        ) for index in blog_snippets
    ]
)


breakpoints_div = Div(
    children=[
        Div(
            id="display",
            style={
                'color': 'rgba(0, 0, 0, 0)'
            }
        ),
        WindowBreakpoints(
            id="breakpoints",
            widthBreakpointThresholdsPx=[
                500,
                830,
                1200
            ],
            widthBreakpointNames=[
                "xs",
                "sm",
                "md",
                "lg"
            ]
        )
    ]
)