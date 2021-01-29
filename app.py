import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import time
from keywordQuery import knowledge_graph, KG_API
from pages import (
    blog,
    serpScraper,
    home,
    knowledgeGraph,
    nlpStats,
    overview,
)


server = flask.Flask(__name__)



app = dash.Dash(
    __name__,
    server=server,
    suppress_callback_exceptions=True
)
app.layout = html.Div(
    [dcc.Location(id="url", refresh=True), html.Div(id="page-content")]
)


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/blog":
        return blog.create_layout(app)
    elif pathname == "/graphapi":
        return knowledgeGraph.create_layout(app)
    elif pathname == "/serpscrape":
        return serpScraper.create_layout(app)
    elif pathname == "/":
        return home.create_layout(app)
    elif pathname == "/nlpstats":
        return nlpStats.create_layout(app)
    else:
        return overview.create_layout(app)


# all callbacks for pages go here
# SERP Scraper Callback
# @app.callback(
#     Output("serp_scrape", "data"),
#     [Input('serp_button', 'n_clicks')],
#     state=[State("serp_input", "value")]
# )
# def update_output2(n_clicks, serp_input):
#     if n_clicks is None:
#         raise PreventUpdate
#     else:
#         pass
        

# Knowledge Graph Callback
@app.callback(
    Output("scraped", "data"),
    [Input('button', 'n_clicks')],
    state=[State("input2", "value")]
)
def update_output(n_clicks, input2):
    if n_clicks is None:
        raise PreventUpdate
    else:
        searched2 =  knowledge_graph(key=KG_API, query=input2)
        searched2['#'] = list(range(1, len(searched2) + 1))
        return searched2.to_dict('rows')
        
        # return clickMethod(input2)



# keeping data queries withing data callbacks ensures fresh data is coming in upon input change

if __name__ == '__main__':
    app.run_server(debug=False)