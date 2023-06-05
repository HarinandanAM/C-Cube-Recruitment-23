list=input("Enter pattern:").split()
p=[]
soln=[]

y=0
for i in range (len(list)):       # for creating a list p that show no. of times the repeated
    k=0
    for j in range(len(list)):   
        if list[i]==list[j]:  
            k=k+1
    p.append(k)
z=0

print(p ) 
for k in range(len(p)):         # for loop for finding the if the no. of times each element are repeated or not 
    if p[0]==p[k]:      
        if p[0]==p[k]==1:       # we dont want the no. that repeated only 1 time, thats not a pattern  
            z=z+1
        else:
            y=y+1               # y will give the total no of times repeated values are repeated
        result= 1

if z==len(p):
    print("not a pattern")
elif result==1:
    for x in range(int(y/max(p))):          
        soln.append(list[x])               # soln list will give the pattern
    print("Pattern Found: ",soln)
    print("No of times pattern repeat is:",max(p))
else:
    print("not a pattern")