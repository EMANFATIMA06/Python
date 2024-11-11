
# -----> Arithmetic Operations

num1 = int(input("ENTER NUMBER: "))   # num1 = 5
num2 = int(input("ENTER NUMBER: "))   # num2 = 2
print("Sum: ", num1+num2)
print("Subtraction: ", num1-num2)
print("Product: ", num1*num2)
print("Division:", num1/num2)
print("Modulus:" , num1%num2)

# -----> Comparison Operators

num3 = int(input("ENTER NUMBER: "))   # num3 = 34
num4 = int(input("ENTER NUMBER: "))   # num4 = 55
if num3 != num4:
    if num3 > num4:
      print(f"{num3} is grater than {num4}")
    else : 
      print(f"{num3} is less than {num4}")
else:
    print(f"{num3} is equal to {num4}")

# -----> Logical Operators

num5 = int(input("ENTER NUMBER: "))    # num = 13
if num5 > 10 and num5 < 20:
    print("THE NUMBER IS BETWEEN 10 AND 20")
else:
    print("THE NUMBER IS NOT BETWEEN 10 AND 20")


    
