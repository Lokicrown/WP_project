#! /usr/bin/perl -w

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

$file = "login2.out";
$idexist = 0;
$return_success = 0;
$new_id = param("id");
$new_pw = param("pw");
$cpw = param("pw2");
$text = "";


open(IN,$file) || die "can't open $file";
while($line=<IN>)
{
	chomp $line;
	@usrinfo=split(/\/\//,$line);
	
	$idcheck=shift(@usrinfo);
	
	if($idcheck eq $new_id)
	{
		$idexist++;
	}
}


if($new_pw eq $cpw && $idexist == 0)
{
	$text = "Account has been created successfully";
	$return_success++;
	open(OUT,">>$file") || die "can't write to $file.";
    print OUT "\n$new_id//$new_pw";
    close OUT;
}

elsif($new_pw ne $cpw){
	$text = "Enter confirmation correctly”";
}
elsif($idexist != 0)
{
	$text = "Account already exists";
}

print "Content-type: text/html\n\n";
print<<EOP;

<!DOCTYPE html>
<html>
<head>
<title>Register</title>
<meta name="author" content="Nani's Pizza">
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
label{  
    color: #000000;  
    font-size: 17px;  
} 
</style>
</head>

<body  bgcolor="#e6f5ff">

<div class="container">
  <img src="img/pizza-salame2.jpeg"  alt="pizza-salame Background" style="width:100%;">
  <div  style="font-size: 75px"  class="title">Register</div>
</div>

EOP

if($return_success != 0)
{

print<<EOP;

    <div class="box2">

    <h2 id="red">Account successfully created</h2>
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
	<input class="button" type="submit" value="Login">
	<br>
	<br><br>
	<label><b>Don't have ID? </b></label>&nbsp;&nbsp;
	<input type="button" id="registbtn" value="SignUp" onclick="location.href='register.htm'"></div>
</div>
</form>

        
</div>


</body>
</html>

EOP

}

elsif($return_success == 0)
{

print<<HTML;
<h2 id="red">$text</h2>
<form action="register.cgi" method="post">
<div class="login">
	<h1 style="color : #ffa366;" margin-left =" auto;" margin-right =" auto;"><center>Register here</center></h1>
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
	<label><b>Confirm Password     
        </b>    
        </label>
	&nbsp;&nbsp;
	<input class="password2" name="pw2" type="password" placeholder="Confirm Password">
	<br><br>
	<center><input class="button" type="submit" value="Sign Up"></center>
	<br>
	<br><br>
	<label><b>Already have an ID? </b></label>&nbsp;&nbsp;
	<input type="button" id="loginbtn" value="Login" onclick="location.href='login.htm'"></div>
</div>
</form>
</body>
</html>
HTML

}
