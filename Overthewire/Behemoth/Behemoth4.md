#Behemoth 4


```
behemoth4@melinda:/behemoth$ gdb behemoth4 -q
Reading symbols from behemoth4...(no debugging symbols found)...done.
(gdb) disassemble main
Dump of assembler code for function main:
   0x080485dd <+0>:	push   %ebp
   0x080485de <+1>:	mov    %esp,%ebp
   0x080485e0 <+3>:	and    $0xfffffff0,%esp
   0x080485e3 <+6>:	sub    $0x40,%esp
   0x080485e6 <+9>:	mov    %gs:0x14,%eax
   0x080485ec <+15>:	mov    %eax,0x3c(%esp)
   0x080485f0 <+19>:	xor    %eax,%eax
   0x080485f2 <+21>:	call   0x8048460 <getpid@plt>
   0x080485f7 <+26>:	mov    %eax,0x1c(%esp)
   0x080485fb <+30>:	mov    0x1c(%esp),%eax
   0x080485ff <+34>:	mov    %eax,0x8(%esp)
   0x08048603 <+38>:	movl   $0x8048740,0x4(%esp)
   0x0804860b <+46>:	lea    0x28(%esp),%eax
   0x0804860f <+50>:	mov    %eax,(%esp)
   0x08048612 <+53>:	call   0x80484d0 <sprintf@plt>
   0x08048617 <+58>:	movl   $0x8048748,0x4(%esp)
   0x0804861f <+66>:	lea    0x28(%esp),%eax
   0x08048623 <+70>:	mov    %eax,(%esp)
   0x08048626 <+73>:	call   0x80484a0 <fopen@plt>
   0x0804862b <+78>:	mov    %eax,0x20(%esp)
   0x0804862f <+82>:	cmpl   $0x0,0x20(%esp)
   0x08048634 <+87>:	jne    0x8048644 <main+103>
   0x08048636 <+89>:	movl   $0x804874a,(%esp)
   0x0804863d <+96>:	call   0x8048470 <puts@plt>
   0x08048642 <+101>:	jmp    0x804868d <main+176>
   0x08048644 <+103>:	movl   $0x1,(%esp)
   0x0804864b <+110>:	call   0x8048440 <sleep@plt>
   0x08048650 <+115>:	movl   $0x8048759,(%esp)
   0x08048657 <+122>:	call   0x8048470 <puts@plt>
   0x0804865c <+127>:	jmp    0x804866a <main+141>
   0x0804865e <+129>:	mov    0x24(%esp),%eax
   0x08048662 <+133>:	mov    %eax,(%esp)
   0x08048665 <+136>:	call   0x80484b0 <putchar@plt>
   0x0804866a <+141>:	mov    0x20(%esp),%eax
   0x0804866e <+145>:	mov    %eax,(%esp)
   0x08048671 <+148>:	call   0x80484c0 <fgetc@plt>
   0x08048676 <+153>:	mov    %eax,0x24(%esp)
   0x0804867a <+157>:	cmpl   $0xffffffff,0x24(%esp)
   0x0804867f <+162>:	jne    0x804865e <main+129>
   0x08048681 <+164>:	mov    0x20(%esp),%eax
   0x08048685 <+168>:	mov    %eax,(%esp)
   0x08048688 <+171>:	call   0x8048430 <fclose@plt>
   0x0804868d <+176>:	mov    $0x0,%eax
   0x08048692 <+181>:	mov    0x3c(%esp),%edx
---Type <return> to continue, or q <return> to quit---
   0x08048696 <+185>:	xor    %gs:0x14,%edx
   0x0804869d <+192>:	je     0x80486a4 <main+199>
   0x0804869f <+194>:	call   0x8048450 <__stack_chk_fail@plt>
   0x080486a4 <+199>:	leave
   0x080486a5 <+200>:	ret
End of assembler dump.
(gdb)
```
Hm....

```
behemoth4@melinda:/behemoth$ objdump -R behemoth4

behemoth4:     file format elf32-i386

DYNAMIC RELOCATION RECORDS
OFFSET   TYPE              VALUE
08049ffc R_386_GLOB_DAT    __gmon_start__
0804a00c R_386_JUMP_SLOT   fclose
0804a010 R_386_JUMP_SLOT   sleep
0804a014 R_386_JUMP_SLOT   __stack_chk_fail
0804a018 R_386_JUMP_SLOT   getpid
0804a01c R_386_JUMP_SLOT   puts
0804a020 R_386_JUMP_SLOT   __gmon_start__
0804a024 R_386_JUMP_SLOT   __libc_start_main
0804a028 R_386_JUMP_SLOT   fopen
0804a02c R_386_JUMP_SLOT   putchar
0804a030 R_386_JUMP_SLOT   fgetc
0804a034 R_386_JUMP_SLOT   sprintf
```
So it seems like it gets the PID of some file and if it exists it opens that file.

