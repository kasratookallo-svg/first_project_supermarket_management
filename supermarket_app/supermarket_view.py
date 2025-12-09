#--------------------------------------------------------------------------------------------------

#                               Supermarket Application
#                <<<<<<         Made by Kasra Tookallo           >>>>>>
#                                   2025 the year
#                                    11/28/2025
#--------------------------------------------------------------------------------------------------
# Description : This program relies on two main approach simultaneously, such as Class_Method (Object_Oriented programming) and Function_handling.
#--------------------------------------------------------------------------------------------------
# Additional hint : Database is recalling Class_method (1st approach) 
#                   while
#                   List_Features, including Submit and Total Price_List through Window,
#                   are based on Function_method (2nd approach) .
#--------------------------------------------------------------------------------------------------
# Finally, please read the following structions before running the perogram.
# In List_Features there are two groups of Buttons in Window (tkinter):
# The first group is Add to list and Total Price_List.
# The second group is Database_Related Buttons, including Submit, Edit , Remove to/from Database.
# These two groups work independantly.
#--------------------------------------------------------------------------------------------------

import datetime
from time import strptime

from persiantools.digits import to_word
from supermarket_controller import *
from supermarket_model import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import persiantools



#                                                    Table reseting
def reset():
    id.set(0)
    name.set("")
    brand.set("")
    quantity.set(0)
    price.set(0)
    today = datetime.now().date()
    date.set(str(today))
    status, product_list = ProductController.find_all()

    for item in table.get_children():
        table.delete(item)

    for product in product_list:
        table.insert("", END, values=tuple(product))
#-----------------------------------------------------------------------------------------------
#                                                  Table_Database function
def select_product(event):
    product = table.item(table.focus())["values"]
    id.set(product[0])
    name.set(product[1])
    brand.set(product[2])
    quantity.set(product[3])
    price.set(product[4])
    date.set(product[5])
#-----------------------------------------------------------------------------------------------
# Entry for Add_to_List and Total price_list based on second approach (Function_handling)
# Second approach is wll_designed for calculating total price.
#--------------------------------------------------------------------------------------------------

def receive_product():
    try:
        product = creat_products_and_validate(
            id.get(),
            name.get(),
            brand.get(),
            quantity.get(),
            price.get(),
            date.get()
            )
        product_list.append(product)
        print(product, "Product saved successfully.")

        # If you use Pickle
        # save_to_file(product_list)

        print("-" * 150)
        #To insert Data into the table
        table.insert("" , END, values=tuple(product.values()))
        messagebox.showinfo("Information Saved", "Product saved successfully.")
        print("Your Market includes : ", product_list)
        print("-" * 150)
        #reset()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong : {e}")
#-----------------------------------------------------------------------------------------------
#                                          Recalling Database functions
def save_click():
    status, message = ProductController.save(
        id.get(),
        name.get(),
        brand.get(),
        quantity.get(),
        price.get(),
        date.get(),
    )
    if status:
        reset()
        messagebox.showinfo("Product Save", message)
    else:
        messagebox.showerror("Product Save Error",message)

def edit_click():
    status, message = ProductController.edit(
        id.get(),
        name.get(),
        brand.get(),
        quantity.get(),
        price.get(),
        date.get()
    )
    if status:
        reset()
        messagebox.showinfo("Product Edit",message)
    else:
        messagebox.showerror("Product Edit Error",message)

def remove_click():
    status, message = ProductController.remove(id.get())
    if status:
        reset()
        messagebox.showinfo("Product Remove",message)
    else:
        messagebox.showerror("Product Remove Error",message)

#-----------------------------------------------------------------------------------------------
# total_price function attached to supermarket_module
def total_price():
    try:
        total = calculate_total(product_list)
        messagebox.showinfo("Total Price", f"Total Price:\n تومان {total}\n{to_word(total)}")
    except Exception as e:
        messagebox.showerror("Error", f"Error!!! : {e}")
#-----------------------------------------------------------------------------------------------
                        # Table starts here

win = Tk()
win.geometry("750x630")
win.title("Welcome to Super Market _ List of Products")
win.configure(bg="green")
#-----------------------------------------------------------------------------------------------------------------------------------
#                                      Description
Label(win , text="Note : This window has 5 buttons which are paired in groups of two."
                 "\n'Add to List' and 'Total Price_List',"
                 "\n'Submit', 'Edit', and 'Remove from Database'."
                 "\nIf you have a saved list from the past in Database and want to calculate the total price of them,"
                 "\nyou should select them case_by_case before clicking on 'Add to List' button.",
      background="yellow", fg="black").place(x=20, y=360,width=505, height=80)

