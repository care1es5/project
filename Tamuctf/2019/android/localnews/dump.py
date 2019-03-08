import frida
import base64
from pwn import *


jsnative = """

console.log("[*]FRIDA STARTS....");

var array = []

Java.perform(function(){
var context = Java.use('android.app.ActivityThread').currentApplication().getApplicationContext();
Java.choose("com.tamu.ctf.hidden.MainActivity$1",{
  
  onMatch : function(instance){ 
        var intent = Java.use("android.content.Intent");
        var ins2 = intent.$new();
        console.log(instance);
        console.log(context);
        console.log(ins2);
        instance.onReceive(context,ins2);
    },
  
  onComplete:function(){
  
  }


});
});


"""


def get_message(message,data):

	if 'payload' in message:
	    print message['payload']
	else:
	    print message


s = frida.get_usb_device(1).attach("com.tamu.ctf.hidden")
script = s.create_script(jsnative)
script.on('message',get_message)
script.load()
pause() 


