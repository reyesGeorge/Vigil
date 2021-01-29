import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([])])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    # html.Img(
                    #     src=app.get_asset_url("addYOURLOGOHERE.png"),
                    #     className="logo",
                    # ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        # [dcc.Link([html.H1(["Welcome!"], style={"marginTop": "12px", "marginLeft": "24px"})], href="/")],
                        [dcc.Link([
                            html.Img(src=app.get_asset_url("logoGR.png"), style={"marginTop": "12px", "marginLeft": "24px"}, className="logo")
                        ],
                                  href="/")],
                        className="five columns",
                    ),
                    html.Div([
                        html.Div(
                            [
                                # dcc.Link(
                                #     "Portfolio",
                                #     href="/",
                                #     className="tab first",
                                # ),
                                html.A(
                                    "Blog",
                                    href="https://georgereyes.dev/",
                                    className="tab",
                                ),
                                dcc.Link(
                                    "SERP Scraper",
                                    href="/serpscrape",
                                    className="tab",
                                ),
                                dcc.Link(
                                    "Knowledge Graph API",
                                    href="/graphapi",
                                    className="tab",
                                ),
                                dcc.Link(
                                    "NLP Analysis",
                                    href="/nlpstats",
                                    className="tab",
                                )
                            ],
                            className="row all-tabs",
                        )
                    ], className="seven columns")
                ],
                className="twelve columns",
                style={"padding-left": "0", "color": "white"},
            )
        ],
        className="row", style={"background-color": "white", "padding-bottom": "10px"}
    )
    return header



def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
