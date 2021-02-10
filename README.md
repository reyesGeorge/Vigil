<img width="50%" height="50%" alt="Dashboard Preview" src="https://github.com/reyesGeorge/Vigil-Marketing-Dashboard/blob/main/dash_pic.png"> 
[Dashboard preview]


# Vigil Marketing Dashboard
`Vigil` is a concept analysis dashboard to aid campaign ideation

> If you find any of these features helpful, or want to stay tuned as I release more over time, consider leaving a star!

## Features
- GUI made utilizing Flask and Dash
- Query data for:
    - Notable Entities Match
    - SERP Keyword Search
    - Twitter User Query utilizing API v2
    - Visualization of Noun/Entity Vectorization for Twitter User's Timelines

## Coming Soon
- Sentiment Analysis

## Future Features
- Image Generation From Caption
- SEO Keyword Generation
- Content Performance Optimizer

Only for Python 3

## Starting Out
First, you'll want to head over to https://developer.twitter.com/en/apply-for-access and register for a developer account!
After you register and make a project, grab your applications `Bearer Key` and set it in your yourCreds.py file as "bearer_token"

Second, you'll want to head over to https://developers.google.com/knowledge-graph/libraries#python and register for a developer account to access this API!
After you register, grab your `API_KEY` and set it in your yourCreds.py file as "KG_API"


```python
pip install -r requirements.txt
```



To start the dashboard, run the command below:
```python
flask run
```
To run the scraper you will have to go to the googler/spiders directory and run: 
```python
python3 serpGoogler.py
```
Inside the file change the query word to whatever it is that you want to look up
