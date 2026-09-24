#Store_managing
# سیستمی برای مدیریت محصولات و مشتری ها و سفارش های فروشگاه
import sqlite3
import csv

connection = sqlite3.connect("Store.db")
cursor = connection.cursor()

class Product:
    def __init__(self, Name , Description , Price):
        self.name = Name
        self.desc = Description
        self.price = Price
class Customer:
    def __init__(self , Username , Password , Money):
        self.username = Username
        self.password = Password
        self.money = Money
########################################################################################
def add_product(product):
    # adding product into product table
    try:
        query = "INSERT INTO product(Name , Description , Price) VALUES (? , ? , ?)"
        parametrs = (product.name , product.desc , product.price)
        cursor.execute(query , parametrs)
        connection.commit()
        print("product added succesfully.")
    except Exception as e:
        print("error:" , e)
def show_product():
    # print product in terminal
    try: 
        query = "SELECT * FROM product"
        cursor.execute(query)
        result = cursor.fetchall()
        print("--- Products ---")
        for product in result:
            print(product)
    except Exception as e:
            print("error:" , e)
            
def edit_product_price():
    try:
        id = int(input("enter product id :"))
        new_price = float(input("enter new product price :"))
        query = "UPDATE product SET Price = ? WHERE ID = ?"
        parametrs = (new_price , id )
        cursor.execute(query , parametrs)
        connection.commit()
        print("edited succesfully.")
    except Exception as e:
        print("error:" , e)
def delete_product():
    try:
        id = int(input("enter product id:"))
        query = "DELETE FROM product WHERE ID = ?"
        cursor.execute(query , (id,))
        connection.commit()
        print("deleted succesfully.")
    except Exception as e:
        print("error:" , e)
########################################################################################
def check_username(username):  
    query = "SELECT * FROM customer WHERE Username = ?"
    cursor.execute(query , (username,))
    result = cursor.fetchone()
    if not result:
        return True
    return False       # این نام کاربری از قبل وجود داشته است
def password_validation(password):
    correct_password = True
    if len(password)<8:
        print("password must be at least 8 characters")
        correct_password = False
    has_alpha = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    if  not has_alpha  or not has_digit:
        print("password must has at least 1 character and 1 number")
        correct_password = False
    return correct_password

def Register(customer):
    try:
        query = "INSERT INTO customer(Username , Password , Money) VALUES(? , ? , ?)"
        parametrs = (customer.username ,  customer.password , customer.money)
        cursor.execute(query , parametrs)
        connection.commit()
        print("added succesfully. thank you for sign up")
    except Exception as e :
        print("problem :" , e)
        
def Login():
    login = False
    username = input("enter your username:")
    password = input("enter your password:")
    try:
        sql = "SELECT * FROM customer WHERE Username = ?"
        cursor.execute(sql , (username,))
        result = cursor.fetchone()
        if not result:
            print("no such username exist.")
            return
    except Exception as e:
        print("error :" , e)
    try:
        query = "SELECT * FROM customer WHERE Username = ? AND Password = ?"
        cursor.execute(query , (username , password))
        result = cursor.fetchone()
        if not result:
            print("username or password is incorrect")
        else:
            print(f"welcome {username}")
            login = True
    except Exception as e:
        print("problem :" , e)
    if login:
        return username
    else:
        return False
def charge_money(username):
    try:
        amount = float(input("enter amount of money to charge:"))
        query = "UPDATE customer SET Money = Money + ? WHERE Username = ?"
        cursor.execute(query , (amount , username))
        connection.commit()
        print("charged succesfully.")
    except Exception as e:
        print("error:" , e)
