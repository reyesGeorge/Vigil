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
    essays,
    portfolio,
    login,
    contact,
    overview,
)


# def clickMethod(input2):
#         if input2:
#             """
#                         This is a webscraper. It works by passing in a URL and the element identifiers into the code below.
#                         """
#             seoWord = input2
#             print(seoWord)
#             chrome_options = Options()
#             chrome_options.add_argument("--headless")
#             chrome_options.add_argument("--window-size=1500,1250")
#             browser = webdriver.Chrome(executable_path="/Users/georgereyes/Downloads/chromedriver",
#                                        options=chrome_options)
#             query = seoWord
#             query = query.replace(' ', '+')
#             URL = f"https://google.com/search?q={query}"
#             resp = browser.get(URL)
#             time.sleep(2)  # 2, causes a delay so its not too fast
#             data = browser.find_elements_by_class_name('LC20lb')
#             headings = []
#             for title in data:
#                 if title:
#                     insights = title.text
#                     headings.append(insights)
#                     while '' in headings:
#                         headings.remove('')
#                         # print('PRINTED:', headings)
#                     # print('PRINTED2:', insights)
#                 else:
#                     pass

#             time.sleep(2)
#             browser.close()
#             df = pd.DataFrame(headings, columns=['Headliners'])
#             df.index += 1
#             downloadedFrame = df.to_csv('keywordHeadlines.csv', index=True)
#             return df.to_dict('rows')
#         else:
#             pass


server = flask.Flask(__name__)



# @server.route('/app')
# def index():
#     return 'Hello Flask app'

# app = dash.Dash(
#     __name__,
#     server=server,
# )
# app = dash.Dash()



# Describe the layout/ UI of the application
# app.layout = html.Div(
#     [dcc.Location(id="url", refresh=True), html.Div(id="page-content")]
# )
# app.config.suppress_callback_exceptions = True


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
        return login.create_layout(app)
    elif pathname == "/essays":
        return essays.create_layout(app)
    elif pathname == "/":
        return portfolio.create_layout(app)
    elif pathname == "/contact":
        return contact.create_layout(app)
    else:
        return overview.create_layout(app)


# all callbacks for pages go here
@app.callback(
    Output("scraped", "data"),
    [Input('button', 'n_clicks')],
    state=[State("input2", "value")]
)
def update_output(n_clicks, input2):
    # f'Input 2 输出 {input2}'
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