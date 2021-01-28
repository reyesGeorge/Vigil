import datetime
from yourCreds import KG_API
import logging
from itertools import product
from concurrent import futures
import requests
import pandas as pd


"""
.. _knowledge_graph:
Import and Analyze Knowledge Graph Results on a Large Scale
===========================================================
If :ref:`analyzing SERPs <serp>` is the first step in understanding your
rankings on search engines, then analyzing the knowledge graph can be thought
of as step zero.
SERP positions for a certain keyword show how each page is ranked in comparison
to all other eligible pages. Knowledge graph scores on the other hand, show the
ranks of the different meanings that a word can take for Google (a person, a
city, a brand, etc.).
.. WARNING:: From `Google's documentation <https://developers.google.com/knowledge-graph>`_:
   This API is not suitable for use as a production-critical service. Your
   product should not form a critical dependence on this API.
It's not clear whether this is from a technical reliability or a content
correctness point of view, but it is what the docs mention. So please keep this
in mind when using it.
Account Setup
*************
In order to be able to send requests, you will need to `create a project
<https://console.developers.google.com/>`_, `set up billing
<https://console.developers.google.com/billing>`_, and `activate the knowledge
graph API <https://console.developers.google.com/apis/library>`_ for your
project. You will then need to `create credentials
<https://console.developers.google.com/apis/credentials>`_ (API Key).
Once you have that, you can use it as your ``key`` parameter when running
requests, as shown below.
How to use Google's Knowledge Graph API
***************************************
What is "google"? Is it a search engine, a company, a brand, a very large
number? What else is it?
And if it is all of those things, what is the relative ranking of each? What
is the source of the information, its URL, images (if any)?
.. code-block:: python
    >>> key = 'YOUR_GOOGLE_DEVELOPER_KEY'
    >>> google =  knowledge_graph(key=key, query='google')
    >>> google
         query	resultScore	                               result.@type                  result.description    result.name
    0	google	     203191	   ['Corporation', 'Organization', 'Thing']                  Technology company	        Google
    1	google	      49462	                       ['WebSite', 'Thing']                              Google         Search
    2	google	      19142	                       ['WebSite', 'Thing']                                 nan          Gmail
    3	google	      13251	              ['Brand', 'WebSite', 'Thing']                             Website	   Google Maps
    4	google	       7549	['WebSite', 'SoftwareApplication', 'Thing']                             Website   Google Drive
    5	google	       6853	                       ['WebSite', 'Thing']                             Website	   Google Play
    6	google	       6543	           ['SoftwareApplication', 'Thing']                         Web browser  Google Chrome
    7	google	       4312	   ['Corporation', 'Organization', 'Thing']  Multinational conglomerate company  Alphabet Inc.
    8	google	       3395	           ['SoftwareApplication', 'Thing']                                 nan Google Account
    9	google	       1306	                                  ['Thing']                                 nan         Google
    >>> google.columns
    Index(['query', 'resultScore', '@type', 'result.@type', 'result.description',
       'result.image.contentUrl', 'result.image.url',
       'result.detailedDescription.articleBody',
       'result.detailedDescription.url', 'result.detailedDescription.license',
       'result.url', 'result.name', 'result.@id', 'query_time'],
      dtype='object')
The above table is a sample response from the :func:`knowledge_graph` function.
Many more columns are available as you can see in the second line above.
We can see that "google" is a company, with a result score of 203,191 and it is
a search engine/website with a result score of 49,462. It is then understood as
an email application, a mapping application, and so on, as you can see in the
`result.name` column.
You can also see that we get the types under which this result falls, in the
`result.@type` column. Multiple types show the type inheritance, and as you can
also see, everything is a "Thing". This is the top element in the type
hierarchy under which everything belongs.
Like :func:`serp_goog` and :func:`serp_youtube`, this funcion works in the same
manner, creating, sending, and aggregating the product of the arguments passed
to it.
For example if you run
>>> knowledge_graph(key=key, query=['google', 'bing'], languages=['en', 'fr', 'de'])
The function will send 2 (queries) x 3 languages = 6 requests.
(google, en), (google, fr), (google, de) , (bing, en), (bing, fr), (bing, de)
This is actually the main value of having this function, because you usually
want a large sample to evaluate certain keywords across languages or types.
Let's check what "seo" and "search engine optimization" mean in different
languages.
>>> seo = knowledge_graph(key=key, query=['seo', 'search engine optimization'], languages=['en', 'es', 'de'])
>>> seo
	query	                        languages	resultScore	    result.name	                     result.@type	                                   result.description
0	search engine optimization	de      	       3587	    Suchmaschinenoptimierung	         ['Thing']                                         nan
1	search engine optimization	de      	        321	    Lokale Suchmaschinenoptimierung	 ['Thing']                                         nan
2	search engine optimization	de      	        252	    Suchmaschinenmarketing	         ['Thing']                                         nan
13	seo	                        de      	       3313	    Seoul	                         ['AdministrativeArea', 'Thing', 'City', 'Place']  Hauptstadt von Südkorea
14	seo	                        de      	       1509	    Seo Yea-ji	                         ['Thing', 'Person']	                           Schauspielerin
15	seo	                        de      	        584	    Suchmaschinenoptimierung	         ['Thing']	                                   nan

>>> seo.columns
Index(['query', 'languages', 'resultScore', '@type', 'result.name',
       'result.@type', 'result.@id', 'result.image.contentUrl',
       'result.image.url', 'result.detailedDescription.license',
       'result.detailedDescription.url',
       'result.detailedDescription.articleBody', 'result.description',
       'result.url', 'query_time'],
      dtype='object')
It's interesting to see how the same word can mean different things in
different contexts.
"""

def _dict_product(d):
    items = list(d.items())
    keys = [x[0] for x in items]
    values = [x[1] for x in items]
    dicts = []
    for prod in product(*values):
        tempdict = dict(zip(keys, prod))
        dicts.append(tempdict)
    return dicts



param_regex = '^query$|^ids$|^languages$|^types$|^prefix$|^limit$'


def knowledge_graph(key, query=None, ids=None, languages=None, types=None,
                    prefix=None, limit=None):
    
    params = locals()
    base_url = 'https://kgsearch.googleapis.com/v1/entities:search?'
    supplied_params = {k: v for k, v in params.items()
                       if params[k] is not None}
    for p in supplied_params:
        if isinstance(supplied_params[p], (str, int)):
            supplied_params[p] = [supplied_params[p]]

    params_list = _dict_product(supplied_params)
    result_df = pd.DataFrame()


    def single_request(param):
        nonlocal result_df
        resp = requests.get(base_url, params=param)
        param_log = ', '.join([k + '=' + str(v) for k, v in param.items()])
        logging.info(msg='Requesting: ' + param_log)
        df = pd.json_normalize(resp.json(), record_path='itemListElement')
        del param['key']
        param_columns = {k: [v] if df.empty else v
                         for k, v in param.items()}
        df = df.assign(**param_columns)
        result_df = result_df.append(df, ignore_index=True)

    with futures.ThreadPoolExecutor(max_workers=16) as executor:
        executor.map(single_request, params_list)

    reordered_df = pd.concat([result_df.filter(regex=param_regex),
                              result_df.filter(regex=f'^(?!{param_regex})')],
                             axis=1)
    reordered_df['query_time'] = pd.Timestamp.utcnow()
    return reordered_df


    