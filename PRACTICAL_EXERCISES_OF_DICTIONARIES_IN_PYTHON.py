##### A ####
#------> A dictionary to store information about a person (name, age, city, hobbies).
my_dictionary = {
    "name" : "EMAN FATIMA",
    "age" :"19 Years",
    "city" : "LAHORE",
    "hobbies" : "BOOK READING"
    }
print(my_dictionary)


##### B ####
#-----> frequency of words in a given text.
text = [1,2,3,1,2,4,5,7,6,5,5,'hello',3,10,'hello']
frequency = {element: text.count(element) for element in text}
print(frequency)


##### C ####
#-----> Implement a simple inventory system.
inventory ={
    "chairs" : "15",
    "laptops" : "10",
    "tables" : "13",
    "pen" : "50"}
print(inventory)
# Iterating Over a Dictionary
for key,value in inventory.items():
    print(key,value)
# Adding and Modifying Values
inventory["PC"] = 5
print(inventory)
# Removing Values
del inventory ["tables"]
print(inventory)


##### D ####
#------> Analyze a dataset of customer orders to find the most popular product category.
orders = [
          {"customer_id":"1","product_category":"electronics","quantity":"2"},
          {"customer_id": "1", "product_category": "clothing", "quantity": "5"},
          {"customer_id":"3", "product_category":"electronics","quantity":"2"}
]
electronics =[]
clothing =[]
for order in orders:
    if order["product_category"] == "electronics":
        electronics.append(order["product_category"])
    elif order["product_category"] == "clothing":
        clothing.append(order["product_category"])

if len(electronics) > len(clothing):
    popular_product_category = "electronics"
else:
     popular_product_category = "clothing"
print(f"The most popular product category is: {popular_product_category}")



##### E ####
#------> Dictionary to store student grades and calculate the average grade.
student_info = [
    {"name":"Eman", "accounting":"24","programming":"23","mathematics":"24"},
    {"name":"Areesh", "accounting":"20","programming":"25","mathematics":"21"},
    {"name":"Hussain", "accounting":"22","programming":"19","mathematics":"10"}
]
for student in student_info:
    grades = [int(student["accounting"]),int(student["programming"]),int(student["mathematics"])]   
    total_grades = sum(grades)
    average = total_grades/len(grades)
    print(student["name"],average)



##### F ####
#------> Inventory Management:
# Create a dictionary to store product information: name, quantity, price.S
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



##### G ####
#------> Student Gradebook
stu =[{ "name":"Zainab", "english":"25","urdu":"12","physics":"21"},
    {"name":"Fatimah sughra", "english":"24","urdu":"8","physics":"23"},
    {"name":"Ali Akbar", "english":"10","urdu":"19","physics":"5"}
]
# average grade for each student.
for student in stu:
    grades = [int(student["english"]),int(student["urdu"]),int(student["physics"])]   
    total_grades = sum(grades)
    average = total_grades/len(grades)
# sorted average
    print(student["name"],average)

    
##### H ####
# -------> Shopping cart
products = {
    "Laptop": {"price": 800, "quantity": 10},
    "Smartphone": {"price": 500, "quantity": 15},
    "Headphones": {"price": 100, "quantity": 20}
}
cart = {"Laptop": 2, "Smartphone": 1}
# Calculate total cost
total = 0
for product, quantity in cart.items():
    total += products[product]["price"] * quantity  
# Apply discount (10%) and tax (5%)
total_after_discount = total * 0.90  
total_after_tax = total_after_discount * 1.05  
print("Total before discount and tax: ",total_after_discount )
print("Final total after discount and tax: ",total_after_tax)