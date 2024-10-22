Fruit_list = ['apple', 'mango', 'grapes','banana', 'kiwi', 'pineapple', 'orange', 'banana']

# indexing
print(Fruit_list[1])
print(Fruit_list[3])
print(Fruit_list[4])
print(Fruit_list[5])

# negative indexing
print(Fruit_list[-1])
print(Fruit_list[-2])
print(Fruit_list[-3])
print(Fruit_list[-4])

# appened --> use to add something at the end of list
Fruit_list.append('cherry')
print(Fruit_list)

# remove --> use to remove specific item from list
Fruit_list.remove('kiwi')
print(Fruit_list)

# insert --> use to add something at specific index
Fruit_list.insert(4, 'melon')
print(Fruit_list)

# length of list 
print(len(Fruit_list))

# count --> use to count how many time a ecific item preent in list
count = Fruit_list.count('banana')
print(count)

# sorting in  ascending order 
number_list=[12, 14,15,16, 6, 8,1,11,20]
number_list.sort()
print(number_list)

# Slicing
print(number_list[1:4])
print(number_list[4:6])

# Reverse
number_list.reverse()
print (number_list)
