#!/usr/bin/perl -w

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser); 

$fn= param("fn");
$ln= param("ln");
$email= param("email");
$subject = param("subject");

$ctu= "ctu.out";

open(OUT,">>$ctu") || die "can't write to $ctu";
print OUT "Name: $ln $fn\n";
print OUT "Email: $email\n";
print OUT "Subject: $subject\n";
print OUT "---------------\n\n";
close OUT;

print header ();

print<<EOP; 
<html>
<head><title>Contact</title>
<meta name="author" content="Nani's Pizza - Tiffany">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<link rel="stylesheet" type="text/css" href="css/style.css">
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

img {
  border-radius: 5px;
}


.button {
  background-color: #ffa366;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}

.input{
    background:#ecf0f1;
    border: #ccc 1px solid;
    border-bottom: #ccc 2px solid;
    padding: 8px;
    width: 80%;
    color: black;
    margin-top:10px;
    font-size:1em;
    border-radius:4px;
 }

.input1{
    background:#ecf0f1;
    border: #ccc 1px solid;
    border-bottom: #ccc 2px solid;
    padding: 8px;
    width: 80%;
    height: 200px;
    color: black;
    margin-top:10px;
    font-size:1em;
    border-radius:4px;
 }

</style>
</head>
<body>
<div class="container">
  <img src="img/pizza-salame2.jpeg"  alt="pizza-salame Background" style="width:100%;">
  <div  style="font-size: 75px"  class="title">
Thank you for contacting us!!
</div>
</div>
<br>
<br>
<h3 style="font-size: 25px" align="center">
	<h2>We have your comments now, so we will get back to you as soon as we can~</h2>
</h3>
</html>
EOP