#Store_managing
# سیستمی برای مدیریت محصولات و مشتری ها و سفارش های فروشگاه
import mysql.connector
import csv
class Product:
    def __init__(self, ID , Name , Description , Price):
        self.id = ID
        self.name = Name
        self.desc = Description
        self.price = Price
class Customer:
    def __init__(self , ID , Name , Password , Money):
        self.id = ID
        self.name = Name
        self.password = Password
        self.money = Money
  