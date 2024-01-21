'''# CSS Only Animation Scroll in Dash

## Introduction

Welcome to the intriguing world of practical web development, an essential skill set for scientists immersed in the coding realm who aspire to stand out with more polished, consumer-ready products. In today's blog post, titled "Animation Scroll in Dash using CSS only," we delve into the elegant art of enhancing web applications. As a career scientist who has transitioned from intensive coding to the realm of educational blogging, I understand the significance of adding that extra flair to your projects. This post is specifically tailored for those utilizing Dash, a Python framework for building analytical web applications. We will explore how to create captivating scroll animations using only CSS, providing your Dash applications with a dynamic and visually appealing user experience. This approach not only elevates the aesthetic appeal of your projects but also demonstrates the power of CSS in creating interactive and engaging web interfaces. Whether you're a seasoned coder or just beginning your journey, this guide will walk you through the steps to implement smooth, eye-catching scroll animations, transforming your scientific data presentations into interactive storytelling masterpieces. Let's get scrolling!

## Setup 

1. To begin, make sure you have an `assets` folder in your project directory as shown below:

![Figure 1. Project folder structure.](/assets/images/blog/1/folder-structure.png)

Make sure you have a file named `style.css` in the `assets` folder. 

2. Open up the style.css file and copy the following code snippet into your style sheet.

```css
@media (prefers-reduced-motion: no-preference){
  .fadeIn > * {
    scale: 0.6;
    opacity: 0;
    animation: fade-in linear forwards;
    animation-timeline: view();
    animation-range: entry;
  }
  @keyframes fade-in {
    to {
      scale: 1;
      opacity: 1;
    }
  }
}
```

3. To apply this to any dash component, apply the `fadeIn` class to it. For example:

```python
from dash import html
import dash_mantine_components as dmc

_publications_html = html.Div(
    dmc.Center(
        children=[
            dmc.Title(
                "2021",
                order=3
            ),
            dmc.Divider(
                variant="solid"
            ),
            dmc.Space(
                h=25
            ),
            dmc.Image(
                src=publication_2021,
                className="fadeIn" # <-- applying fadeIn class
            ),
        ],
        p=25
    )
)
```

After applying the class to your image component, you should now have a fade in animation as shown below:

![Figure 2a. Image with and without fadeIn class applied.](/assets/images/blog/1/juxtapose-fadein.gif)

## Breakdown

Breaking down CSS code can be an insightful journey, especially when it involves creating engaging web elements like animations. Let's dissect the provided CSS code snippet line by line:

1. `@media (prefers-reduced-motion: no-preference)`
    - This line is a media query that checks if the user has expressed no preference for reduced motion in their system settings. It's a way to respect accessibility preferences. If the user prefers reduced motion, the styles inside this block won't apply.

2. `.fadeIn > *`
    - This selector, `>`, targets all child elements, `*`, of any element with the class `fadeIn`. It means that the following styles will be applied to each child element within a container that has the `fadeIn` class. 
    - You can further customize this section by giving this class any abitrary name instead of `fadeIn`. You can be more specific with child elements you would like to apply the animation to by replace `*` with your target element types.

3. `scale: 0.6;`
    - This line sets the initial scale (size) of each child element to 60% of its original size. This is part of setting up the animation effect.

4. `opacity: 0;`
    - This sets the initial opacity of the child elements to 0, making them fully transparent initially.

5. `animation: fade-in linear forwards;`
    - This shorthand property defines the animation. 
    - `fade-in` is the name of the keyframes animation defined later. 
    - `linear` is the timing function, meaning the animation proceeds at a constant pace. 
    - `forwards` means the animation will retain the styles set by the last keyframe after it finishes.

6. `animation-timeline: view();`
    - This line defines the timeline for the animation. The `view()` function is a library-provided function that controls when the animation starts, based on the element's visibility in the viewport.

7. `animation-range: entry;`
    - This sets the range of the animation, with `entry` likely defining a specific point or duration within the animation timeline.

8. `@keyframes fade-in`
   - This block defines the `fade-in` animation. `@keyframes` is used to create custom animations by specifying styles at various points during the animation sequence.

9. `to`
    - This indicates the final state of the animation. In CSS animations, you can define from/to or any percentage points.

10. `scale: 1;`
    - This sets the scale of the element to its original size (100%) at the end of the animation.

11. `opacity: 1;`
    - This sets the element to be fully opaque (no transparency) at the end of the animation.

In summary, this CSS snippet is designed to animate elements within a `.fadeIn` class container to gradually change from smaller and transparent to their full size and opacity. The animation is designed to be respectful of users' accessibility settings regarding motion.

## Resources

Used to make this blog was Kevin Powell's youtube videos (1).

[https://www.youtube.com/watch?v=UmzFk68Bwdk](1. Incredible scroll-based animations with CSS-only)
''' 