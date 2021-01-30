import dash_html_components as html
from utils import Header, make_dash_table
import dash_core_components as dcc
import pathlib
import pandas as pd
from dash_table import DataTable


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
                html.H4("Twitter Research"),
            ], style={'display': 'flex', 'justifyContent': 'center', 'paddingTop': '12rem'}),

            # DESCRIPTION
            html.Div([
                html.Br([]),
                html.P(
                    "All data obtained utilizing the Twitter v2 API"),
                html.Br([])
                
            ], style={'display': 'flex', 'justifyContent': 'center'}),
            # DESCRIPTION 2
            html.Div([
                html.P(
                    "Type in Twitter User Names only seperated by a comma: user1, user2, user3"),
                html.Br([])
                
            ], style={'display': 'flex', 'justifyContent': 'center'}),

            # INPUT
            html.Div([
                html.Br([]),
                html.Div([
                    dcc.Input(id="twitter_input", type="text", placeholder="Search", debounce=True)], className="SPACE"),
                # html.Div(id="output"),
            ], style={'display': 'flex', 'justifyContent': 'center'}),

            # BUTTON
            html.Div([
                html.Button('Fetch', id='twitter_button',
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
                        DataTable(id='twitter_scraped',
                                  virtualization=True,
                                  #   fixed_rows={'headers': True},
                                  style_header={'background-color': 'white'},
                                  style_cell={'font-family': 'Georgia'},
                                  columns=[{'name': col, 'id': col}
                                           for col in ['description', 'id', 'name', 'username', 'created_at']]
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