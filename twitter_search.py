import urllib.request
from requests_oauthlib import OAuth1Session # ライブラリ(1)
from bs4 import BeautifulSoup 
from TwitterAPI import TwitterAPI
import requests
import tweepy
import sys, os

arguments = sys.argv
arguments.pop(0)
query_keyword = arguments[0]

# 検索条件
#query_keyword = 'python' #検索語句を指定
query_date = '2018-07-08' #投稿日を指定

# 各種キーをセット
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

#apiを取得
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# twitter内を検索し、結果をprintする
for status in api.search(q=query_keyword, lang='ja', result_type='recent',count=100): #qに検索語句,countに検索結果の取得数
    if str(status.created_at).count(query_date):
        #print(status.user.name) #useridが出てくる
        #print(status.user.screen_name) #ユーザー名が出てくる
        print("★★ TIME:", status.created_at) #投稿時間が出てくる
        print(status.text.encode('UTF-8').decode('UTF-8'), "\n\n") #ツイート内容が出てくる
        #print(status)

#api.update_status('TEST: Hello, world! from tweepy')
