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
#############################################################
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
