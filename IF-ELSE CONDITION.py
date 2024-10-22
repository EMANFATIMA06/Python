# example 1: Number positive/negative

num = float(input("Enter Number : "))
if num > 0: 
    print (" given number is positive")
else:
    print("given number is negative")

# example 2 : Number even/odd

number = int(input("Enter Number: "))
if number % 5==0:
    print (" Given number is multiple of five ")
else:
    print("Given number is not multiple of 5")

# Grading system : 

score = int(input("Enter Marks: "))
if score >= 90:
    print('A')
elif score < 90 and score >= 80:
    print('B')
elif score < 80 and score >= 70:
    print("C")
elif score < 70 and score >= 60:
    print("D")
elif score < 60 and score >= 50:
    print("E")
else:
    print("F")

# Age Classification:
age = int(input("Enter your Age: "))
if age < 18:
    print("you are child")
elif age>=18 and age<=55:
    print("You are Adult")
else:
    print("Yor are old person")

