#No Comment - 20

```
The CD you find has a copy of your father`s website: homepage.html. Maybe something is hidden in the site...

https://picoctf.com/api/autogen/serve/homepage.html?static=false&pid=3099c443d360a2514f17f155fb65d5d2
```

This challenge is very stragihtforward: Checking source code

```
<html>
	<head>
		<title>Dr. Claudio Drake`s Personal Website</title>
	</head>
	
	<body>
		<center>
			<div style="width: 500px">
				<h1>Dr. Claudio Drake</h1>
				
				<img src="/problem-static/web/no-comment/me.png">
				
				<p>
					I am a roboticist with a Doctorate Degree in Robotics. My primary interests are in developing new medical robotics to help doctors 
better perform surgery on high risk patients. 
				</p>
								
				<!-- In case you forget, the password for this site is: flag_3683876057e4ba20028358fdb9f03e5ea73909f1 -->
					
			</div>
		</center>
	</body>
</html>


Flag:flag_3683876057e4ba20028358fdb9f03e5ea73909f1
```
