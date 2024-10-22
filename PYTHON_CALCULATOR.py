num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print("+ , - , * , /")
oper = (input("Which operation you want to perform: "))
z = oper
if oper == "+" :
   z = num1 + num2
   print(z)
elif oper == "-" :
   z = num1 - num2
   print(z)
elif oper == "*" :
   z = num1 * num2
   print(z)
elif oper == "/":
   z= num1 / num2
   print(z)
