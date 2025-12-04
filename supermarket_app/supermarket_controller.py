#----------------------------------------------------------------------
#                               Supermarket Application
#                <<<<<<         Made by Kasra Tookallo           >>>>>>
#                                   2025 the year
#                                    11/28/2025
#----------------------------------------------------------------------
# Description : This program relies on two main approach simultaneously, including Class_Method (Object_Oriented programming) and Function_handling.
#----------------------------------------------------------------------
# Additional hint : Database is recalling Class_method (1st approach)
#                   while
#                   List_Features, including Submit and Total Price List through Window,
#                   are based on Function_method (2nd approach).
#----------------------------------------------------------------------
# Finally, please read the following structions before running the perogram.
# In List_Features there are two groups of Buttons in Window (tkinter):
# The first group is Add to list and Total Price List.
# The second group is Database_Related Buttons, including Submit, Edit , Remove to/from Database.
# These two groups work independantly.
#----------------------------------------------------------------------

from supermarket_dao import ProductDataAccess
from supermarket_model import *


class ProductController:
    @staticmethod
    def save(id, name,brand,quantity ,price):
        try:
            product = Product(id,
            name,
            brand,
            quantity,
            price)
            product_da = ProductDataAccess()
            product_da.save(product)
            return True, "Product saved successfully"
        except Exception as e:
            return False, f"Error saving product {e}"

    @staticmethod
    def edit(id, name, brand, quantity, price):
        try:
            product = Product(id,
                                                  name,
                                                  brand,
                                                  quantity,
                                                  price)
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