from typing import Tuple

def graphic_from_selection(
    n_inverval:int,
    publication:bool,
    patent:bool,
    computational:bool,
    experience:bool)->Tuple[str]:
    '''Generate Graphics Based on User Selections
    ---
    This function creates a tuple of Image objects based on the provided selection criteria. 
    It takes boolean values for various types of criteria like publications, patents, 
    computational aspects, and experience, and an integer for interval. Based on these inputs, 
    it generates relevant graphical representations.

    ### Parameters
        * `n_interval` (int): The interval or frequency for generating graphics.
        * `publication` (bool): Flag to determine if publications are included in the graphic.
        * `patent` (bool): Flag to indicate inclusion of patent-related graphics.
        * `computational` (bool): Indicates whether computational aspects are to be included.
        * `experience` (bool): A flag to include experience-related graphics.

    ### Return
        * `Tuple['str']`: A tuple of Image objects representing the selected criteria. 
        Each `Image` in the tuple corresponds to a specific selection criterion.

    '''

    from portfolio.pages.home.image import hero_carousel

    if publication:
        image = hero_carousel[0]
    elif patent:
        image = hero_carousel[1]
    elif computational:
        image = hero_carousel[2]
    elif experience:
        image = hero_carousel[3]
    else:
        image = hero_carousel[n_inverval % len(hero_carousel)]

    callback = (image)
    return callback


def column_resize_from_display(
    display:str):

    display_width = display.split(",")[0]
    if display_width in ["md","lg"]:
        callback=(
            4,4,4,
            4,4
        )
    elif display_width in ["sm"]:
        callback=(
            6,6,6,
            6,6
        )
    else:
        callback=(
            12,12,12,
            12,12
        )
    return callback


def tag_from_click():
    callback = (
        'placeholder'
    )
    return callback