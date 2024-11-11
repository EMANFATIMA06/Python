
# ----> Countdown

countdown = 11
while(countdown>1):
    countdown-=1
    print(countdown)
print("End of Story!")

# -----> Sum of Numbers

total = 0
while (True):
    number = int(input("ENTER NUMBER: "))        # 5, 10, -3, 0
    if number == 0:
        break
    else:
      total+=number
print(f"sum = {total}")

# -----> Factorial Calculation

fictorial = 1
num = int(input("ENTER NUMBER: "))     # num = 5
while(num>1):
    fictorial*=num
    num-=1
print("fictorial = " , fictorial)




