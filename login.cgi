#! /usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Cookie;

$userid = param("id");
$userpw = param("pw");
$text = "";
$file = "login2.out";

chomp $userid;
chomp $userpw;

$successmatch = 0;
$access = 0;
open(IN,$file) || die "can't open $file";
while($line=<IN>)
{
	chomp $line;
	@userinfo = split(/\/\//,$line);#split it into works
	
	$oldid = $userinfo[0]; #since its stored as username + password, userinfo[0] will return id	
	$oldpw = $userinfo[1];#userinfo[1] returns password for the corresponding id
	
	if($userid eq $oldid){
		$successmatch++;
	
	if($userpw eq $oldpw){		
		$access++;
		if($access == 1)
{
	$cookie = cookie(
	-name => "hellgate",
	-value => "$access+$userid",
	-expires => "+1h"
	);

print header(-cookie=>$cookie,-charset=>'utf-8');

print<<HTML;
<!DOCTYPE html>
<html>
    <head>
        <title></title>
		<meta charset="utf-8">
		<meta name="author" content="Bharadwaj">
    <style>
	
.container {
  position: relative;
  text-align: center;
  color: white;
  font-weight: bold;
  font-family:  "century gothic", monospace, verdana;
}

.title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
label{  
    color: #08ffd1;  
    font-size: 17px;  
} 
</style>

	</head>

    <body>

      
    <div class="container">
        <a href="home.cgi"><img src="img/pizza-salame2.jpeg"  alt="pizza-salame Background" style="width:100%;"></a>
        </div>
            
    <!-- ---------------If you log in---------------- -->
    <div class="box2">
    <h2 id="blue">Welcome Back, $userid !!</h2>
            <div class="main"  style="margin-bottom : 10%; ">
            <h1><center>Please Proceed to Order page</center></h1>
            </div>
    </div>
<!-- --------------------------- -->

</body>
</html>
HTML

}

		}
	elsif($userpw ne $oldpw){		
		$text = "Wrong credentials";
	}
	els($userid = ""||userpw = ""){
		$text = "Enter something";	
	}
		last;
	}
}

if($successmatch == 0){
	$text = "Id doesn't Exist";
}



if($access != 1)
{
print<<HTML;

<!DOCTYPE html>
<html>
    <head>
        <title>Nani's Pizzeria</title>
		<meta charset="utf-8">
		<meta name="author" content="Bharadwaj">
        <style>
body {
	background-color: #e6f5ff;
}

text {
	font-family: "century gothic", monospace, verdana;
}
	
.container {
  position: relative;
  text-align: center;
  color: white;
  font-weight: bold;
  font-family:  "century gothic", monospace, verdana;
}

.title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
label{  
    color: #000000;  
    font-size: 17px;  
}
.login{
width: 382px;  
overflow: hidden;  
        margin: auto;  
        margin: 20 0 0 450px;  
        padding: 80px;  
        background: #e6f5ff;  
        border-radius: 15px ;
	border-style: solid; 
	border-color: orange;
 
}
 
</style>

</head>

    <body>

        <div class="container">
        <a href="home.cgi"><img src="img/pizza-salame2.jpeg"  alt="pizza-salame Background" style="width:100%;"></a>
        <div  style="font-size: 75px"  class="title">Login</div>
	</div>

    <div class="box2">

    <h2 id="red">$text</h2>
<form action="login.cgi" method="post">
<div class="login">
	<h1 style="color : #ffa366;" margin-left =" auto;" margin-right =" auto;"><center>LOGIN</center></h1>
	<label><b>User Name     
        </b>    
        </label>
	&nbsp;&nbsp;
	<input class="username" name="id" type="text" placeholder="ID">
	<br><br>
	<label><b>Password     
        </b>    
        </label>
	&nbsp;&nbsp;&nbsp;&nbsp;
	<input class="password" name="pw" type="password" placeholder="Password">
	<br><br>
	<center><input class="button" type="submit" value="Login"></center>
	<br>
	<br><br>
	<label><b>Don't have ID? </b></label>&nbsp;&nbsp;
	<input type="button" id="registbtn" value="SignUp" onclick="location.href='register.htm'"></div>
</div>
</form>

        
</div>


</body>
</html>

HTML
}

