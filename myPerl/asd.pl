

#!/usr/bin/perl

use warnings;
use strict;

###########################################
print("Perl scalar reference\n");

my $x = 5;
my $xr = \$x;

print($x, "\n", $xr, "\n", $$xr, "\n");

${$xr} = ${$xr} * 2;

print($x, "\n", $xr, "\n", $$xr, "\n");

###########################################
print("Perl array reference\n");

my @a = qw/1 2 3 4 5/;
my $ar = \@a;
print("@a\n $ar \n@$ar \n");

print('@a:');
for my $i (@a){
    print("$i ");
}
print("\n");

print('@$ar:');
for(@$ar){
    print("$_ ");
}
print("\n");

print('$ar->[$i]: ');
for my $i (0..scalar(@$ar)){
    print("$ar->[$i] ");
}
print("\n");

print('$$ar[$i]: ');
for my $i (0..@$ar){
    print("${$ar}[$i] ");
}
print("\n");

###########################################
print("Perl hash reference\n");

my %h = qw/jan 1 feb 2 mar 3 apr 4 may 5 jun 6 jul 7 aug 8/;
my $hr = \%h;

print("%h\n $hr \n%$hr \n");

print('$h{$_}: '."\n");
for(keys %h){
    print("Key: $_: $h{$_} \n");
}
print("\n");

# It does not accept to call a hash as a dereference of its reference
# print('%$hr{$i}: '."\n");
# for (keys %$hr){
#     print("Key: $_: %$hr{$_} \n");
# }
# print("\n");

print('$hr->{$i}: '."\n");
for (keys %$hr){
    print("Key: $_: $hr->{$_} \n");
}
print("\n");

###########################################
print("Perl anonymous references\n");

my @ar1 = (1..9);
my $ar2 = [1..9];

print("@ar1 \n@$ar2 \n");

my $mtx = [[1,2,3],[4,5,6],[7,8,9]];

print("$mtx \n");
print("@$mtx \n");
print("@$mtx[0] \n");

for(@$mtx){
    print("@$_ \n");
}


