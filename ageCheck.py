#Ask the user for their age
#Store the age in a variable
#Use control flow (if, else) to print out whether or not they are old enough to vote
#Challenge: Are they old enough to drive? Rent a car? Retire?

age = int(input("What is your age?"))
if age >= 18:
    print ("You can vote!")
else:  
    print ("You can't vote! >:V")

# or age = input("What is your age?")
# age = int(age)

if age >=21:
    print ("You can rent a car!")
else:
    print ("YoU cAn'T ReNt a CaR!")