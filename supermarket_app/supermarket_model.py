#--------------------------------------------------------------------------------------------------
#                               Supermarket Application
#                <<<<<<         Made by Kasra Tookallo           >>>>>>
#                                   2025 the year
#                                    11/28/2025
#--------------------------------------------------------------------------------------------------
# Description : This program relies on two main approach simultaneously, including Class_Method (Object_Oriented programming) and Function_handling.
#--------------------------------------------------------------------------------------------------
# Additional hint : Database is recalling Class_method (1st approach)
#                   while
#                   List_Features, including Submit and Total Price List through Window,
#                   are based on Function_method (2nd approach).
#--------------------------------------------------------------------------------------------------
# Finally, please read the following structions before running the perogram.
# In List_Features there are two groups of Buttons in Window (tkinter):
# The first group is Add to list and Total Price List.
# The second group is Database_Related Buttons, including Submit, Edit , Remove to/from Database.
# These two groups work independantly.
#--------------------------------------------------------------------------------------------------

import re
from datetime import date,datetime


product_list = []

#--------------------------------------------------------------------------------------------------
#                                                 First approach : Class
# This approach requires date.

class Product:
    def __init__(self, id, name, brand, quantity, price ,date):
        self.id = id
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price
        self.date = datetime.strptime(date, "%Y-%m-%d").date()

    #                                                 Method_function
    def is_valid(self):
        if not (type(self.id ) == int and self.id > 0):
            raise NameError("Invalid product ID")

        if not re.match(r"^[a-zA-Z0-9\s]{3,30}$", self.name):
            raise NameError("Invalid name!")

        if not re.match(r"^[a-zA-Z0-9\s]{3,30}$", self.brand):
            raise NameError("Invalid brand!")

        if not (type(self.quantity) == int and self.quantity > 0):
            raise NameError("Invalid quantity!")

        if not (type(self.price) == float and self.price > 0):
            raise NameError("Invalid price!")

        if not self.date >= datetime.today().date():
            raise NameError("Invalid expiration date!")

        return True

    #                                               Representation
    def __repr__(self):
        return print(f"Each Product Info ====>> ID Num : {self.id:10} ---> Name :{self.name:10}, Brand :{self.brand:10}, Quantity :{self.quantity:5}, Price :{self.price:5}, Date :{self.date:5}")

    def to_tuple(self):
        return tuple((self.id,
                      self.name,
                      self.brand,
                      self.quantity,
                      self.price,
                      self.date
                      ))

#--------------------------------------------------------------------------------------------------
#                                          Second appproach : Function_handling
# This approach does not require date while being well_designed for calculating Total_price.

def id_validator(id):
    if (type(id) == int and id > 0):
        return id
    else:
        return ValueError("ID Must Be positive number!")

def name_validator(name):
    if re.match(r"^[a-zA-Z0-9\s]{2,20}$", name):
        return name
    else:
        raise ValueError("Name must be a string")

def brand_validator(brand):
    if re.match(r"^[a-zA-Z0-9\s]{2,20}$", brand):
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

def creat_products_and_validate(id ,name , brand , quantity , price):
    id_validator(id)
    name_validator(name)
    brand_validator(brand)
    quantity_validator(quantity)
    price_validator(price)


    product = {
        "id_number": id,
        "name": name,
        "brand": brand,
        "quantity": quantity,
        "price": price }


    return product
#--------------------------------------------------------------------------------------------------
#                                              total_price function
def calculate_total(product_list):
    # If there is no product available show this message
    if not product_list:
        raise ValueError("No Products", "There are no products saved.")


    total = 0

    for product in product_list:
        total = total + product["quantity"] * product["price"]
    return total
