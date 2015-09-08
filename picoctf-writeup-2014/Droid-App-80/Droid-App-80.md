# Droid App - 80

```
An Android application was released for the toaster bots, but it seems like this one is some sort of debug version. 
Can you discover the presence of any debug information being stored, so we can plug this?
You can download the apk here.
```

Hint says it all:
Android apk files are notoriously easy to decompile. 
We heard there are even online services that does this automatically nowadays.

I used this online apk decomplier: http://www.decompileandroid.com

Once it is decompiled, you can download the contents. 

Flag was in src/picoapp453/picoctf/com/picoapp/ToasterActivity.java

```
Flag:what_does_the_logcat_say
```
