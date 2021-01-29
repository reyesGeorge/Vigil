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

            # Blog Posts
            html.Div([
                html.Div([html.Br([])], className="three columns"),
                html.Div([
                    #Blog 1
                    html.Article([
                        html.H4("Parallel Processing for Faster Cleaning"),
                        html.H6("October 24th, 2020")
                    ], style={"background-color": "white", "border-radius": "10px", "padding": "15px",
                              "border": "whitesmoke ridge 4px"}),
                    #spacer
                    html.Div([html.Br([])], style={"padding-top": "5px"}, className="row"),
                    # Blog 1
                    html.Article([
                        html.H4("What is Chunking"),
                        html.H6("October 24th, 2020")
                    ], style={"background-color": "white", "border-radius": "10px", "padding": "15px",
                              "border": "paleturquoise ridge 4px"}),
                    # spacer
                    html.Div([html.Br([])], style={"padding-top": "5px"}, className="row"),
                    # Blog 1
                    html.Article([
                        html.H4("Parallel Processing for Faster Cleaning"),
                        html.H6("October 24th, 2020")
                    ], style={"background-color": "white", "border-radius": "10px", "padding": "15px",
                              "border": "whitesmoke ridge 4px"}),
                    # spacer
                    html.Div([html.Br([])], style={"padding-top": "5px"}, className="row"),
                ], className="six columns"),
                html.Div([html.Br([])], className="three columns"),
            ], className="row"),
            html.Div([

            ], className="row")


            # add your UI here, and callbacks go at the bottom of app.py
            # assets and .js go in assets folder
            # csv or images go in data folder

        ]
    )