########################################################################################
# ثبت سفارش
def order(username):
    try:
        product_id = int(input("enter product id :"))
        quantify = int(input("how many do you want? :"))
        # بدست اوردن قیمت محصول
        sql = "SELECT Price FROM product WHERE ID = ?"
        cursor.execute(sql , (product_id ,))
        result = cursor.fetchone()
        price = result[0]
        total_price = quantify * price
        print(type(total_price))
        # پیدا کردن ایدی و پول کاربر
        query = "SELECT ID , Money FROM customer WHERE Username = ?"
        cursor.execute(query , (username ,))
        result = cursor.fetchone()
        customer_id = result[0]
        money = result[1]
        print(type(money))
        # اضافه کردن به جدول سفارش ها
        if money >= total_price:
            query2 = "INSERT INTO orders(customer_id , product_id , quantify) VALUES(? , ? , ?)"
            parametrs = (customer_id , product_id , quantify)
            cursor.execute(query2 , parametrs)
            connection.commit()
            print("order placed.")
            # کم کردن پول از حساب کاربر
            query3 = "UPDATE customer SET Money = Money - ? WHERE Username = ?"
            cursor.execute(query3 , (total_price , username))
            connection.commit()
        else:
            print("your money is not enough")
    except Exception as e:
        print("error:" , e)

########################################################################################
'''
# منوی ویژه مدیر
===== STORE MANAGEMENT SYSTEM =====
1. Product Management
2. Customer Management
3. Order Management
4. Sales Report
5. Export Report
6. Exit
'''
'''
# منوی ویژه مشتری ها
print("===== CUSTOMER MENU =====")
print("1. Show Products")
print("2. Place Order")
print("3. Charge Money")
print("4. Back to Main Menu")
'''

logged_in_user = None
manager_username = "erfan_aghaee"

print("===== welocome to store =====")
print("plese first login to your account or register if you don't have an account.")

while True:
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print()
    choice = input("enter your choice:")
    if choice == "1":
        logged_in_user = Login()
        if logged_in_user == manager_username:
            print("===== STORE MANAGEMENT SYSTEM =====")
            print("1. Product Management")
            print("2. Customer Management")
            print("3. Order Management")
            print("4. Sales Report")
            print("5. Export Report")
            print("6. Exit")
            print()
            while True:
                choice = input("enter your choice:")
                if choice == "1":
                    print("1. Add Product")
                    print("2. Show Products")
                    print("3. Edit Product Price")
                    print("4. Delete Product")
                    print("5. Back to Main Menu")
                    print()
                    product_choice = input("enter your choice:")
                    if product_choice == "1":
                        name = input("enter product name:")
                        desc = input("enter product description:")
                        price = float(input("enter product price:"))
                        product = Product(name , desc , price)
                        add_product(product)
                    elif product_choice == "2":
                        show_product()
                    elif product_choice == "3":
                        edit_product_price()
                    elif product_choice == "4":
                        delete_product()
                    elif product_choice == "5":
                        break
                    else:
                        print("invalid choice. please try again.")
                elif choice == "2":
                    # مدیریت مشتری ها
                    pass
                elif choice == "3":
                    # مدیریت سفارش ها
                    pass
                elif choice == "4":
                    # گزارش فروش
                    pass
                elif choice == "5":
                    # خروجی گرفتن از گزارش
                    pass
                elif choice == "6":
                    print("exiting...")
                    exit()
                else:
                    print("invalid choice. please try again.")
        if logged_in_user and logged_in_user != manager_username:
            while True:
                print()
                print("===== MENU =====")
                print("1. Show Products")
                print("2. Place Order")
                print("3. Charge Money")
                print("4. Exit")
                print()
                customer_choice = input("enter your choice:")
                if customer_choice == "1":
                    show_product()
                elif customer_choice == "2":
                    order(logged_in_user) # place order functionality can be implemented here
                elif customer_choice == "3":
                    charge_money(logged_in_user)
                elif customer_choice == "4":
                    break
                else:
                    print("invalid choice. please try again.")

    elif choice == "2":
        username = input("enter your username:")
        if not check_username(username):
            print("this username is already taken.")
            continue
        password = input("enter your password:")
        if not password_validation(password):
            continue
        try:
            money = float(input("enter your initial money:"))
        except ValueError:
            print("invalid amount. please enter a valid number.")
            continue
        customer = Customer(username , password , money)
        Register(customer)
    elif choice == "3":
        print("exiting...")
        exit()
    else:
        print("invalid choice. please try again.")
