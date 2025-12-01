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