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
    def __init__(self , Name , Password , Money):
        self.name = Name
        self.password = Password
        self.money = Money

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
