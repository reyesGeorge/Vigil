import dash_html_components as html
from utils import Header, make_dash_table
import dash_core_components as dcc
import pathlib
import pandas as pd
from dash_table import DataTable


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_headlines = pd.read_csv(DATA_PATH.joinpath("serpData.csv"))


def create_layout(app):
    return html.Div(
        [
            html.Div([Header(app)], style={"background-color": "white"}),

            # html.Div([html.Br([])], style={"padding-top": "20px"}, className="row"),
            # Sinewaves Bar
            html.Div([
                html.Section([
                    html.Div([
                    ], className="sineWaves")
                ], style={"height": "143px"}),
            ], className="row"),

            # TITLE
            html.Div([
                html.Br([]),
                html.H4("SERP Headline Scraper"),
            ], style={'display': 'flex', 'justifyContent': 'center', 'paddingTop': '12rem'}),

            # DESCRIPTION
            html.Div([
                html.Br([]),
                html.I(
                    "Data obtained from the Google Website"),
                html.Br([])
            ], style={'display': 'flex', 'justifyContent': 'center'}),
            # DESCRIPTION 2
            html.Div([
                html.Br([]),
                html.P(
                    "Getting Scrapy to run from a script within a Flask application callback is too much of a pain, instead head on over to the 'googler/spiders' directory and run 'python3 serpGoogler while changing out the keyword in the URL to scrape your data'"),
                html.Br([])
            ], style={'display': 'flex', 'justifyContent': 'center'}),

            # DESCRIPTION 3
            html.Div([
                html.Br([]),
                html.Span(
                    "Once you gather the data you can begin running some NLP"),
                html.Br([])
            ], style={'display': 'flex', 'justifyContent': 'center'}),

            # TABLE
            html.Div([
                html.Div([
                    html.Br([])
                ], className="one columns"),
                html.Div([
                    html.H5(
                        "Headlines",
                        className="tableHeader padded",
                    ),
                    # This is the HTML Table receiving data from a csv path
                    html.Table(make_dash_table(df_headlines), style={"fontSize": "14px", "textIndent": "10px"}),
                ], className="ten columns"),
                html.Div([
                    html.Br([])
                ], className="one columns")
            ], className="row"),
            # Spacer
            html.Div([
                html.Br([]),
            ], style={'display': 'flex', 'justifyContent': 'center', 'paddingTop': '12rem'}, className="row"),

        ],)
    # ], className="page")