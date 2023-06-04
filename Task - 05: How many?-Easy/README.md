We grep the text file users.txt and count the no. of users that has matching user id (used while grepping) given in the question 
```
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
echo "Total count of USER IDs are:" $k                      # total no. of people that can enter are stored in k
``
The output will be:

![Screenshot from 2023-06-04 15-18-26](https://github.com/HarinandanAM/C-Cube-Recruitment-23/assets/116416113/6c632ea7-3176-48f0-a404-35c9b9127edc)
