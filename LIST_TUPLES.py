
# ----> List Operations
num_list =[1,2,3,4,5,6,7,8,9]
num_list.append(10)
num_list.remove(2)
print(num_list)
print("length of list is : ", len(num_list))

min_num = num_list[0] 
max_num = num_list[0]
for i in num_list:
     if i < min_num: 
      min_num = i
     if i > max_num: 
      max_num= i
print("MINIMUM NUMBER IN THE LIST IS : ", min_num)
print("MAXIMUM NUMBER IN THE LIST IS : ",max_num)

# ----> Tuple Manipulation
my_tuple = (1, 3, 5, 7, 9)
print(my_tuple)
print("SECOND ELEMENT IN THE TUPLE IS: " , my_tuple[1])
print("LAST ELEMENT IN THE TUPLE IS: " , my_tuple[4])
print("LENGTH OF TUPLE IS  : ", len(my_tuple))

# ----> List of Tuples
people = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
print(people)
total_age = 0
num_people = 0
for person in people:
    name, age = person  
    total_age += age  
    num_people += 1     
average_age = total_age / num_people
print(f"The average age is: {average_age}")