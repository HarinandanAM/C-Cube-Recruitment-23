import random                            # importing random for creating a rondom no.           
max=int(input("Upper limit:"))           # Input upper and lower limit
min=int(input("Lower limit:"))
p=100                                    # p is the total points one has at the initial stage of game
n=random.randint(min,max)

while (p>0):                             # the game should continue till the points of the user will be 0 or when the user guess the correct no.
    guess=int(input("Enter guess:"))
    if guess == n:                      
        print("Total points:",p)
        break
    elif guess > n:                      #  prints if the no is too high
        print("Too high")
    else:
        print("Too low")                 #  prints if the no is too low
        
    p=p-5                                # user will looses 5 point when he or she enters the wrong number