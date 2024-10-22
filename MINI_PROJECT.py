from re import I


menu= {
    'Pizza' : 150,
    'Burger' : 140,
    'Wrap' : 300,
    'Coffee' : 170,
    'Tea' : 100,
    'Paratha roll' : 130,
}
print("WELCOME TO PYTHON RESTAURANT!")
print("Here's The Menu List.")
print(" Pizza: Rs150\n Burger : Rs140\n Wrap: Rs300\n Coffee: Rs170\n Tea: Rs100\n Paratha roll : Rs130")

order_total =0
item_1 = input("WHAT YOU WANT TO ORDER ? ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added. ")
else:
    print("ORDERED ITEM IS NOT AVALIABLE")

item_2 = input("DO YOU WANT TO ORDER SOMETHING ELSE: ")
if item_2== "Yes":
       item2 = input("WHAT DO YOU WANT TO ORDER: ")
       if item2 in menu:
         order_total += menu[item2]
         print(f"Your item {item2} has been added.")
       else:
         print("ORDERED ITEM IS NOT AVALIABLE")

print("YOUR ORDER TOTAL IS: ",order_total)


