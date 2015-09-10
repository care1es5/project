#Behemoth0

```
behemoth0@melinda:/behemoth$ gdb behemoth0 -q
Reading symbols from behemoth0...(no debugging symbols found)...done.
(gdb) disassemble main
Dump of assembler code for function main:
   0x080485a2 <+0>:	push   %ebp
   0x080485a3 <+1>:	mov    %esp,%ebp
   0x080485a5 <+3>:	and    $0xfffffff0,%esp
   0x080485a8 <+6>:	sub    $0x70,%esp
   0x080485ab <+9>:	mov    %gs:0x14,%eax
   0x080485b1 <+15>:	mov    %eax,0x6c(%esp)
   0x080485b5 <+19>:	xor    %eax,%eax
   0x080485b7 <+21>:	movl   $0x475e4b4f,0x1f(%esp)
   0x080485bf <+29>:	movl   $0x45425953,0x23(%esp)
   0x080485c7 <+37>:	movl   $0x595e58,0x27(%esp)
   0x080485cf <+45>:	movl   $0x8048720,0x10(%esp)
   0x080485d7 <+53>:	movl   $0x8048738,0x14(%esp)
   0x080485df <+61>:	movl   $0x804874d,0x18(%esp)
   0x080485e7 <+69>:	movl   $0x8048761,(%esp)
   0x080485ee <+76>:	call   0x8048400 <printf@plt>
   0x080485f3 <+81>:	lea    0x2b(%esp),%eax
   0x080485f7 <+85>:	mov    %eax,0x4(%esp)
   0x080485fb <+89>:	movl   $0x804876c,(%esp)
   0x08048602 <+96>:	call   0x8048470 <__isoc99_scanf@plt>
   0x08048607 <+101>:	lea    0x1f(%esp),%eax
   0x0804860b <+105>:	mov    %eax,(%esp)
   0x0804860e <+108>:	call   0x8048440 <strlen@plt>
   0x08048613 <+113>:	mov    %eax,0x4(%esp)
   0x08048617 <+117>:	lea    0x1f(%esp),%eax
   0x0804861b <+121>:	mov    %eax,(%esp)
   0x0804861e <+124>:	call   0x804857d <memfrob>
   0x08048623 <+129>:	lea    0x1f(%esp),%eax
   0x08048627 <+133>:	mov    %eax,0x4(%esp)
   0x0804862b <+137>:	lea    0x2b(%esp),%eax
   0x0804862f <+141>:	mov    %eax,(%esp)
   0x08048632 <+144>:	call   0x80483f0 <strcmp@plt>
   0x08048637 <+149>:	test   %eax,%eax
   0x08048639 <+151>:	jne    0x8048665 <main+195>
   0x0804863b <+153>:	movl   $0x8048771,(%esp)
   0x08048642 <+160>:	call   0x8048420 <puts@plt>
   0x08048647 <+165>:	movl   $0x0,0x8(%esp)
   0x0804864f <+173>:	movl   $0x8048782,0x4(%esp)
   0x08048657 <+181>:	movl   $0x8048785,(%esp)
   0x0804865e <+188>:	call   0x8048460 <execl@plt>
   0x08048663 <+193>:	jmp    0x8048671 <main+207>
   0x08048665 <+195>:	movl   $0x804878d,(%esp)
   0x0804866c <+202>:	call   0x8048420 <puts@plt>
   0x08048671 <+207>:	mov    $0x0,%eax
   0x08048676 <+212>:	mov    0x6c(%esp),%edx
   0x0804867a <+216>:	xor    %gs:0x14,%edx
   0x08048681 <+223>:	je     0x8048688 <main+230>
   0x08048683 <+225>:	call   0x8048410 <__stack_chk_fail@plt>
   0x08048688 <+230>:	leave
   0x08048689 <+231>:	ret
End of assembler dump.
(gdb) b*0x08048627
Breakpoint 1 at 0x8048627
(gdb) r
Starting program: /games/behemoth/behemoth0
Password: asd123
(gdb) x /s $eax
0xffffd66f:	"eatmyshorts"
(gdb)quit
behemoth0@melinda:/behemoth$ ./behemoth0
Password: eatmyshorts
Access granted..
$ cat /etc/behemoth_pass/behemoth1
aesebootiv
```
