
 ########## INVENTORY MANAGEMENT SYSTEM #############

class inventory:
    def __init__(self,name,price,total_stock,code):
        self.name=name
        self.price=price
        self.code=code
        self.total_stock=total_stock
        
    def total_sales(self,sales):
        self.total_stock-=sales
        return self.total_stock , sales
    def update_quantity(self,new_quantity):
        self.total_stock+=new_quantity
        return self.total_stock , new_quantity
    def current_inventory(self):
        return self.name , self.price , self.code , self.total_stock
    def purchase_return(self,purchase_returns):
        self.total_stock-=purchase_returns
        return purchase_returns , self.total_stock
def main():
    product_dic = {"101": inventory("Bread",150,12,0),
                   "102": inventory("Jam",400,8,0)}
    while True:
        print("\nSUPER MARKET")
        print("1. Add New Inventory")
        print("2. Update Inventory Quantity")
        print("3. Update Sales and Check Updated Inventory Quantity")
        print("4. Check Current Inventory")
        print("5. Add Purchase Returns to Update Inventory")
        print("6.EXIT")
        
        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            name = input("ENTER PRODUCT NAME: ")
            code = input("ENTER PRODUCT CODE: ")
            price = float(input("ENTER PRODUCT PRICE: "))
            total_stock = int(input("ENTER TOTAL_STOCK: "))
            product_dic[code] = inventory(name,price,total_stock,code)
            print("PRODUCT ADDED SUCCESSFULLY! ")
        if choice == 2:
            code = input("ENTER CODE OF PRODUCT: ")
            if code in product_dic:
                new_quantity = int(input("ENTER QUANTITY"))
                total_stock, new_quantity = product_dic[code].update_quantity(new_quantity)
                print(f" STOCK IS UPDATED BY { new_quantity} UPDATED PRODUCT QUANTITY IS: {total_stock} ")
        if choice == 3:
            code = input("ENTER CODE OF PRODUCT: ")
            if code in product_dic:
                sales = int(input("ENTER QUANTITY OF SOLD ITEMS: "))
                total_stock , sales = product_dic[code].total_sales(sales)
                print(f"TOTAL SALES ARE {sales} REMAINING STOCK IS {total_stock}")
        if choice == 4:
            for code , value in  product_dic.items():
                name,price,total_stock,code = product_dic[code].current_inventory()
                print(value.name,value.price,value.total_stock)
        if choice == 5:
            code = input("ENTER CODE OF PRODUCT: ")
            if code in product_dic:
                purchase_returns = int(input("ENTER NUMBER OF RETURN ITEMS: "))
                purchase_returns , total_stock = product_dic[code].purchase_return(purchase_returns)
                print(f"{ purchase_returns} ARE DEFECTED ITEMS AND ARE RETURN BACK TO SALES MAN AND REMAINING TOTAL INVENTORY IS {total_stock}")
        if choice == 7:
            break

    bread_price=product_dic["101"].total_stock
    print(bread_price)

    cake_price = product_dic["102"].price
    print(cake_price)




main()