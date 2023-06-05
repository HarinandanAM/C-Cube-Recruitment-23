#!/bin/bash

k=$(grep -c "553" users.txt)       # grep -c can count the lines 
l=$(grep -c "828" users.txt)       # if there is more than person with same user id  grep will count the  no. lines  ie equal to no of times same user id repeated  
m=$(grep -c "723" users.txt)
n=$(grep -c "698" users.txt)

z=$(($k+$l+$m+$n))

echo "Total count of USER IDs are:" $z     # total no. of people cant enter are stored in z


