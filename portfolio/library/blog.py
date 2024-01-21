

from typing import List, Dict
from dash.development.base_component import Component

def _parse_text_value(
    text_value:str)->List[Component]:

    import re
    from dash_mantine_components import (
        Text, 
        Code, 
        Anchor
    )

    ignore_text = ["BOLD","H","LINK","DOT"]
    break_pattern = r'!!([A-Z]+)!!(.*?)@@'
    bold_pattern = r'!!BOLD!!(.*?)@@'
    highlight_pattern = r'!!H!!(.*?)@@'
    link_pattern = r'!!LINK!!(.*?)@@'

    # Find all matches to patterns
    bold_matches = re.findall(bold_pattern, text_value)
    highlight_matches = re.findall(highlight_pattern, text_value)
    link_matches = re.findall(link_pattern, text_value)

    # Split the input string at each bold section
    split_string = [i for i in re.split(break_pattern, text_value) if i not in ignore_text]

    # Initialize result list
    result = [""]

    # Iterate over the split string and bold matches, alternating between them
    for i in split_string:
        if i in bold_matches:
            result.append(
                i
            )

        elif i in highlight_matches:
            result.append(
                Code(
                    i
                )
            )
        elif i in link_matches:
            href = i.split('](')[0][1:]
            child = i.split('](')[-1][:-1]
            result.append(
                Anchor(
                    children=child,
                    href=href,
                    target="_blank"
                )
            )
        else:
            result.append(
                    i
            )

    result = [
        Text(
            children=result,
        )
    ]
    return result


def _build_figure(section:Dict):
    from dash.dcc import Graph
    from portfolio.library.figures import splom_figure_from_blog_section

    if section['type'] == "Splom":
        figure = splom_figure_from_blog_section(section)

    graph = Graph(figure=figure)
    return graph

def _parse_section(section:Dict[str,str]):

    from dash.html import (
        Div,
        Thead,
        Tbody,
        Th,
        Tr,
        Td
    )
    from dash_mantine_components import (
        Title, 
        Image, 
        Prism, 
        Anchor,
        Center,
        Space,
        Paper,
        Table,
        List,
        ListItem
    )
    element = []
    for key,value in section.items():

        # Header section
        if key.startswith('header'):
            order = int(float(key.split('-')[-1]))
            if order == 1:
                element = Div(
                    [
                        Title(
                            value,
                            order=order
                        )
                    ],
                    className="fadeOut"
                )
            else:
                element = Div(
                    [
                        Space(h=35),
                        Title(
                            value,
                            order=order
                        ),
                        Space(h=15),
                    ],
                    className="fadeOut"
                )
        
        # Text section
        if key == 'text':
            element = Div(
                children=_parse_text_value(value),
                className="fadeOut",
                style={
                    "display":"inline"
                }
            )
        
        # Image section
        if key == 'image':
            src = value.split('](')[-1][:-1]
            caption = value.split('](')[0][2:]
            # if '.png' in value:
            element = Div(
                [
                    Center(
                        Image(
                            src=src,
                            caption=caption,
                            maw=600,
                            className="fadeOut"
                        )
                    ),
                    Space(h=25)
                ]
            )
                
            # if '.gif' in value:
            #     element = Div(
            #         [
            #             Center(
            #                 Image(
            #                     src=src,
            #                     maw=600,
            #                     className="fadeOut"
            #                 )
            #             ),
            #             Space(h=25)
            #         ]
            # )
        
        # Jupyter Notebook
        if key == 'jupyter': 
            element = Div(
                children=[
                    _parse_section(section) for section in value
                ],
                style={
                    "background-color": "#333333",
                    "box-sizing": "border-box",
                    "padding-left": 20,
                    "padding-right": 20,
                    "padding-top": 15
                }
            )

        # Build Figure
        if key == 'figure': 
            element = Div(
                children=[
                    _build_figure(value)
                ]
            )

        # Build table
        if key == 'table': 
            element = Div(
                children=[
                    Table(
                        children=[
                            Thead(
                                Tr(
                                    [
                                        Th(
                                            i,
                                            style={
                                                "color":"#FAF9F6",
                                                "background-color": "#444444"
                                            }
                                        ) for i in value['columns']
                                    ]
                                )
                            )
                        ] + [
                            Tbody(
                                [
                                    Tr(
                                        [
                                            Td(
                                                d,
                                                style={
                                                    "color":"#FAF9F6"
                                                }
                                            ) for d in row
                                        ]
                                    ) for row in value['rows']
                                ]
                            )
                        ],
                        fontSize=12
                    )
                    
                ],
                style={
                    "background-color": "#333333",
                    "box-sizing": "border-box",
                    "padding-left": 10,
                    "padding-right": 10,
                    "padding-bottom": 20
                },
                className="fadeOut"
            )

        # List
        if key == 'list': 
            element = Div(
                children=List(
                    [
                        ListItem(_parse_text_value(section)) for section in value if section.replace("\n","").strip()
                    ]
                ),
                style={
                    "box-sizing": "border-box",
                    "padding-left": 20,
                    "padding-right": 20,
                    "padding-top": 15
                }
            )

        # Code snippet
        if key in ['css','python','bash','python','reason']:
            
            element = Div(
                [
                    Space(h=15),
                    Paper(
                        Prism(
                            language=key,
                            children=value,
                            colorScheme="dark"
                        ),
                        shadow="xs",
                        withBorder=True,
                        style={
                            "background-color": "#000000",
                        }
                    ),
                    Space(h=15)
                ],
                className="fadeOut"
            )

        if key == 'anchor':
            href = value.split('](')[0][1:]
            child = value.split('](')[-1][:-1]
            element = Div(
                [
                    Anchor(
                        child,
                        href=href,
                        target="_blank"
                    ),
                    Space(h=10)
                ],
                className="fadeOut"
            )


    return element


