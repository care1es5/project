#Toaster Control - 50

```
Daedalus Corp. uses a web interface to control some of their toaster bots. It looks like they removed the command 'Shutdown & Turn Off' from the control panel. Maybe the functionality is still there...

http://web2014.picoctf.com/toaster-control-1040194/
```

There are three button:Blink lights, Patrol Mode and Make Toast.

When I click one of these buttons, it querys the action in the url:

```
http://web2014.picoctf.com/toaster-control-1040194/handler.php?action=Blink%20Lights
```

So I urlencoded the querry Shutdown and Turn Off (including whitespace)

```
http://web2014.picoctf.com/toaster-control-1040194/handler.php?action=Shutdown%20%26%20Turn%20Off

Toaster Defense System Controls
	Shutting down
Shutdown code: flag_c49bdkeekr5zqgvc20vc

Flag:c49bdkeekr5zqgvc20vc
```
