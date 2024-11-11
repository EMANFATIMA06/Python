
# ----> Even or Odd

number = int(input("Enter Number: "))  # number = 6
if number % 2 == 0:
    print(f"{number} is even number")
else:
    print(f"{number} is odd number")

# ----> Grade Categorization

stu_grade= int(input("ENTER STUDENT MARKS: "))    # stu_geade = 85
if stu_grade >= 90:
    print("EXCELLENT")
elif 70 <= stu_grade <= 89:
    print("GOOD")
elif 50 <= stu_grade <= 69:
     print("AVERAGE")
else:
     print("FAIL")

# -----> Age Group

age = int(input("ENTER YOUR AGE: "))     # age = 16
if age < 13:
    print("CHILD")
elif 13 <= age <= 19:
    print("TEENAGER")
elif 20 <= age <= 64: 
    print("ADULT")
else:
    print("SENIOR")