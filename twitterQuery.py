import requests
import os
import json
from yourCreds import bearer_token
import pandas as pd

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return bearer_token


def create_url(queryItems):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    # usernames = "usernames=TwitterDev,TwitterAPI,YourTwitterHandle"
    queryItems = queryItems.replace(' ', '')
    usernames = f"usernames={queryItems}"
    
    user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url


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

def parser(new_json):
    # with open('usersTweet.json', 'w') as outf:
    #     outf.write(new_json)
    tweet_json = json.loads(new_json)
    x = tweet_json['data']

    description = []
    id = []
    name = []
    username = []
    created_at = []
    for i in x:
        description.append(i['description'])
        id.append(i['id'])
        name.append(i['name'])
        username.append(i['username'])
        created_at.append(i['created_at'])

        # d.add('description', i['id'])
    d = {'description': description, 'id': id, 'name': name, 'username': username, 'created_at': created_at}
    new = pd.DataFrame(d)
    # print(new.head())
    return new





def scale_bird(queryItems):
    bearer_token = auth()
    url = create_url(queryItems)
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    new = json.dumps(json_response, indent=4, sort_keys=True)
    data = parser(new)
    return data



# If you want to reuse this in its own script file below is good practice
# if __name__ == "__main__":
#     main()