Lets see what file it actually opens 

```
(gdb) b*0x08048623
Breakpoint 2 at 0x8048623
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /games/behemoth/behemoth4
Breakpoint 2, 0x08048623 in main ()

(gdb) x /s $eax
0xffffd6a8:	"/tmp/9845"
```
To be more clear, I ran strace 

```
behemoth4@melinda:/behemoth$ strace ./behemoth4
execve("./behemoth4", ["./behemoth4"], [/* 22 vars */]) = 0
[ Process PID=23708 runs in 32 bit mode. ]
brk(0)                                  = 0x804b000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fd8000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=35517, ...}) = 0
mmap2(NULL, 35517, PROT_READ, MAP_PRIVATE, 3, 0) = 0xfffffffff7fcf000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib32/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0\300\233\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1742588, ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fce000
mmap2(NULL, 1747580, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xfffffffff7e23000
mmap2(0xf7fc8000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a5000) = 0xfffffffff7fc8000
mmap2(0xf7fcb000, 10876, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fcb000
close(3)                                = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7e22000
set_thread_area(0xffffd5b0)             = 0
mprotect(0xf7fc8000, 8192, PROT_READ)   = 0
mprotect(0x8049000, 4096, PROT_READ)    = 0
mprotect(0xf7ffc000, 4096, PROT_READ)   = 0
munmap(0xf7fcf000, 35517)               = 0
getpid()                                = 23708
brk(0)                                  = 0x804b000
brk(0x806c000)                          = 0x806c000
open("/tmp/23708", O_RDONLY)            = -1 ENOENT (No such file or directory)
fstat64(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 1), ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fd7000
write(1, "PID not found!\n", 15PID not found!
)        = 15
exit_group(0)                           = ?
+++ exited with 0 +++
```
But.... 

````
behemoth4@melinda:/behemoth$ strace ./behemoth4
execve("./behemoth4", ["./behemoth4"], [/* 22 vars */]) = 0
[ Process PID=32072 runs in 32 bit mode. ]
brk(0)                                  = 0x804b000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fd8000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=35517, ...}) = 0
mmap2(NULL, 35517, PROT_READ, MAP_PRIVATE, 3, 0) = 0xfffffffff7fcf000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib32/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0\300\233\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1742588, ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fce000
mmap2(NULL, 1747580, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xfffffffff7e23000
mmap2(0xf7fc8000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a5000) = 0xfffffffff7fc8000
mmap2(0xf7fcb000, 10876, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fcb000
close(3)                                = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7e22000
set_thread_area(0xffffd5b0)             = 0
mprotect(0xf7fc8000, 8192, PROT_READ)   = 0
mprotect(0x8049000, 4096, PROT_READ)    = 0
mprotect(0xf7ffc000, 4096, PROT_READ)   = 0
munmap(0xf7fcf000, 35517)               = 0
getpid()                                = 32072
brk(0)                                  = 0x804b000
brk(0x806c000)                          = 0x806c000
open("/tmp/32072", O_RDONLY)            = -1 ENOENT (No such file or directory)
fstat64(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 1), ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xfffffffff7fd7000
write(1, "PID not found!\n", 15PID not found!
)        = 15
exit_group(0)                           = ?
+++ exited with 0 +++
```
The process id was changed. To solve it, I thought of making a symlink with password and /tmp/PID where PID is randomely picked PID and run it until it has the same process id as the file name.

```
behemoth4@melinda:/tmp$ ln -s /etc/behemoth_pass/behemoth5 /tmp/32072
```

At first I tried to write bash script to get the PID and break the loop if the pid matches the file name.... But then it failed because it stopped but did not print the password. (Probably I somehow had to pasue the program to give enough time to make the symlink and resume but I do not know exactly know why :( )
 
So after many hours of research, I found out that I could directly do this in commandline.

```
behemoth4@melinda:/tmp$ while [ true ];do /behemoth/behemoth4 | grep -v "PID";done
Finished sleeping, fgetcing
[OMITTED]
```

