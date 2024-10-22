# USE OF NOT OPERATOR
a = False
print(not a)

# GUESS THE NUMBER GAME
number = 13
random_number = (input("Enter your number: "))
if not random_number:
    print("You did't enter any thing, enter your guess")
else:
    random_number = int(random_number)
    if random_number == 13:
        print("Congratulations you have guessed the number.")
    else:
        print("You didn't guessed correct.")

# TO CHANGE DATATYPE OF INPUT
number = (input("enter your input: "))
print(number)
number=int(number)
print(type(number))

# TO CHECK INPUT INTEGER IS ODD OR EVEN NUMBER
number = int(input("ENTER NUMBER HERE: "))
if not number % 2 ==0:
    print("GIVEN NUMBER IS ODD NUMBER.")
else:
    print("GIVEN NUMBER IS EVEN NUMBER.")

# A USERNAMAE IS NOT EMPTY AND DOES NOT CONTAIN SPACES
username = str(input("ENTER USERNAME HERE: "))
if not username:
    print("USERNAME NOT YET ENTERED")
elif " " in username:
    print("INVALID USERNAME")
else:
    print("DONE")

#TO CHECK NUMBER IS POSITIVE OR NEGATIVE
mynumber = float(input("ENTER THE REQUIRED NUMBER: "),[])
if not mynumber >= 0:
    print("YOU ENTERED A NEGATIVE NUMBER.")
else:
    print("YOU ENTERED A POSITIVE NUMBER.")











