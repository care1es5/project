#Javascrypt - 40

Challenge:

```
Tyrin Robotics Lab uses a special web site to encode their secret messages. Can you determine the value of the secret key?

https://picoctf.com/api/autogen/serve/index.html?static=false&pid=b1d725db54a1fb027ea6bbd78f9a7d0b
```

First thing I notice in the website is there are input and output box where the user types in the message and the output shows the encoded message.

Lets take look at javascript and how this 'encoding' function works.

```
 	    var key; // Global variable. 
            
            // Since the key is generated when the page 
            // is loaded, no one will be able to steal it
            // by looking at the source! This must be secure!
            function generateKey() {
		var i = 1;
                var x = 205;
                var n = 5493;
                while (i <= 25) {
                    x = (x * i) % n;
                    i++;
                }
                key = "flag_" + Math.abs(x);
	    }
            
            generateKey();
            
            // Encode the message using the 'key'
            function encode() {                                                        
                var input = $("#inputmessage").val();
                var output = CryptoJS.AES.encrypt(input, key);
                $('#outputmessage').val(output);
	    }
```

Ok. So it does some math on the input. However, for the sake of this challenge, we do not really need to know how the encoding works.
The important part here is that key is global variable. That means anyone can easily access!!!!

In the javascript console:

```
>key
"flag_411"

Flag:"flag_411"
```


