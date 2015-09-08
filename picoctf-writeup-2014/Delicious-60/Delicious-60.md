# Delicious! - 60

```
You have found the administrative control panel for the Daedalus Coperation Website: https://web2014.picoctf.com/delicious-5850932/login.php. Unfortunately, it requires that you be logged in. Can you find a way to convince the web site that you are, in fact, logged in?
```

Not much to explain. When I go into the website, it shows the session number.
I immediately thought this was cookie mainpulation to login as a someone who already logged into the website.

I used burpsuite to intercept and changed the session_id to 65 and that gave me the flag.

But just for fun, I went back to check if there are other session(s) that I can login into.

I tried from 58-66 and It all worked. If you want, you can try more.

```
Flag:session_cookies_are_the_most_delicious
```