def blog_div_from_blog_sections(
    blog_sections:List[Dict[str,str]]):

    div_children = [
        _parse_section(section) for section in blog_sections
    ]

    return div_children


def blog_section_from_markdown_string(markdown_string:str):
    import re
    from ast import literal_eval
    # Regular expressions for different markdown elements
    header_re = re.compile(r'^(#+)\s*(.*)')
    image_re = re.compile(r'^!\[.*\)$')
    jupyter_re = re.compile(r'^!!!JUPYTER')
    table_re = re.compile(r'^!!!TABLE')
    list_re = re.compile(r'^!!!LIST')
    figure_re = re.compile(r'^!!!FIGURE')
    code_re = re.compile(r'^```')
    anchor_re = re.compile(r'\[http.*?\)')

    lines = markdown_string.split('\n')
    sections = []
    current_section = {}
    in_jupyter_block = False
    in_table_block = False
    in_list_block = False
    in_figure_block = False
    in_code_block = False
    code_language = None
    text_language = None
    
    for line in lines:
        line = line#.strip()

        # Check for headers, images, and code blocks
        header_match = header_re.match(line)
        image_match = image_re.match(line)
        jupyter_match = jupyter_re.match(line)
        table_match = table_re.match(line)
        list_match = list_re.match(line)
        figure_match = figure_re.match(line)
        code_match = code_re.match(line)
        anchor_match = anchor_re.match(line)

        # Check if we are in a code block
        if in_code_block:
            if line.startswith("```"):
                # End of code block
                in_code_block = False
                if in_jupyter_block:
                    jupyter_section["jupyter"].append(current_section)
                else:
                    sections.append(current_section)
                current_section = {}
            else:
                # Continue adding to code block
                current_section[code_language] += line + '\n'
            continue
        
        # Build table
        if in_table_block:
            if line.startswith("COLUMNS:"):
                columns = line.replace("COLUMNS:","").split(",")
                table_section['table']['columns'] = columns
            if line.startswith("ROW:"):
                row = line.replace("ROW:","").split(",")
                table_section['table']['rows'].append(row)
            if table_match:
                in_table_block = False
                if in_jupyter_block:
                    jupyter_section["jupyter"].append(table_section)
                else: 
                    sections.append(table_section)
            continue


        # Build Figure
        if in_figure_block:
            if line.startswith("TYPE:"):
                fig_parameter = line.replace("TYPE:","").strip()
                figure_section['figure']['type'] = fig_parameter
            if line.startswith("DATA:"):
                fig_parameter = line.replace("DATA:","").strip()
                figure_section['figure']['data'] = fig_parameter
            if line.startswith("DIMENSIONS:"):
                fig_parameter = [i.split(",") for i in line.replace("DIMENSIONS:","").strip().split("|")]
                figure_section['figure']['dimensions'] = fig_parameter
            if line.startswith("SHOWUPPERHALF:"):
                fig_parameter = True if line.replace("SHOWUPPERHALF:","") == "True" else False
                figure_section['figure']['showupperhalf'] = fig_parameter
            if line.startswith("TEXT:"):
                fig_parameter = line.replace("TEXT:","").strip()
                figure_section['figure']['text'] = fig_parameter
            if line.startswith("MARKER:"):
                fig_parameter = literal_eval(line.replace("MARKER:","").strip())
                figure_section['figure']['marker'] = fig_parameter
            if line.startswith("UPDATE-LAYOUT:"):
                fig_parameter = literal_eval(line.replace("UPDATE-LAYOUT:","").strip())
                figure_section['figure']['update_layout'] = fig_parameter
            if figure_match:
                in_figure_block = False
                if in_jupyter_block:
                    jupyter_section["jupyter"].append(figure_section)
                else: 
                    sections.append(figure_section)
            continue

        # Build list
        if in_list_block:
            if list_match:
                in_list_block = False
                sections.append(current_section)
            else:
                current_section['list'].append(line)
            continue
        
        # Check if for jupyyter block end
        if in_jupyter_block:
            if jupyter_match:
                in_jupyter_block = False
                sections.append(jupyter_section)
                continue
        
        # Initiations
        if header_match:
            # Handle headers
            header_level = 'header-' + str(len(header_match.group(1)))
            current_section = {header_level: header_match.group(2)}
            sections.append(current_section)
            current_section = {}
        elif image_match:
            # Handle images
            sections.append({'image': line})
        elif jupyter_match:
            # Start Jupyter block
            in_jupyter_block = True
            jupyter_section = {"jupyter":[]}
        elif table_match:
            # Start Table block
            in_table_block = True
            table_section = {"table":{"columns":[],"rows":[]}}
        elif figure_match:
            # Start Figure block
            in_figure_block = True
            figure_section = {
                "figure":{
                    "type":None,
                    "data":None,
                    "x":None,
                    "y":None,
                    "z":None,
                    "text":None,
                    "dimensions":None,
                    "showupperhalf":None,
                    "marker":None,
                    "update-layout":None
                }
            }
        elif list_match:
            # Start List block
            in_list_block = True
            current_section = {"list":[]}
        elif code_match:
            # Start of code block
            in_code_block = True
            code_language = line.replace("```", "")#.strip()
            current_section = {code_language: ''}
        elif anchor_match:
            # handle anchor
            sections.append({'anchor': line})
        elif line:
            # Handle regular text
            text_language = 'text'
            current_section = {text_language: line}
            sections.append(current_section)
                
    #print(sections)
    return sections