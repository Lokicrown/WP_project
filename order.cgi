#!/usr/bin/perl -w

#-----------------------------
#ordering pg - Tiffany
#-----------------------------

use CGI qw(:standard -debug);
use CGI::Carp qw(fatalsToBrowser);

#get input

$size= param("size");
@topping= param("topping");
@drink= param("drink");

$topping= join(", ",@topping);
$drink= join(", ",@drink);

#append to file

$file= "history.out";

#-----------------------------
#html


print header ();
{
print <<EOP;
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="author" content="Nani's Pizza - Tiffany">
<link rel="stylesheet" type="text/css" href="css/style.css">
<head>
<title>Order Page</title>
<style>

body {
	background-color: #e6f5ff;
}

text {
	font-family: "century gothic", monospace, verdana;
}

.button {
  background-color: #ffa366;
  border: none;
  color: black;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 5px;
}

</style>
</head>

<h2>Thank you <b>$id</b> for ordering!</h2>

<p>Your order is currently being prepared by our chef
<br><br><br>
<b>Your order:</b>
<br><br>
Size: $size
<br>
Toppings: $topping
<br>
Drink: $drink
<br>

EOP
open(OUT,">>$file") || die "can't write to $file";
print OUT "\nSize: $size\n";
print OUT "Toppings: $topping\n";
print OUT "Drink: $drink\n\n";
print OUT "-----------------\n\n";
close OUT;
}
</html>