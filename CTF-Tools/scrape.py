import requests
import sys
from bs4 import BeautifulSoup
import argparse
import subprocess


parser = argparse.ArgumentParser(description="Easy Crwaling")
parser.add_argument("-u","--url", help="crawl url,creates scrape.html file and show in nice structure (in less)")
parser.add_argument("-a","--link",action="count",help ="print all the links from the provided url")
parser.add_argument("-l","--llst",action="count",help ="return list with all the links")

args = parser.parse_args()

if not args.url:
	parser.print_help()
	exit(0)

if "http:" in args.url or "https:" in args.url:
	r = requests.get(args.url)
	soup = BeautifulSoup(r.text,'html.parser')
	l = []
	for link in soup.find_all('a'):
		l.append(link.get('href'))

	if args.link == 1:
		num = 0
		for link in soup.find_all('a'):
			print (str(num) + ". " + link.get('href')) 	
			num +=1
		if args.link == 1 and args.llst == 1:
			print l	
			
	elif not args.link and args.llst == 1:
		print l
	else:		
		scrape = soup.prettify().encode('utf-8')
		f = open('scrape.html','w')
		f.write(scrape)
		f.close()
		cmd = "cat scrape.html | less"
		subprocess.call(cmd,shell=True)
		
else:
	print "[*] There was a problem in the process of crawling"	




		
