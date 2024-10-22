# LIST FLITTERING (even numbers)
num_list = [1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(num_list)):
    if i % 2 == 0:
        print("EVEN NUMBERS IS LIST ARE: ", i )

# LIST FLITTERING (odd numbers)
num_list = [11,12,13,14,15,16,17,18,19,20]
for i in range(0,len(num_list)):
    if i % 2 != 0:
        print("ODD NUMBERS IS LIST ARE: ", i )
 
#  TO UNPACK FRUIT TUPLE
fruits = ("apple","mango","orange")
print(fruits)# ---> OUTPUT --->UNPACK FRUIT LIST
fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3)

# TEMPERATURE CHECK
temp= input("ENTER TEMPERATURE IN CELSIUS: ")
temp = float(temp)
if temp < 0:
    print("It's FREEZING!")
elif temp > 0 and temp < 30:
    print("It's PLEASENT")
else:
    print("It's HOT!")