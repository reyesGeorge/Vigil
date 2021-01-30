import datetime
from yourCreds import KG_API
import logging
from itertools import product
from concurrent import futures
import requests
import pandas as pd


# This section of code was taken from the "advertools" package and adapted to work with our Dash inputs/callbacks


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


    
