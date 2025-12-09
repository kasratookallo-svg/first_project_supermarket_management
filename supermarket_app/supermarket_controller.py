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
# Product Database Controller is based on Class Product.
#--------------------------------------------------------------------------------------------------

from supermarket_dao import ProductDataAccess
from supermarket_model import *

# Since Database Controller is a Class_Method, therefore requires date.
class ProductController:
    @staticmethod
    def is_valid(id, name, brand, quantity, price, date):
        if not (type(id ) == int and id > 0):
            raise NameError("Invalid product ID")

        if not re.match(r"^[a-zA-Z0-9\s]{2,30}$", name):
            return False, "Invalid name!"

        if not re.match(r"^[a-zA-Z0-9\s]{2,30}$", brand):
            return False, "Invalid brand!"

        if not (type(quantity) == int and quantity > 0):
            return False, "Invalid quantity!"

        if not (type(price) == float and price > 0):
            return False, "Invalid price!"


        today = str(datetime.now().date())
        if not date >= today:
            return False, "Date must be Onward"

        return True, ""

    @staticmethod
    def save(id, name, brand, quantity ,price ,date):
        valid, message = ProductController.is_valid(id, name, brand, quantity ,price ,date)
        if not valid:
            return False, message

        if not valid:
            return False, message
        try:
            product = Product(
            id,
            name,
            brand,
            quantity,
            price,
            date
            )
            product_da = ProductDataAccess()
            product_da.save(product)
            return True, "Product saved successfully"
        except Exception as e:
            return False, f"Error saving product {e}"

    @staticmethod
    def edit(id, name, brand, quantity, price, date):
        valid, message = ProductController.is_valid(id, name, brand, quantity, price, date)
        if not valid:
            return False, message
        try:
            product = Product(
                id,
                name,
                brand,
                quantity,
                price,
                date
                )
            product_da = ProductDataAccess()
            product_da.edit(product)
            return True, "Product edited successfully"
        except Exception as e:
            return False, f"Error editing product {e}"

    @staticmethod
    def remove(product_id):
        try:
            product_da = ProductDataAccess()
            product_da.remove(product_id)
            return True, "Product removed successfully"
        except Exception as e:
            return False, f"Error removing product {e}"

    @staticmethod
    def find_all():
        try:
            product_da = ProductDataAccess()
            return True, product_da.find_all()
        except Exception as e:
            return False, f"Error find product {e}"
