import dash_html_components as html
from utils import Header


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)], style={"background-color": "white"}),

            #Sinewaves Bar
            html.Div([
                html.Section([
                    html.Div([
                    ], className="sineWaves")
                ], style={"height": "143px"}),
            ], className="row"),

            # Title
            html.Div([
                html.Div([html.Br([])], className="four columns"),
                html.Div([
                    html.H2(["Portfolio"], style={
                            "text-align": "center", "padding-top": "40px"}),
                    html.Div([
                        html.Br([]),
                        html.I(
                            "The beginning of my portfolio, so far only three features added, more on the way"),
                        html.Br([]),
                        html.Br([])
                    ], style={'display': 'flex', 'justifyContent': 'center'}),
                ], className="four columns"),
                html.Div([html.Br([])], className="four columns"),
            ], className="row"),
            # Title
            html.Div([
                html.Div([html.Br([])], className="four columns"),
                html.Div([
                    html.Div([
                        html.Br([]),
                        html.I(
                            "Check out the latest NLP Visualizer under Twitter API"),
                        html.Br([]),
                        html.Br([])
                    ], style={'display': 'flex', 'justifyContent': 'center'}),
                ], className="four columns"),
                html.Div([html.Br([])], className="four columns"),
            ], className="row"),

            # Spacer
            html.Div([html.Br([])], style={
                     "padding-top": "20px"}, className="row"),

            # DESCRIPTION


            # First Row
            # html.Div([
            #     html.Div([html.Br([])], className="two columns"),
            #     html.Div([
            #         # Tile 1
            #         html.Article([
            #             html.H4("Tile 1"),
            #             html.H6("October 24th, 2020")
            #         ], style={"background-color": "white", "border-radius": "10px", "padding": "15px",
            #                   "border-left": "mediumturquoise solid 4px"}),
            #         # spacer


            #     ], className="four columns"),
            #     html.Div([html.Br([])], className="one columns"),
            #     html.Div([
            #         # Tile 2
            #         html.Article([
            #             html.H4("Tile 2"),
            #             # html.Img(
            #             #         src=app.get_asset_url("addYOURLOGOHERE.png"),
            #             #         className="logo",
            #             #     ),
            #             html.H6("October 24th, 2020")
            #         ], style={"background-color": "white", "border-radius": "10px", "padding": "15px",
            #                   "border-left": "paleturquoise solid 4px"}),
            #         # spacer

            #     ], className="four columns"),
            #     html.Div([html.Br([])], className="two columns"),
            # ], className="row"),


            html.Div([html.Br([])], style={
                     "padding-top": "20px"}, className="row"),
            # ## Second Row
            # html.Div([
            #     html.Div([html.Br([])], className="two columns"),
            #     html.Div([
            #         ## Tile 2
            #         html.Article([
            #             html.H4("Tile 2"),
            #             html.H6("October 24th, 2020")
            #         ], style={"background-color": "white", "border-radius": "10px", "padding": "15px",
            #                   "border-left": "paleturquoise solid 4px"}),
            #         ## spacer

            #     ], className="four columns"),
            #     html.Div([html.Br([])], className="one columns"),
            #     html.Div([
            #         ## Tile 4
            #         html.Article([
            #             html.H4("Tile 4"),
            #             ## html.Img(
            #             ##         src=app.get_asset_url("addYOURLOGOHERE.png"),
            #             ##         className="logo",
            #             ##     ),
            #             html.H6("October 24th, 2020")
            #         ], style={"background-color": "white", "border-radius": "10px", "padding": "15px",
            #                   "border-left": "mediumturquoise solid 4px"}),
            #         ## spacer

            #     ], className="four columns"),
            #     html.Div([html.Br([])], className="two columns"),
            # ], className="row"),

            html.Div([


            ], className="row")


            # page 1
            # add your UI here, and callbacks go at the bottom of app.py
            # assets and .js go in assets folder
            # csv or images go in data folder


            # TITLE

        ]
    )
