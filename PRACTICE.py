# SEPERATE EVEN NUMBERS FROM LIST
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(list1)):
    if i % 2 == 0:
        print(i)

#SEPERATE EVEN NUMBER FROM LIST AND ADD THEM , SEPERATE ODD NUMBER FROM LIST AND MULTIPLY THEM
list2 = []
while True:
    num1 = int(input("ENTER A NUMBER: "))
    list2.append(num1)
    choice = input("ENTER ANOTHER NUMBER: IF NOT PRESS 0: ")
    if choice == "0":
      break
print(list2)
Tuple = tuple(list2)
print(Tuple)
add = 0
product = 1
for i in Tuple:
    if i % 2 == 0:
      add = add+i
    else:
      product = product*i
print(product)
print(add)

# TO CHECK NUMBER IS POSITIVE, NEGATIVE, EVEN, ODD
number = int(input("ENTER A NUMBER:"))
if number > 0:
    if number %2 ==0:
        print("GIVEN NUMBER IS POSITIVE AND EVEN")
    else:
        print("GIVEN NUMBER IS POSITIVE AND ODD")
if number < 0:
    print("GIVEN NUMBER IS NEGATIVE NUMBER")

# SEPERATE ODD NUMBER FROM LIST
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(list1)):
    if not i % 2 == 0:
        print(i)

# TO CHECK EITHER STRING IS EMPTY OR NOT
String = input("ENTER STRING OF NUMBERS: ")
num = String
if not num:
    print("STRING IS EMPTY")
else:
    print(num)

# SEPERATE STUDENTS ACOIRDING TO THEOR MARKS
Tuple3 = [("EMAN",78),
    ("AREESH",43),
    ("HUSSAIN", 100),
    ("ALI", 37),
    ("AROOJ",50)]

maximum_marks = 50
for i in Tuple3:
    name, marks=i 
    if marks>maximum_marks:
       status  = "above"
        
    elif marks==maximum_marks:
       status  = "equal"   
    else:
        status  = "below"
    print(name, status, maximum_marks)

# PASSWORD CHECK
correct_password = "eman00"
attempts = 0
while(attempts<3):
    password = input("ENTER YOUR PASSWORD")
    if password == correct_password:
        print("ACCESS GRANTED")
        break
    attempts+= 1
else:
     print("Access denied")

# NESTED IF ELSE
user_name = input("ENTER YOUR USERNAME")
password = input("ENTER YOUR PASSWORD")
if user_name=="admin":
    if password == "admin123":
        print("ACCESS GRANTED")
else:
    print("ACCESS DENIED!")

#LIST
list4 = ['apple','mango','orange','banana']
list4.extend(["kiwi","tomato"])
print(list4)

list4.pop(2)
print(list4)

list4.append('grapes')
print(list4)

list4.insert(3,"cherry")
print(list4)

list4.remove('apple')
print(list4)

# TUPLE SLICING
number = [13,11,65,432,23,19,144,10]
slice1 = number[1:6]
slice2 = number[:6]
print(slice1)
print(slice2)

# TUPLE SORTING
number = [13,11,65,432,23,19,144,10]
number.sort()
number.reverse()
print(number)

# TUPLE LENGTH
number = [13,11,65,432,23,19,144,10]
print(len(number))
number.pop(2)
print(number)

# COMBINE TUPLE
tuple2 = (1,2,3,4)
tuple3 = (5,6,7,8)
result = tuple2 + tuple3
print(result)

# UNPACKING TUPLE
stu_info = ("ALI ZAR", '024' ,'BBD')
name, reg_no, course = stu_info 
print(name)
print(reg_no)
print(course)

# UNPACKING OF TUPLES
info =(("Eman",23),("Essah",98))
maximum_marks = 50
for i in info:
    name, marks =i
    if marks < maximum_marks:
        status = 'below'
        print(name, status, maximum_marks,)
    else:
        status = 'above'
print(name, status, maximum_marks,)


    
    


