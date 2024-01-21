from typing import Dict

def splom_figure_from_blog_section(
    section:Dict):

    from plotly.graph_objects import Figure, Splom
    from pandas import read_parquet

    df = read_parquet("/app%s"%(section['data']))

    fig = Figure(
        data = Splom(
            dimensions=[
                dict(label=i[0],values=df[i[1]]) for i in section['dimensions']
            ],
            showupperhalf=section['showupperhalf'],
            text=df[section['text']],
            marker=dict(
                color=df[section['marker']['color']] if 'color' in section['marker'] else None,
                showscale=section['marker']['showscale'] if 'showscale' in section['marker'] else None,
                line_color=section['marker']['line_color'] if 'line_color' in section['marker'] else None, 
                line_width=section['marker']['line_width'] if 'line_width' in section['marker'] else None
            )
        )
    )

    fig.update_layout(
        title=section['update_layout']['title'] if 'title' in section['update_layout'] else None,
        width=section['update_layout']['width'] if 'width' in section['update_layout'] else None,
        height=section['update_layout']['height'] if 'height' in section['update_layout'] else None,
        template="plotly_dark",
        paper_bgcolor="#333333"
    )
    return fig