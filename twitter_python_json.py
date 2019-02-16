import oauth2
#import json

API_KEY = ''
API_SECRET = ''
TOKEN_KEY = ''
TOKEN_SECRET = ''

def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=API_KEY, secret=API_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body.encode('utf8'), headers=http_headers)
    return content

url = 'https://api.twitter.com/1.1/search/tweets.json?q=python%20tweepy&src=typd'
data = oauth_req(url, TOKEN_KEY, TOKEN_SECRET)

#data = json.loads(data)

with open("twitter_python.json", "wb") as data_file:
    data_file.write(data)
    
