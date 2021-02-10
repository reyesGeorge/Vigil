import dash_html_components as html
from utils import Header, make_dash_table
import dash_core_components as dcc
import pathlib
import pandas as pd
from dash_table import DataTable
import plotly.express as px

import plotly.graph_objects as go

import numpy as np

fig = go.Figure(go.Histogram(
    x=np.random.randint(7, size=100),
    bingroup=1))

fig.add_trace(go.Histogram(
    x=np.random.randint(7, size=20),
    bingroup=1))

fig.update_layout(
    barmode="overlay",
    bargap=0.1)

# fig.show()


# df = px.data.tips()

# fig = px.histogram(x=results_words['count'], y=results_words['keyword'], title="Twitter Word Frequency")
# fig.update_xaxes(title_text='Counts')
# fig.update_yaxes(title_text='Keywords')
# fig.show()


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
                        "Twitter Timeline",
                        className="tableHeader padded",
                    ),
                    dcc.Loading(
                        DataTable(id='twitter_scraped',
                                  virtualization=True,
                                  #   fixed_rows={'headers': True},
                                  style_header={'background-color': 'white'},
                                  style_cell={'font-family': 'Georgia'},
                                  columns=[{'name': col, 'id': col}
                                           for col in ['author_id', 'id', 'lang', 'text', 'geo.place_id',
       'public_metrics.like_count', 'public_metrics.quote_count',
       'public_metrics.reply_count', 'public_metrics.retweet_count']]
                                  ),
                    ),
                    # html.Table(make_dash_table(df_headlines), style={"fontSize": "14px", "textIndent": "10px"}),
                ], className="ten columns"),
                html.Div([
                    html.Br([])
                ], className="one columns")
            ], className="row"),
            html.Br([]),
            html.Br([]),
            html.Div([
                # html.Div([dcc.Graph(figure=fig)], className="six columns"),
                html.Div([html.Br([])], className="two columns"),
                html.Div([dcc.Graph(id="graph")], className="eight columns"),
                html.Div([html.Br([])], className="two columns")

            ], className="row"),
            # Spacer
            html.Div([
                html.Br([]),
            ], style={'display': 'flex', 'justifyContent': 'center', 'paddingTop': '12rem'}, className="row"),

        ],)
    # ], className="page")