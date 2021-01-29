import dash_html_components as html
from utils import Header


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)], style={"background-color": "white"}),

            # html.Div([html.Br([])], style={"padding-top": "20px"}, className="row"),
            # Sinewaves Bar
            # html.Div([
            #     html.Section([
            #         html.Div([
            #         ], className="sineWaves")
            #     ], style={"height": "143px"}),
            # ], className="row"),

            # Title
            html.Div([
                html.Div([html.Br([])], className="three columns"),
                html.H2(["NLP Analysis"], style={"text-align": "center", "padding-top": "40px"}, className="six columns"),
                html.Div([html.Br([])], className="three columns"),
            ], className="row"),

            # Spacer
            html.Div([html.Br([])], style={"padding-top": "20px"}, className="row"),
            # add your UI here, and callbacks go at the bottom of app.py
            # assets and .js go in assets folder
            # csv or images go in data folder

        ],
    )



    # Loop for top named entities
    