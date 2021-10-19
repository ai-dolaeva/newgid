from requests.auth import AuthBase
import requests
from datetime import datetime, timedelta


def get_auth_headers(api_key):
    return {"Content-Type": "Application/JSON", "Authorization": api_key}


class NewsApiAuth(AuthBase):
    # Provided by newsapi: https://newsapi.org/docs/authentication
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        request.headers.update(get_auth_headers(self.api_key))
        return request

def get_news(req):

    auth = NewsApiAuth(api_key='8d64b2e970014d7ab5df3f59119fb286')
    EVERYTHING_URL = "https://newsapi.org/v2/everything"
    HEADLINES_URL = "https://newsapi.org/v2/top-headlines"
    URL = HEADLINES_URL
    print(req)
    keys = req.keys()
    today = datetime.now()
    r = ''
    payload = {}
    payload["q"] = ' '
    payload['pageSize'] = 100

    if ('lan' in keys):
        payload["language"] = req['lan']

    if ('category' in keys):
        items = req['category'].split(",")
        if len(items) > 1:
            URL = HEADLINES_URL
            payload["category"] = ''
            for i in items:
                if i != 'undefined':
                    payload["category"] += i+','
            lenstr = len(payload["category"])
            if lenstr > 1:
                payload["category"] = payload["category"][:lenstr - 1]
        elif ('source' in keys):
            items = req['source'].split(",")
            if len(items) > 1:
                URL = EVERYTHING_URL
                payload['from'] = (today - timedelta(days=26)).strftime("%Y-%m-%d")
                payload["domains"] = ''
                for i in items:
                    if i != 'undefined':
                        payload["domains"] += i+','
                lenstr = len(payload["domains"])
                if lenstr > 1:
                    payload["domains"] = payload["domains"][:lenstr - 1]
                payload["to"] = req['date']
                if ('sortby' in keys):
                    payload["sortBy"] = ''
                    for i in req['sortby'].split(","):
                        if i != 'undefined':
                            payload["sortBy"] += i
                    if len(payload["sortBy"]) == 0:
                        payload["sortBy"] = 'publishedAt'

        else:
            URL = HEADLINES_URL
            payload["category"] = 'general'
    print(payload)
    r = requests.get(URL, auth=auth, timeout=100, params=payload)

    print(r.json()['articles'])

    return r.json()['articles']