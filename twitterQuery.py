import requests
import os
import json
from yourCreds import bearer_token
import pandas as pd

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return bearer_token


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()



def create_usergrab_url(queryItems):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    queryItems = queryItems.replace(' ', '')
    usernames = f"usernames={queryItems}"
    user_fields = "user.fields=description,created_at,public_metrics"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url

# Host the portfolio
# https://www.pythonanywhere.com/details/flask_hosting



def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Query Users request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def parser(new_json):
    # with open('usersTweet.json', 'w') as outf:
    #     outf.write(new_json)
    tweet_json = json.loads(new_json)
    x = tweet_json['data']

    
    id = []
    
    for i in x:
        
        id.append(str(i['id'].replace(' ','')))
        
    print(id)
        
    # d = {'id': id}
    # new = pd.DataFrame(d)
    # return ','.join(id)
    return id



# def create_users_followers_url():
#     # Replace with user ID below
#     user_id = ## add the ids from users here as integers
#     return "https://api.twitter.com/2/users/{}/followers".format(user_id)


def get_params():
    return {"user.fields": "created_at"}


# def connect_to_users_followers_endpoint(users_followers_url, headers, params):
#     response = requests.request("GET", users_followers_url, headers=headers, params=params)
#     print(response.status_code)
#     if response.status_code != 200:
#         raise Exception(
#             "Users Followers request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     return response.json()


# def create_grabtweets_url():
#     tweet_fields = "tweet.fields=lang,author_id,geo,text,public_metrics"
#     # Tweet fields are adjustable.
#     # Options include:
#     # attachments, author_id, context_annotations,
#     # conversation_id, created_at, entities, geo, id,
#     # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
#     # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
#     # source, text, and withheld
#     ids = "ids=1278747501642657792,1255542774432063488"
#     # You can adjust ids to include a single Tweets.
#     # Or you can add to up to 100 comma-separated IDs
#     url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
#     return url


# def connect_to_grabtweets_endpoint(grabtweets_url, headers):
#     response = requests.request("GET", grabtweets_url, headers=headers)
#     print(response.status_code)
#     if response.status_code != 200:
#         raise Exception(
#             "Grab Tweets request returned an error: {} {}".format(
#                 response.status_code, response.text
#             )
#         )
#     return response.json()


def get_timeline_params():
    return "tweet.fields=lang,author_id,geo,text,public_metrics&max_results=100"


def create_user_timeline_url(cln_ids):
    # Replace with user ID below
    user_id = cln_ids
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def connect_to_user_timeline_endpoint(user_timeline_url, headers, timeline_params):
    response = requests.request("GET", user_timeline_url, headers=headers, params=timeline_params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()




def scale_bird(queryItems):
    #### GET USER CODE *************
    bearer_token = auth()
    url = create_usergrab_url(queryItems)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    new = json.dumps(json_response, indent=4, sort_keys=True)
    # print(new)
    # with open('usersTweet.json', 'w') as outf:
    #     outf.write(new)
    
    cln_ids = parser(new)
    
    for id in cln_ids:
        user_timeline_url = create_user_timeline_url(id)
        timeline_params = get_timeline_params()
        json_response4 = connect_to_user_timeline_endpoint(user_timeline_url, headers, timeline_params)
        naw = json.dumps(json_response4, indent=4, sort_keys=True)
        # with open('usersTimeline.json', 'w') as outf:
        #     outf.write(naw)
        tweets_json = json.loads(naw)
        burd_df = pd.json_normalize(tweets_json, record_path='data',record_prefix='')
        print(burd_df.head(4))
        return burd_df

        

        # final return as a dataframe
    


