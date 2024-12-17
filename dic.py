
#### QUESTION # 1 ####
a = int(input("ENTER THE LENTH OF FIRST SIDE OF TRIANGLE: "))
b = int(input("ENTER THE LENTH OF SECOND SIDE OF TRIANGLE: "))
c = int(input("ENTER THE LENTH OF THIRD SIDE OF TRIANGLE: "))
if a+b>c and a<b+c and a+c>b :
    if a == b == c:
        print("EQUILATERAL TRIANGLE")
    elif a==b or b==c or a==c:
        print("ISOSCELES TRIANGLE ")
    else:
        print("SCALENE TRIANGLE")
else:
    print("TRIANGLE IS NOT VALID")



#### QUESTION # 2 ####
marks = int(input("ENTER MARKS: "))
salary = int(input("ENTER FAMILY MONTHLY SALARY: "))
grade = input("ENTER YOUR PREVIOUS GRADE")
if marks > 85:
    if salary < 100000:
        if grade == "A":
          print("CONGRATULATIONS YOU GOT 100% SCHLORSHIP")
        elif grade == "B":
            print("CONGRATULATIONS YOU GOT 75% SCHLORSHIP")
        elif grade == "C" :
            print("CONGRATULATIONS YOU GOT 50% SCHLORSHIP")
        else:
            print("YOU ARE NOT ELIGIBLE FOR SCHLORSHIP")
    else:
            print("YOU ARE NOT ELIGIBLE FOR SCHLORSHIP")
elif 70 <= marks <=85:
    if salary < 70000:
       print("YOU GOT 25% SCHLORSHIP")
    else:
        print("YOU ARE NOT ELIGIBLE FOR SCHLORSHIP")
else:
            print("YOU ARE NOT ELIGIBLE FOR SCHLORSHIP")



#### QUESTION # 3 ####
items = {
    "fruits" : {
        "apple" : 120,
        "banana" : 100,
        "pineapple" : 350,
        "grapes" : 450,
        "melon" : 120,
        "watermelon" : 500},
    "beveragea" : {
        "soft drinks" : 200,
        "milk" : 100,
        "juice" : 50},
    "grain products" : {
        "bread" : 110,
        "flour" : 150,
        "rice" : 400 }
        }
sum = 0
cart = []
while True:
   product = input("ENTER ITEMS: ")
   if product == "done":
       break
   else:
       for category , products in items.items():
          if  product in products:
           cart.append(product)
           sum+= products[product]
           print(product ,"added in cart")
           break
       else:
          print("OUT OF STOCK")
print(sum)
print(cart)


#### QUESTION # 4 ####
def stu_grades(students):
    grades = {}
    for student in students:
        marks = int(input(f"Enter marks for {student}: ")) 
        if marks < 50:
            status = "Fail"
        else:
            status = "Pass"
        grades[student] = {"Grades" : grades , "Status" : status}
    return grades
students =  ["eman","areesh","hussain","zaianb","fatima"]
student_grade = stu_grades(students)
print(student_grade)



#### QUESTION # 5 ####
def student_performance(students):
    stu_info = {}
    for student in students:
        marks = int(input("ENTER MARKS OUT OF 70: "))
        percentage = (marks/70)*100
        if percentage > 90:
            status = "EXCELLENT"
        elif 80 <= percentage <=90:
            status = "VERY GOOD"
        elif 70 <= percentage < 80:
            status = "GOOD"
        else:
            status = "NEED IMPROVEMENT"
        stu_info[student] = {"PERCENTAGE" : percentage, "STATUS" : status}
    return stu_info
students = ["EMAN","AREESH"]
student_information = student_performance(students)
print(student_information)


#### QUESTION # 6 ####
def inventory_stock(inventory):
    item1 = []
    for item , quantity in inventory.items():
         if quantity <10:
            item1.append((item,quantity))
    return item1
inventory={
        "apple" : 15,
        "bread" : 10,
        "grapes" : 20,
        "melon" : 12,
        "water melon": 5}
item2 = inventory_stock(inventory)
print(item2)


#### QUESTION # 7 ####
def employee_salary(employees):
    employee = []
    for person,salary in employees.items():
        if salary < 2000:
            employee.append((person , salary))
    return employee
employees = {"eman" :5000,
             "fatima" : 1000,
             "hussain" : 2500,
             "areesh" : 1200 }
employee_list = employee_salary(employees)
print(employee_list)



#### QUESTION # 8 ####
def merge_and_filter(dic1,dic2):
    merged_dict = []
    for key,value in dic1.items():
        for key1,value1 in dic2.items():
            if key == key1:
               new = (value + value1) /2
               merged_dict.append(new)
            else:
                print(dic1,dic2)
    return merged_dict
dic1 = {"a":1,"b":3,"c":4}
dic2 = {"a":1,"b":3,"c":4}
result = merge_and_filter(dic1,dic2)
print(result)


#### QUESTION # 9 ####
scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}
key = "Bob"
print(key,scores["Bob"])
print(scores.get("Charlie"))
scores["Alice"]=95
scores["Areesh"]=21
del scores["Charlie"]
for key,value in scores.items():
    print(key,value)



#### QUESTION # 10 ####
store_inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 20,
    "grapes": 10,
}
fruit = input("Enter fruit: ")
for key in store_inventory.items():
   
    if fruit in store_inventory:
        print(key)
    else:
        print("not found")
        break

 
#### QUESTION # 11 ####
inventory_managment = [{"product": "Furniture","quantity" : "15","price" : "1800"},
                       {"product": "computer","quantity" : "10","price" : "150"},
                       {"product": "printer","quantity" : "2","price" : "100"},
                       {"product": "File folder","quantity" : "25","price" : "15"}]
# Add new products
inventory_managment.append({"product" : "chair","quantity" : "50","price" : "250"})
print(inventory_managment)
# Calculate total inventory value
total_value= 0
minimum_stock = 5
low_stock_item=[]
for product in inventory_managment:
    total_price =  int(product["price"]) * int(product["quantity"])
    total_value+=total_price
# Generate a report of low-stock items
    if int(product["quantity"]) < minimum_stock:
      low_stock_item.append(product)

print("total value of inventory is : ", total_value)
print("LOW STOCK ITEM  IN THE INVENTORY IS :", low_stock_item)





