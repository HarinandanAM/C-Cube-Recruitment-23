#!/bin/bash

k=0                                                          # k is used for counting
 
if grep -q "553" users.txt ; then                            # grep to get the users having the  respective user id 
	k=$(($k+1))                                          # -q so that the output grep will not  be printed
fi

if grep  -q "828" users.txt ; then
	k=$(($k+1))
fi

if grep  -q "723" users.txt ; then
	k=$(($k+1))
fi

if grep  -q "698" users.txt ; then
	k=$(($k+1))
fi

echo "Total count of USER IDs are:" $k
