# INPUT NUMBERS IN LIST AND SEPERATE THEM ON THE BASIS OF EVEN AND ODD
list1 = []
while True:
    num = int(input('ENTER NUMBERS: '))
    list1.append(num)
    choice = input("DO YOU WANT TO ADD ANOTHER NUMBER, (enter/n)")
    if choice  == "n":
      break
print(list1)
even = []
odd = []
for num in list1:
   if num % 2 == 0:
    even.append(num)
    even.sort()
   else:
    odd.append(num)
    odd.sort()

print(odd)
print(even)

# TO ENTER NAMES IN ARRAY USING WHILE LOOP
array = []
while True:
    names = input("ENTER NAME: ")
    array.append(names)
    choice = input("DO YOU WANT TO ADD ANOTHER NAME: (press enter / no)")
    if choice == "no":
        break
print(array)

# INPUT NUMBERS IN LIST USING WHILE LOOP  
list2 = []
while True:
    num2 = int(input("ENTER NUMBERS: "))
    list2.append(num2)
    choice = input("DO YOU WANT TO ADD ANOTHER NUMBER: (press enter/no)")
    if choice == "no":
        break
print(list2)
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.insert(1, 'eman')
print(list2)


# TO PRINT NUMBERS FROM 1 TO 10  
count =0
while count<10:
    count+=1
    print(count)

# ENTER NUMBERS IN LIST UNTILL NEGATIVE NUMBER
num_list = []
while True:
    num = int(input('ENTER NUMBER: '))
    if  num <0:
       break
    num_list.append(num)
print(num_list)


# SUM OF EVEN NUMBERS FROM 1 TO 100
add = 0
num = 0
while num<=100:
    if num %2 ==0:
      add+= num
    num+=1
print(add)
  
# TABLE OF 5
num = 5
count = 0
while count<=10:
   result = num*count
   
   print(num,"x",count,"=",result)
   count+=1


#TABLE OF SIX
num =6
count =1
while count<=20:
     result = count*num
     print(num, "x", count, "=",result)
     count +=1



#ODD NUMBERS FROM 1 TO 100
odd = 1
while odd<=100:
    if odd % 2 !=0:
     
     print(odd)
    odd+=1

