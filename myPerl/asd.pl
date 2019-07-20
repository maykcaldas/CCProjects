#!/usr/bin/perl

use warnings;
use strict;

my @b = (1..5);
 
for my $i (@b){
    print("$i ");
}
print("\n");

for (@b){
    print("$_ ");
}
print("\n");

for (my $i = 1; $i<=5; $i++){
    print("$i ")
}

my $num;
my @numbers = ();
 
print "Enter numbers, each per line :\n";
print "ctrl-z (windows) or ctrl-d(Linux) to exit\n>";
 
while(my $input = <>) {
  print(">");
  chomp $input;
  $num = int($input);
  push(@numbers, $num);    
}
 
print "You entered: @numbers\n";