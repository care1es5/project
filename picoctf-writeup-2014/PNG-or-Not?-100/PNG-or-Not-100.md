# PNG or Not? - 100

```
On a corner of the bookshelf, you find a small CD with an image file on it. It seems that this file is more than it appears, and some data has been hidden within. Can you find the hidden data?

https://picoctf.com/problem-static/forensics/png-or-not/image.png
```
When you open up the link, you are present with the qr code. 
My first attempt was to use the qrcode scanner but you get this:
Nice try, but you`re breaking the wrong tree!

Hm... so downlaoded the image and ran the file command:

```
Danny@tests-MacBook-Pro:~/Downloads$ file image.png
image.png: PNG image data, 280 x 280, 8-bit/color RGB, non-interlaced
```

Lets analyze even deeper using hexedit:

```
Danny@tests-MacBook-Pro:~/Downloads$ hexedit image.png
```

And I found 7z with flag.txt.

```
00000600   00 00 00 00  49 45 4E 44  AE 42 60 82  37 7A BC AF  ....IEND.B`.7z..
00000610   27 1C 00 03  B8 64 D3 C1  1A 00 00 00  00 00 00 00  `....d..........
00000620   50 00 00 00  00 00 00 00  B5 6B 69 46  00 22 92 C6  P........kiF.``..
00000630   AE 77 46 B4  23 6D F7 5D  C0 C0 A4 DC  1F A8 38 05  .wF.#m.]......8.
00000640   57 B9 76 3E  20 00 01 04  06 00 01 09  1A 00 07 0B  W.v> ...........
00000650   01 00 01 23  03 01 01 05  5D 00 00 01  00 0C 14 00  ...#....].......
00000660   08 0A 01 DC  E1 0D DE 00  00 05 01 11  13 00 66 00  ..............f.
00000670   6C 00 61 00  67 00 2E 00  74 00 78 00  74 00 00 00  l.a.g...t.x.t...
00000680   14 0A 01 00  90 D6 20 07  48 DB CF 01  15 06 01 00  ...... .H.......
00000690   20 00 00 00  00 00                                   .....
000006A0 
```

At this point all you need to do is extracting 7z and read the flag.txt:

```
Danny@tests-MacBook-Pro:~/Downloads$ 7z x image.png

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov 2010-11-18
p7zip Version 9.20 (locale=utf8,Utf16=on,HugeFiles=on,4 CPUs)

Processing archive: image.png

Extracting flag.txt

Everything is Ok

Size:       20
Compressed: 1686

Danny@tests-MacBook-Pro:~/Downloads$ cat flag.txt
EKSi7MktjOpvwesurw0v
```

```
Flag:EKSi7MktjOpvwesurw0v
```
