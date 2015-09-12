from socket import socket
from struct import unpack,pack

s = socket()
s.connect(('vortex.labs.overthewire.org',5842))

total = 0
for i in range(4):
	integer = s.recv(4)
	total += unpack('I',integer)[0]

s.send(pack('I',(total & 0xFFFFFFFF))+"\n")

print s.recv(0x1024)

