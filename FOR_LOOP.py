
# ----> Multiplication Table

num = int(input('ENTER NUMBER: '))        # num = 3
for i in range (1,10+1):
    total = i*num
    print(f"{num} x {i} = {total}")

# ----> Fibonacci Sequence

a = 0
b = 1
print(a)
for i in range(0,9):
    a,b = b,a+b
    print(a)

# ----> Prime Numbers

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:  
            break  
    else:
        print(num)

