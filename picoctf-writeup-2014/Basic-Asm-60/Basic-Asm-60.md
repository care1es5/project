#Basic ASM - 60

```
We found this program snippet.txt, but we`re having some trouble figuring it out. 
What`s the value of %eax when the last instruction (the NOP) runs?

# This file is in AT&T syntax - see http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
# and http://en.wikipedia.org/wiki/X86_assembly_language#Syntax. Both gdb and objdump produce
# AT&T syntax by default.
MOV $1645,%ebx
MOV $2523,%eax
MOV $11302,%ecx
CMP %eax,%ebx
JL L1
JMP L2
L1:
IMUL %eax,%ebx
ADD %eax,%ebx
MOV %ebx,%eax
SUB %ecx,%eax
JMP L3
L2:
IMUL %eax,%ebx
SUB %eax,%ebx
MOV %ebx,%eax
ADD %ecx,%eax
L3:
NOP
```

Basic assembly instruction can be easily translated into codes. So I translated these into python and got the flag:

```
ebx = 1645
ebx = 1645
eax = 2523
ecx = 11302

if(eax > ebx):
        ebx *= eax
        eax += ebx
        eax -= ecx
        print eax
else:
        ebx *= eax
        ebx -= eax
        eax = ebx
        eax += ecx
        print eax

Danny@bt:~/Desktop$ python m.py
4141556

Flag:4141556
```
