#This is the Endian - 40

```
This is the end! Solving this challenge will help you defeat Daedalus`s cyborg. You can find more information about endianness and the problem here. The flag is the smallest possible program input that causes the program to print "Access Granted".


int main(int argc, char **argv) {

    size_t answer_size = sizeof(int32_t)*2+2;
    char* str_answer = calloc(1, answer_size);

    printf("Access Code: ");
    fgets(str_answer, answer_size, stdin);

    trim(str_answer);
    int32_t* answer = (int32_t*)str_answer;

    if(answer[0] == 0x52657663 && answer[1] == 0x30646521) {
        printf("Access Granted!\n");
    } else {
        printf("You supplied: 0x%x and 0x%x\n", answer[0], answer[1]);
    }
    free(str_answer);
    return 0;
}
```

Hm... Nothing else special otherthan answer[0] == 0x52657663 && answer[1] == 0x30646521 to get access.

Lets convert these into characters. Note this is "endianness" challenge and happens to be little-endian.

```
0x52657663 = cveR
0x30646521 = !ed0

You can easily find this by using the tool that they have provided us or any other mean to convert each byte into a character

pico15564@shell:/home/endianess$ ./ endian
Access Code:cveR!ed0
Acess Granted! 

Flag:cveR!ed0
```
