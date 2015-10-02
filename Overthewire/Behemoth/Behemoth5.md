# Behemoth5 

```
behemoth5@melinda:/behemoth$ ./behemoth5
```

Hm It doesnt do anything..... Lets see what is going on with gdb.

```
behemoth5@melinda:/behemoth$ gdb behemoth5 -q
Reading symbols from behemoth5...(no debugging symbols found)...done.
(gdb) disassemble main
Dump of assembler code for function main:
   0x0804873d <+0>:	push   %ebp
   0x0804873e <+1>:	mov    %esp,%ebp
   0x08048740 <+3>:	and    $0xfffffff0,%esp
   0x08048743 <+6>:	sub    $0x50,%esp
   0x08048746 <+9>:	mov    0xc(%ebp),%eax
   0x08048749 <+12>:	mov    %eax,0x1c(%esp)
   0x0804874d <+16>:	mov    %gs:0x14,%eax
   0x08048753 <+22>:	mov    %eax,0x4c(%esp)
   0x08048757 <+26>:	xor    %eax,%eax
   0x08048759 <+28>:	movl   $0x0,0x24(%esp)
   0x08048761 <+36>:	movl   $0x80489f0,0x4(%esp)
   0x08048769 <+44>:	movl   $0x80489f2,(%esp)
   0x08048770 <+51>:	call   0x80485d0 <fopen@plt>
   0x08048775 <+56>:	mov    %eax,0x28(%esp)
   0x08048779 <+60>:	cmpl   $0x0,0x28(%esp)
   0x0804877e <+65>:	jne    0x8048798 <main+91>
   0x08048780 <+67>:	movl   $0x8048a0f,(%esp)
   0x08048787 <+74>:	call   0x8048560 <perror@plt>
   0x0804878c <+79>:	movl   $0x1,(%esp)
   0x08048793 <+86>:	call   0x8048590 <exit@plt>
   0x08048798 <+91>:	movl   $0x2,0x8(%esp)
   0x080487a0 <+99>:	movl   $0x0,0x4(%esp)
   0x080487a8 <+107>:	mov    0x28(%esp),%eax
   0x080487ac <+111>:	mov    %eax,(%esp)
   0x080487af <+114>:	call   0x8048550 <fseek@plt>
   0x080487b4 <+119>:	mov    0x28(%esp),%eax
   0x080487b8 <+123>:	mov    %eax,(%esp)
   0x080487bb <+126>:	call   0x80485c0 <ftell@plt>
   0x080487c0 <+131>:	mov    %eax,0x24(%esp)
   0x080487c4 <+135>:	addl   $0x1,0x24(%esp)
   0x080487c9 <+140>:	mov    0x28(%esp),%eax
   0x080487cd <+144>:	mov    %eax,(%esp)
   0x080487d0 <+147>:	call   0x8048530 <rewind@plt>
   0x080487d5 <+152>:	mov    0x24(%esp),%eax
   0x080487d9 <+156>:	mov    %eax,(%esp)
   0x080487dc <+159>:	call   0x8048570 <malloc@plt>
   0x080487e1 <+164>:	mov    %eax,0x2c(%esp)
   0x080487e5 <+168>:	mov    0x28(%esp),%eax
   0x080487e9 <+172>:	mov    %eax,0x8(%esp)
   0x080487ed <+176>:	mov    0x24(%esp),%eax
   0x080487f1 <+180>:	mov    %eax,0x4(%esp)
   0x080487f5 <+184>:	mov    0x2c(%esp),%eax
   0x080487f9 <+188>:	mov    %eax,(%esp)
   0x080487fc <+191>:	call   0x8048510 <fgets@plt>
---Type <return> to continue, or q <return> to quit---
   0x08048801 <+196>:	mov    0x2c(%esp),%eax
   0x08048805 <+200>:	mov    %eax,(%esp)
   0x08048808 <+203>:	call   0x80485a0 <strlen@plt>
   0x0804880d <+208>:	mov    0x2c(%esp),%edx
   0x08048811 <+212>:	add    %edx,%eax
   0x08048813 <+214>:	movb   $0x0,(%eax)
   0x08048816 <+217>:	mov    0x28(%esp),%eax
   0x0804881a <+221>:	mov    %eax,(%esp)
   0x0804881d <+224>:	call   0x8048520 <fclose@plt>
   0x08048822 <+229>:	movl   $0x8048a15,(%esp)
   0x08048829 <+236>:	call   0x8048620 <gethostbyname@plt>
   0x0804882e <+241>:	mov    %eax,0x30(%esp)
   0x08048832 <+245>:	cmpl   $0x0,0x30(%esp)
   0x08048837 <+250>:	jne    0x8048851 <main+276>
   0x08048839 <+252>:	movl   $0x8048a1f,(%esp)
   0x08048840 <+259>:	call   0x8048560 <perror@plt>
   0x08048845 <+264>:	movl   $0x1,(%esp)
   0x0804884c <+271>:	call   0x8048590 <exit@plt>
   0x08048851 <+276>:	movl   $0x0,0x8(%esp)
   0x08048859 <+284>:	movl   $0x2,0x4(%esp)
   0x08048861 <+292>:	movl   $0x2,(%esp)
   0x08048868 <+299>:	call   0x8048610 <socket@plt>
   0x0804886d <+304>:	mov    %eax,0x34(%esp)
   0x08048871 <+308>:	cmpl   $0xffffffff,0x34(%esp)
   0x08048876 <+313>:	jne    0x8048890 <main+339>
   0x08048878 <+315>:	movl   $0x8048a2d,(%esp)
   0x0804887f <+322>:	call   0x8048560 <perror@plt>
   0x08048884 <+327>:	movl   $0x1,(%esp)
   0x0804888b <+334>:	call   0x8048590 <exit@plt>
   0x08048890 <+339>:	movw   $0x2,0x3c(%esp)
   0x08048897 <+346>:	movl   $0x8048a34,(%esp)
   0x0804889e <+353>:	call   0x8048600 <atoi@plt>
   0x080488a3 <+358>:	movzwl %ax,%eax
   0x080488a6 <+361>:	mov    %eax,(%esp)
   0x080488a9 <+364>:	call   0x8048540 <htons@plt>
   0x080488ae <+369>:	mov    %ax,0x3e(%esp)
   0x080488b3 <+374>:	mov    0x30(%esp),%eax
   0x080488b7 <+378>:	mov    0x10(%eax),%eax
   0x080488ba <+381>:	mov    (%eax),%eax
   0x080488bc <+383>:	mov    (%eax),%eax
   0x080488be <+385>:	mov    %eax,0x40(%esp)
   0x080488c2 <+389>:	movl   $0x8,0x8(%esp)
   0x080488ca <+397>:	movl   $0x0,0x4(%esp)
   0x080488d2 <+405>:	lea    0x3c(%esp),%eax
   0x080488d6 <+409>:	add    $0x8,%eax
---Type <return> to continue, or q <return> to quit---
   0x080488d9 <+412>:	mov    %eax,(%esp)
   0x080488dc <+415>:	call   0x80485e0 <memset@plt>
   0x080488e1 <+420>:	mov    0x2c(%esp),%eax
   0x080488e5 <+424>:	mov    %eax,(%esp)
   0x080488e8 <+427>:	call   0x80485a0 <strlen@plt>
   0x080488ed <+432>:	movl   $0x10,0x14(%esp)
   0x080488f5 <+440>:	lea    0x3c(%esp),%edx
   0x080488f9 <+444>:	mov    %edx,0x10(%esp)
   0x080488fd <+448>:	movl   $0x0,0xc(%esp)
   0x08048905 <+456>:	mov    %eax,0x8(%esp)
   0x08048909 <+460>:	mov    0x2c(%esp),%eax
   0x0804890d <+464>:	mov    %eax,0x4(%esp)
   0x08048911 <+468>:	mov    0x34(%esp),%eax
   0x08048915 <+472>:	mov    %eax,(%esp)
   0x08048918 <+475>:	call   0x80485f0 <sendto@plt>
   0x0804891d <+480>:	mov    %eax,0x38(%esp)
   0x08048921 <+484>:	cmpl   $0xffffffff,0x38(%esp)
   0x08048926 <+489>:	jne    0x8048940 <main+515>
   0x08048928 <+491>:	movl   $0x8048a39,(%esp)
   0x0804892f <+498>:	call   0x8048560 <perror@plt>
   0x08048934 <+503>:	movl   $0x1,(%esp)
   0x0804893b <+510>:	call   0x8048590 <exit@plt>
   0x08048940 <+515>:	mov    0x34(%esp),%eax
   0x08048944 <+519>:	mov    %eax,(%esp)
   0x08048947 <+522>:	call   0x8048630 <close@plt>
   0x0804894c <+527>:	movl   $0x0,(%esp)
   0x08048953 <+534>:	call   0x8048590 <exit@plt>
End of assembler dump.
(gdb)
```
Pretty long but there are few functions call to note such as fopen,sendto,socket,gethostbyname etc...

