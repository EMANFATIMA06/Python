
#### 1 ####
def greet():
   print("hello,world")
greet()


#### 2 ####
def say_hello(name):
   print("hello, ",name) 
return_name = say_hello("areesh")


#### 3 ####
def greet():
    print("hello,world")
greet()


#### 4 ####
def sum_num(a,b):
    return a+b
a = int(input("ENTER NUMBER: "))
b = int(input("ENTER NUMBER: "))
result = sum_num(a,b)
print(result)


#### 5 ####
def multiply_num(c,d):
    return c*d
c = int(input("ENTER NUMBER: "))
d = int(input("ENTER NUMBER: "))
total = multiply_num(c,d)
print(total)


#### 6 ####
#### A ####
def min_max(e,f):
    if e>f:
        print(f"{e} greater than {f}")
    elif e == f:
        print(f"{e} is equal to {f}")
    else:
        print(f"{e} less than {f}")
e = int(input("ENTER NUMBER: "))
f = int(input("ENTER NUMBER: "))
min_max(e,f)


#### B ####
def min_max(e,f):
    if e>f:
        return f"{e} greater than {f}"
    elif e == f:
        return f"{e} is equal to {f}"
    else:
        return f"{e} less than {f}"
e = int(input("ENTER NUMBER: "))
f = int(input("ENTER NUMBER: "))
result = min_max(e,f)
print(result)


#### 7 ####
def max_list(g):
     max_num = g[0]
     for num in g:
        if num > max_num:
            max_num = num
     return max_num
g = [1,2,3,4,5,6]
max = max_list(g)
print(f"MAXIMUM NUMBER IN THE LIST IS : " , max)


#### 8 ####
def case(string):
    return string.title()
string = " syeda eman fatima abidi"
name = case(string)
print(name)


#### 9 ####
def even_odd(n):
    if n % 2 == 0:
        return f" {n} is EVEN NUMBER"
    else:
        return f" {n} is ODD NUMBER"
n = int(input("ENTER NUMBER: "))
output = even_odd(n)
print(output)


#### 10 ####
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count+=1
    return count
string = "hello workd"
result = count_vowels(string)
print(result)


#### 11 #### 
def even_num(list1):
    list2 = []
    for num in list1:
        if num % 2 ==0:
            list2.append(num)
    return list2
list1 =[1,2,3,4,5,6,7,8,9,10]
total = even_num(list1)
print(total)


#### 12 ####
def factorial_num(number):
    factorial = 1
    while(number >= 1):
        factorial*=number
        number-=1
    return factorial
number = int(input("ENTER NUMBER: "))
result = factorial_num(number)
print(result)
