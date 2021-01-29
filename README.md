<img width="50%" height="50%" alt="Dashboard Preview" src="https://github.com/reyesGeorge/Vigil-Marketing-Dashboard/blob/main/dash_pic.png"> 
[Dashboard preview]


# Vigil Marketing Dashboard
`Vigil` is a concept analysis dashboard to aid campaign ideation


## Features
- GUI made utilizing Flask and Dash
- Query data for:
    - Notable Entities Match
    - SERP Keyword Search

## Coming Soon
- Twitter integration utilizing the new API v2

## Future Features
- Image Generation From Caption
- SEO Keyword Generation
- Content Performance Optimizer

Only for Python 3

## Starting Out
First, you'll want to head over to https://developer.twitter.com/en/apply-for-access and register for a developer account!
After you register, grab your applications `Bearer Key` and set it in your yourCreds.py file as "bear_key"

Second, you'll want to head over to https://developers.google.com/knowledge-graph/libraries#python and register for a developer account to access this API!
After you register, grab your `API_KEY` and set it in your yourCreds.py file as "api_key"


```python
pip install -r requirements.txt
```

To run the scraper you will have to go to the googler/spiders directory and run: python3 serpGoogler.py
Inside the file change the query word to whatever it is that you want to look up


To start the dashboard, run the command below:
```python
flask run
```
