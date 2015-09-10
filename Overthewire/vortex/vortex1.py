from socket import socket
from struct import unpack,pack
s = socket()
s.connect(('vortex.labs.overthewire.org',5842))

sum = 0
for i in range(4):
	integer = s.recv(4)
	sum += unpack('I',integer)[0]

s.send(pack('I',(sum & 0xFFFFFFFF)))
print s.recv(0x1024)

