#Grep is Still Your Friend - 40

Challenge:

```
The police need help decrypting one of your father'\s' files. 
Fortunately you know where he wrote down all his backup decryption keys as a backup (probably not the best security practice). 
You are looking for the key corresponding to daedaluscorp.txt.enc. The file is stored on the shell server at /problems/grepfriend/keys.
```

First we have to login to the shell (creds were on shell page): 

```
ssh pico15664@shell2014.picoctf.com -p 22
password:3f10aa

pico15664@shell:/$ cd /problems/grepfriend/keys
```

When I read the file from the keys, it was filled with huge list of the file name and its decryption key. 
As the hint suggests, grep is our best friend.



```
pico15664@shell:/problems/grepfriend$ cat keys | grep 'daedaluscorp.txt.enc'
daedaluscorp.txt.enc	  b2bee8664b754d0c85c4c0303134bca6

Flag:b2bee8664b754d0c85c4c0303134bca6
```





