from socket import socket
import sys

if len(sys.argv) < 2:
	print "Usage: python brute.py [HOST] [PORT] [NUMBER OF 'A' TO SEND]"
	exit(0)

s = socket()

HOST = sys.argv[1]
PORT = int(sys.argv[2])
number = sys.argv[3]

s.connect((HOST,PORT))

s.send("A" * int(number) +"\n")

print "Response: %s " % (s.recv(0x1024))






