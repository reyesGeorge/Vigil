import dash_html_components as html
from utils import Header, make_dash_table
import dash_core_components as dcc
import pathlib
import pandas as pd
from dash_table import DataTable


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_headlines = pd.read_csv(DATA_PATH.joinpath("keywordHeadlines.csv"))


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
                html.H4("Knowledge Graph Research"),
            ], style={'display': 'flex', 'justifyContent': 'center', 'paddingTop': '12rem'}),

            # DESCRIPTION
            html.Div([
                html.Br([]),
                html.I(
                    "Data obtained from the Google KGS API"),
                html.Br([])
            ], style={'display': 'flex', 'justifyContent': 'center'}),

            # INPUT
            html.Div([
                html.Br([]),
                html.Div([
                    dcc.Input(id="input2", type="text", placeholder="Search", debounce=True)], className="SPACE"),
                # html.Div(id="output"),
            ], style={'display': 'flex', 'justifyContent': 'center'}),

            # BUTTON
            html.Div([
                html.Button('Fetch', id='button',
                            className="scrapeButton")
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
                    dcc.Loading(
                        DataTable(id='scraped',
                                  virtualization=True,
                                  #   fixed_rows={'headers': True},
                                  style_header={'background-color': 'white'},
                                  style_cell={'font-family': 'Georgia'},
                                  columns=[{'name': col, 'id': col}
                                           for col in ['#', 'query', 'result.@type', 'result.name', 'resultScore',
                                                       'result.detailedDescription.articleBody', 'result.url', 'result.description', 'result.detailedDescription.url']]
                                  ),
                    ),
                    # html.Table(make_dash_table(df_headlines), style={"fontSize": "14px", "textIndent": "10px"}),
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