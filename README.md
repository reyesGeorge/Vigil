# Vigil Marketing Dashboard
`Vigil` is a concept analysis dashboard to visualize conceptualizations


## Features
- GUI made utilizing Flask and Dash
- Query data for:
    - Notable Entities Match
    - Twitter

    
- Utilises Twitter's new API v2
- Only for Python 3

## Future Features
- Image Generation From Caption
- SEO Keyword Generation
- Content Performance Optimizer

## Starting Out
First, you'll want to head over to https://developer.twitter.com/en/apply-for-access and register for a developer account!
After you register, grab your applications `Bearer Key` and set it in your creds.py file as "bear_key"

Second, you'll want to head over to https://developers.google.com/knowledge-graph/libraries#python and register for a developer account to access this API!
After you register, grab your `API_KEY` and set it in your creds.py file as "api_key"


```python
import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import time
```
