import tweepy, time,sys


CONSUMER_KEY = 'YOUR KEY'
CONSUMER_SECRET = 'YOUR SECRET'
ACCESS_KEY = 'YOUR ACCESS KEY'
ACCESS_SECRET = 'YOUR ACCESS SECRET'
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)

f = open("tweets.txt",'r')
message = f.readlines()

for line in message:
	api.update_status(line)
	time.sleep(3600)
