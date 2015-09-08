# Function Address - 60

```
We found this program file on some systems. But we need the address of the 'find_string' function to do anything useful! 
Can you find it for us?
```

Not much.I used objdump to find the address of the string.

```
danny@ubuntu:~/Desktop$ objudmp -d problem | less
08048444 <find_string>:
```

```
Flag:0x08048444
```