Label(win , text="Fact.\n\n\n<<<<Please Pay Attention>>>>"
                 "\n\n\nYou should "
                 "\nclick on 'Submit to Database' button,"
                 "\notherwise,"
                 "\nyour product's detail"
                 "\nwill be deleted automatically,"
                 "\nafter closing the program."
                 "\n!!!!",background="red").place(x=530, y=360, height=257 ,width=205)

Label(win, text="Instruction : "
                "\n1- Enter your product's detail."
                "\n2- Click on 'Add to List' button to make a list of products."
                "\n3- Click on 'Total Price_List' button to see the Total price."
                "\n4- Select your products case_by_case from the table in which you want to 'Submit to Database'."
                "\n5- Enter Date of Submission for your future reference before clicking on 'Submit to Database'."
                "\n6- Click 'Submit to Database' button to make a list in Database."
                "\n7- 'Edit' option only works with product's id, which means if you want to change the id,"
                "\nyou have to 'Remove' previous unwanted Id at first,"
                "\nand then 'Add to List' new product with a new Id."
                "\nFinally, remember to 'Submit to Database' your new product.",
      background="yellow", fg="black").place(x=20, y=450 ,width=505, height=167)
#-----------------------------------------------------------------------------------------------------------------------------------
Label(win, text="Id\n>0" ,background="grey" , fg="white").place(x=20, y=20,width=70 ,height=29)
id = IntVar()
Entry(win, textvariable=id , width=22,background="grey" , fg="white").place(x=90, y=20)


Label(win, text="Name\n>3 char.",background="grey", fg="white").place(x=20, y=60,width=70 ,height=29)
name = StringVar()
ttk.Combobox(win, textvariable=name , values=("Laptop","TV","PlayStation","SmartPhone") ).place(x=90, y=60 ,width=135)


Label(win, text="Brand\n>3 char.",background="grey", fg="white").place(x=20, y=100,width=70 ,height=29)
brand = StringVar()
ttk.Combobox(win, textvariable=brand, values=("Sony","Lenovo","Samsung","Apple")).place(x=90, y=100,width=135)


Label(win, text="Quantity\nتعداد",background="grey", fg="white").place(x=20, y=140,width=70 ,height=30)
quantity = IntVar()
Entry(win, textvariable=quantity, width=22,background="grey" , fg="white").place(x=90, y=140)


Label(win, text="Price\nتومان",background="grey", fg="white").place(x=20, y=180,width=70 ,height=30)
price = DoubleVar()
Entry(win, textvariable=price, width=22,background="grey" , fg="white").place(x=90, y=180)


Label(win , text="Date\nyyyy-mm-dd",background="grey", fg="white").place(x=20, y=220 ,width=70 ,height=29)
date = StringVar()
Entry(win, textvariable=date , width=22,background="grey" , fg="white").place(x=90, y=220)

Button(win, text="Add to List", width=10, command=receive_product, background="grey").place(x=20, y=260)
Button(win, text="Total Price_List", width=17, command=total_price , background="grey").place(x=100, y=260)

Button(win, text="Edit Database", width=10, command=edit_click , background="lightblue").place(x=20, y=295)
Button(win, text="Remove from Database", width=17, command=remove_click , background="lightblue").place(x=100, y=295)
Button(win,text="Submit to Database", width=29, command=save_click, background="lightblue").place(x=20, y=325 ,width=209)

table = ttk.Treeview(win, height=12, columns=["Id", "Name", "Brand", "Quantity", "Price" , "Date"],
                     show="headings")

table.column("Id", width=60)
table.column("Name", width=100)
table.column("Brand", width=100)
table.column("Quantity", width=60)
table.column("Price" , width=60)
table.column("Date", width=100 )

table.heading("Id", text="Id" )
table.heading("Name", text="Name")
table.heading("Brand", text="Brand")
table.heading("Quantity", text="Quantity")
table.heading("Price", text="Price")
table.heading("Date", text="Date")

table.place(x=250, y=20 ,height=327)
table.bind("<<TreeviewSelect>>", select_product)


reset()
win.mainloop()
