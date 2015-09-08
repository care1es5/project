# Easy Overflow - 40

```
Is the sum of two positive integers always positive?
nc vuln2014.picoctf.com 50000
nc is the Linux netcat command. Try running it in the shell
```

```
pico15664@shell:/problems/grepfriend$ nc vuln2014.picoctf.com 50000
Your number is 8835096. Can you make it negative by adding a positive integer?
99999999999999999999

Im unable to parse your number. It might be too large (the largest java int is 2147483647), or just not a number.
```

In first try, I just gave in large number to see if it overflows the maximum number of integer. However, the program can not parse my number.
Fortunately, program was kind enough to tell us the largest java int is 2147483647.

So:

```
pico15664@shell:/problems/grepfriend$ nc vuln2014.picoctf.com 50000
Your number is 4039130. Can you make it negative by adding a positive integer?
2147483647
Congratulations! The sum is -2143444519. Here is the flag: That_was_easssy!

Thanks for playing.

Flag: That_was_easssy!
```

