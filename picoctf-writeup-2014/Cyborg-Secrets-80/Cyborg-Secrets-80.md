#Cyborg Secrets - 80

```
You found a password protected binary on the cyborg relating to its defensive security systems. 
Find the password and get the shutdown code! You can find it on the shell server at /home/cyborgsecrets/cyborg-defense or you can download it here.
```

Oh well binary challenge. Time to use debugger.... but the hint suggests 'I wonder if they hardcoded the password string.' 
So I run strings on cyborg:

```
danny@ubuntu:~/Desktop$ strings cyborg_defense  | less

tdP     
/lib/ld-linux.so.2
libc.so.6
_IO_stdin_used
puts
putchar
printf
strcmp
__libc_start_main
__gmon_start__
GLIBC_2.0
PTRh0
[^_]
ZogH
TODO: REMOVE DEBUG PASSWORD!
DEBUG PASSWORD: 2manyHacks_Debug_Admin_Test
```

There is our password! When we login:

```
danny@ubuntu:~/Desktop$ ./cyborg_defense 2manyHacks_Debug_Admin_Test
______               _       _             _____                  
|  _  \             | |     | |           /  __ \                 
| | | |__ _  ___  __| | __ _| |_   _ ___  | /  \/ ___  _ __ _ __  
| | | / _` |/ _ \/ _` |/ _` | | | | / __| | |    / _ \| '__| '_ \ 
| |/ / (_| |  __/ (_| | (_| | | |_| \__ \ | \__/\ (_) | |  | |_) |
|___/ \__,_|\___|\__,_|\__,_|_|\__,_|___/  \____/\___/|_|  | .__/ 
                                                           | |    
                                                           |_|
Password: 2manyHacks_Debug_Admin_Test
Authorization successful.
403-shutdown-for-what

Flag:403-shutdown-for-what
```
