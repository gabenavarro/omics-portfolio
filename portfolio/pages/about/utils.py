from typing import Tuple


def column_resize_from_display(
    display:str):

    display_width = display.split(",")[0]
    if display_width in ["md","lg"]:
        callback=(
            6,6,12,"horizontal",
            8,4
        )
    else:
        callback=(
            12,12,3,"vertical",
            8,12
        )
    return callback

def stepper_content_from_click(
    stepper:int,
    context:str):

    from portfolio.pages.about.images import (
        amyris_image,
        hexagon_image,
        brightseed_image,
        mondelez_image
    )
    from portfolio.pages.about.text import (
        amyris_text_content,
        hexagon_text_content,
        brightseed_text_content,
        mondelez_text_content
    )

    # Caclulate stepper based on click
    if context == "about-workhistory-backward-actionicon":
        stepper -= 1
    if context == "about-workhistory-forward-actionicon":
        stepper += 1
    stepper = stepper % 4

    # Content from stepper
    if stepper == 0:
        text = mondelez_text_content
        image = mondelez_image

    if stepper == 1:
        text = brightseed_text_content
        image = brightseed_image

    if stepper == 2:
        text = hexagon_text_content
        image = hexagon_image

    if stepper == 3:
        text = amyris_text_content
        image = amyris_image

    callback = (
        stepper,
        text,
        image
    )

    return callback