```
behemoth5@melinda:/behemoth$ objdump -R behemoth5

behemoth5:     file format elf32-i386

DYNAMIC RELOCATION RECORDS
OFFSET   TYPE              VALUE
08049ffc R_386_GLOB_DAT    __gmon_start__
0804a00c R_386_JUMP_SLOT   fgets
0804a010 R_386_JUMP_SLOT   fclose
0804a014 R_386_JUMP_SLOT   rewind
0804a018 R_386_JUMP_SLOT   htons
0804a01c R_386_JUMP_SLOT   fseek
0804a020 R_386_JUMP_SLOT   perror
0804a024 R_386_JUMP_SLOT   malloc
0804a028 R_386_JUMP_SLOT   __gmon_start__
0804a02c R_386_JUMP_SLOT   exit
0804a030 R_386_JUMP_SLOT   strlen
0804a034 R_386_JUMP_SLOT   __libc_start_main
0804a038 R_386_JUMP_SLOT   ftell
0804a03c R_386_JUMP_SLOT   fopen
0804a040 R_386_JUMP_SLOT   memset
0804a044 R_386_JUMP_SLOT   sendto
0804a048 R_386_JUMP_SLOT   atoi
0804a04c R_386_JUMP_SLOT   socket
0804a050 R_386_JUMP_SLOT   gethostbyname
0804a054 R_386_JUMP_SLOT   close
```

