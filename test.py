import tweepy
from textblob import TextBlob

consumer_key = 'wlDBcghzKh7Sxsw9shDzyXezk'
consumer_secret = 'SyAusvCN6XPaFhZhsF8noa0DSicwKzBjyU92PhPBGFAZ64iTxw'

access_token = '76632886-vak0Oho4h11DLOF4gQMyNIA5hUsz9BUjXm8Fe9rr8'
access_token_secret = 'SX15IWDZ7dftxHw3PSvolDK61zTMtGd6bfcN060t713N8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

