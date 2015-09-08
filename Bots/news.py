import requests
import json
import time

while True:
	r = requests.get('http://api.nytimes.com/svc/topstories/v1/technology.json?api-key= your api key')
	print r.status_code
	news = r.json()
	news = json.dumps(news, sort_keys=True,indent=4, separators=(',', ': '))
	news = json.loads(news)
	#you can name your file whatever you like 
	f = open("tweets.txt","w")
	for url in news['results']:
		f.write(url['url'] + "\n")
	f.close()
	time.sleep(21600)
	