It seems like it opens some file and reads it using ftell,fseek etc doing some ascill to into conversion and send to some specific port.

```
(gdb) b*0x08048761
Breakpoint 1 at 0x8048761
(gdb) r
Starting program: /games/behemoth/behemoth5

Breakpoint 1, 0x08048761 in main ()
(gdb) x /s 0x80489f0
0x80489f0:	"r"
(gdb) x /10s 0x80489f0
0x80489f0:	"r"
0x80489f2:	"/etc/behemoth_pass/behemoth6"
0x8048a0f:	"fopen"
0x8048a15:	"localhost"
0x8048a1f:	"gethostbyname"
0x8048a2d:	"socket"
0x8048a34:	"1337"
0x8048a39:	"sendto"
0x8048a40:	"\001\033\003;("
0x8048a46:	""
```
* host:localhost 
* port:1337 
* fopen attemps to open /etc/behemoth_pass/behemoth6

Using tmux...

```
behemoth5@melinda:/behemoth$ nc -l 1337                                                   │behemoth5@melinda:/behemoth$ ./behemoth5
                                                                                          │behemoth5@melinda:/behemoth$
                                                                                          │
                                                                                          │
                                                                                          │
```
Hm....it seems really weird....To find out what was wrong, I looked up the manual for each function and netcat found one interesting information

```
(from netcat)
-u 
Use UDP instead of the default option of TCP. For UNIX-domain sockets, use a datagram socket instead of a stream socket. If a UNIX-domain socket is used, a temporary receiving socket is created in $TMPDIR unless the -s flag is given.
```
So the default stream is TCP.... so how about UDP?

```
behemoth5@melinda:/behemoth$ nc -ul 1337                                                  │behemoth5@melinda:/behemoth$ ./behemoth5
[OMITTED]                                                                                 │behemoth5@melinda:/behemoth$
```
That is it for this challenge.







