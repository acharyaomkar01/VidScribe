<html>
	<head>
	</head>
	<body>
		<form action="/ls" method="POST" enctype="multipart/form-data">
			<center>
				<input class= "myButton" type="submit" name="submitb" value="LS"/>
			</center>
		</form>
	%from bottle import route,error,template,run,request,get,post,static_file,redirect,response
	%import os
	%import bottle
	%if(var != 0 and cname == 'ls'):
		{{var}}		 
	%end	
	</body>
</html>
