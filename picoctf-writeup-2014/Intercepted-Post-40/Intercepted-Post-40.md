# Intercepted Post - 40

```
We intercepted some of your Dad`s web activity. Can you get a password from his traffic?. You can also view the traffic on CloudShark.
```

When I open up the pcap in cloudshark, I saw bunch of Get and http request. But the key here is the "POST" request since the goal is to get the password.
Since the number of packet was fairly small,I was able to scroll down and found the packet with "POST"

```
151		24.876569	172.16.1.132	104.131.53.208	HTTP	550	POST /login/ HTTP/1.1
``` 

When I followed the stream, I was able to get the username and password:

```
username=claudio&password=flag%7Bpl%24_%24%24l_y0ur_l0g1n_form%24%7D
```

However, since it was urlencoded,it must be decoded:

```
%7B = {
%24 = $
%7D = }

Flag:flag{pl$_$$l_y0ur_l0g1n_form$}
```
