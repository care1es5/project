# Tyrannosaurus Hex - 10

Challenge:

```The contents of the flash drive appear to be password protected. On the back of the flash drive, you see the hexadecimal number 0x658015e3 scribbled in ink. The password prompt, however, only accepts decimal numbers. What number should you enter? (Press the Hint button for advice on solving the challenge)```

This one is pretty easy.

```
Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int(0x658015e3)
1702893027 <-Flag
>>>
```

