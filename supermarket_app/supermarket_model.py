# Supermarket Application
# Made by Kasra Tookallo
# 2025 the year
# 11/28/2025
#----------------------------------------------------------------------
# This program relies on two main approach simultaneously, including Class_Method (Object_Oriented programming) and Function_handling.
#----------------------------------------------------------------------

import re
from datetime import date,datetime


product_list = []

#--------------------------------------------------------------------------------------------------
# First approach : Class
class Product:
    def __init__(self, id, name, brand, quantity, price ):
        self.id = id
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price

    # Method_function
    def is_valid(self):
        if not (type(self.id ) == int and self.id > 0):
            raise NameError("Invalid product ID")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.name):
            raise NameError("Invalid name!")

        if not re.match(r"^[a-zA-Z\s]{3,30}$", self.brand):
            raise NameError("Invalid brand!")

        if not (type(self.quantity) == int and self.quantity > 0):
            raise NameError("Invalid quantity!")

        if not (type(self.price) == float and self.price > 0):
            raise NameError("Invalid price!")


        return True

    # Representation
    def __repr__(self):
        return print(f"Each Product Info ====>> ID Num : {self.id:10} ---> Name :{self.name:10}, Brand :{self.brand:10}, Quantity :{self.quantity:5}, Price :{self.price:5}")

    def to_tuple(self):
        return tuple((self.id,
                      self.name,
                      self.brand,
                      self.quantity,
                      self.price))

#-----------------------------------------------------------------------------------------------
# Second appproach : Function_handling
def id_validator(id):
    if (type(id) == int and id > 0):
        return id
    else:
        return ValueError("ID Must Be positive number!")

def name_validator(name):
    if re.match(r"^[a-zA-Z\s]{2,20}$", name):
        return name
    else:
        raise ValueError("Name must be a string")

def brand_validator(brand):
    if re.match(r"^[a-zA-Z\s]{2,20}$", brand):
        return brand
    else:
        raise ValueError("Brand must be a string")

def price_validator(price):
    if (type(price) == float and price > 0):
        return price
    else:
        raise ValueError("Price must be a positive number")

def quantity_validator(quantity):
    if type(quantity) == int and quantity > 0:
        return quantity
    else:
        raise ValueError("Quantity must be a positive number")

def creat_products_and_validate(id ,name , brand , quantity , price): #, date):
    id_validator(id)
    name_validator(name)
    brand_validator(brand)
    quantity_validator(quantity)
    price_validator(price)
    #date = datetime.strptime(date, "%Y-%m-%d").date()


    product = {
        "id_number": id,
        "name": name,
        "brand": brand,
        "quantity": quantity,
        "price": price }
        #"date": date}

    return product
#--------------------------------------------------------------------------
def calculate_total(product_list):
    # If there is no product available show this message
    if not product_list:
        raise ValueError("No Products", "There are no products saved.")


    total = 0

    for product in product_list:
        total = total + product["quantity"] * product["price"]
    return total
