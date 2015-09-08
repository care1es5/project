import facebook
import time

graph = facebook.GraphAPI(access_token='YOUR TOKEN')
f = open('tweets.txt','r')
f = f.readlines()
for line in f:
	attachment = { 'link' : line }
	graph.put_wall_post(message = "Techn News", attachment=attachment)
	time.sleep(3600)


