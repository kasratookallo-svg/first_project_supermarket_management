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


import sqlite3

#                                             Database_related Functions
# Database Existence
with sqlite3.connect("supermarket_db") as connection:
    cursor = connection.cursor()

    cursor.execute("""
        create table if not exists products_with_date (
    id integer,
    name text,
    brand text,
    quantity integer,
    price integer,
    Date text
        )
    """)

    connection.commit()
print("Database and table created successfully.")

class ProductDataAccess:

    def save(self, product):
        with  sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute("insert into products_with_date (id,name,brand,quantity,price,date) values (?, ?, ?, ?, ?, ?)",
                           [product.id, product.name, product.brand, product.quantity , product.price , product.date]
                           )
            connection.commit()


    def edit(self, product):
        with  sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute("update products_with_date set name=?, brand=?, quantity=? , price=? , date=? where id=?",
                           [product.name, product.brand, product.quantity , product.price, product.date, product.id]
                           )
            connection.commit()

    def remove(self, product_id):
        with  sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute("delete from products_with_date where id=?", [product_id])
            connection.commit()

    def find_all(self):
        with  sqlite3.connect("supermarket_db") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from products_with_date order by id")
            return cursor.fetchall()
