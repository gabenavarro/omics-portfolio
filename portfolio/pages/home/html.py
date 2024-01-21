from dash_mantine_components import (
    Button,
    BackgroundImage,
    Col, 
    Text,
    Grid,
    Center,
    Title,
    Image
)
from portfolio.library.config import grid_max_width
from portfolio.pages.home.image import (
    protein_modeling_image,
    cheminformatics_image,
    omics_image,
    machine_learning_image,
    web_application_image
)

home_temporary_storage = []


homepage_text_grid = Grid(
    children=[
        Col(
            Center(
                children=[
                    Title(
                        "Computational Scientist",
                        order=4
                    )
                ],
                p="md",
                style={
                    'height':100,
                    'style':'flex',
                    'width':'100%'
                }
            ),
            span=12
            
        )
    ]
)

homepage_graphic_grid = Center(
    Grid(
        children=[
            Col(
                children=[
                    Button(
                        children=[
                            Image(
                                src=protein_modeling_image,
                                className='button-hover',
                                height=400,
                                style={
                                    'height':400,
                                    'style':'flex',
                                    'width':500
                                },
                            ),
                            Text(
                                "Protein Modeling",
                                className='home-text-centered',
                                color="white"
                            )

                        ],
                        style={
                            'height':400,
                            'max-width':500,
                            'justifyContent': 'center', # Horizontally center children
                            'alignItems': 'center',     # Vertically center children
                            'overflow':'hidden'
                        },
                        variant="white",
                        fullWidth=True,
                        radius=0,
                        compact=True,
                        id="home-protein-model-graphic-button",
                    )
                ],
                span=4,
                id="home-protein-model-graphic-col"
            ),
            Col(
                children=[
                    Button(
                        children=[
                            Image(
                                src=cheminformatics_image,
                                className='button-hover',
                                width=500,
                                height=400,
                                style={
                                    'height':400,
                                    'style':'flex',
                                    'width':500
                                },
                            ),
                            Text(
                                "Cheminformatics",
                                className='home-text-centered',
                                color="black"
                            )
                        ],
                        style={
                            'height':400,
                            'max-width':500,
                            'justifyContent': 'center', # Horizontally center children
                            'alignItems': 'center',     # Vertically center children
                            'overflow':'hidden'
                        },
                        variant="white",
                        fullWidth=True,
                        radius=0,
                        compact=True,
                        id="home-cheminformatics-graphic-button"
                    )
                ],
                span=4,
                id="home-cheminformatics-graphic-col",
                style={"display":"none"}
            ),
            Col(
                children=[
                    Button(
                        children=[
                            Image(
                                src=omics_image,
                                className='button-hover',
                                width=500,
                                height=400,
                                style={
                                    'height':400,
                                    'style':'flex',
                                    'width':500
                                },
                            ),
                            Text(
                                "Omics",
                                className='home-text-centered',
                                color="white"
                            )
                        ],
                        style={
                            'height':400,
                            'max-width':500,
                            'justifyContent': 'center', # Horizontally center children
                            'alignItems': 'center',     # Vertically center children
                            'overflow':'hidden'
                        },
                        variant="white",
                        fullWidth=True,
                        radius=0,
                        compact=True,
                        id="home-omics-graphic-button"
                    )
                ],
                span=4,
                id="home-omics-graphic-col"
            ),
            Col(
                children=[
                    Button(
                        children=[
                            Image(
                                src=machine_learning_image,
                                className='button-hover',
                                width=500,
                                height=400,
                                style={
                                    'height':400,
                                    'style':'flex',
                                    'width':500
                                },
                            ),
                            Text(
                                "Machine Learning",
                                className='home-text-centered',
                                color="black"
                            )
                        ],
                        style={
                            'height':400,
                            'max-width':500,
                            'justifyContent': 'center', # Horizontally center children
                            'alignItems': 'center',     # Vertically center children
                            'overflow':'hidden'
                        },
                        variant="white",
                        fullWidth=True,
                        radius=0,
                        compact=True,
                        id="home-machine-learning-graphic-button"
                    )
                ],
                span=4,
                id="home-machine-learning-graphic-col"
            ),
            Col(
                children=[
                    Button(
                        children=[
                            Image(
                                src=web_application_image,
                                className='button-hover',
                                width=500,
                                height=400,
                                style={
                                    'height':400,
                                    'style':'flex',
                                    'width':500
                                },
                            ),
                            Text(
                                "Development",
                                className='home-text-centered',
                                color="white"
                            )
                        ],
                        style={
                            'height':400,
                            'max-width':500,
                            'justifyContent': 'center', # Horizontally center children
                            'alignItems': 'center',     # Vertically center children
                            'overflow':'hidden'
                        },
                        variant="white",
                        fullWidth=True,
                        radius=0,
                        compact=True,
                        id="home-web-app-graphic-button"                 
                    )
                ],
                span=4,
                id="home-web-app-graphic-col"
            ),
        ],
        justify="center",
        gutter="xl",
        maw=grid_max_width,
        p=25
    )
)