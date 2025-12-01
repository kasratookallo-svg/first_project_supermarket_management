from supermarket_controller import *
from supermarket_model import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

product_list = []

def reset():
    id.set(0)
    name.set("")
    brand.set("")
    quantity.set(0)
    price.set(0)

    status, product_list = ProductController.find_all()

    #for item in table.get_children():
     #   table.delete(item)

    for product in product_list:
        table.insert("", END, values=tuple(product))
#-----------------------------------------------------------------------------------------------
# Table_Database function
def select_product(event):
    product = table.item(table.focus())["values"]
    id.set(product[0])
    name.set(product[1])
    brand.set(product[2])
    quantity.set(product[3])
    price.set(product[4])
#-----------------------------------------------------------------------------------------------
# Entry based on second approach (Function_handling)
def receive_product():
    try:
        product = creat_products_and_validate(id.get(),
                                              name.get(),
                                              brand.get(),
                                              quantity.get(),
                                              price.get()
                                              )
        product_list.append(product)
        print(product, "Product saved successfully.")
    #---------------------------------------------------------------
        # If you use Pickle
        # save_to_file(product_list)
    #----------------------------------------------------------------
        print("-" * 150)
        #To insert Data into the table
        table.insert("" , END, values=tuple(product.values()))
        messagebox.showinfo("Information Saved", "Product saved successfully.")
        print("Your Market includes : ", product_list)
        print("-" * 150)
        reset()
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong : {e}")
#-----------------------------------------------------------------------------------------------
# Database functions
def save_click():
    status, message = ProductController.save(
        id.get(),
        name.get(),
        brand.get(),
        quantity.get(),
        price.get()
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
        price.get()
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
        messagebox.showinfo("Total Price", f"Total : {calculate_total(product_list)}")
    except Exception as e:
        messagebox.showerror("Error", f"Error!!! : {e}")


win = Tk()
win.geometry("650x350")
win.title("Super Market _ List of Products")
win.configure(bg="green")


Label(win, text="Id" ,background="grey" , fg="white").place(x=20, y=20)
Label(win, text="Name",background="grey", fg="white").place(x=20, y=60)
Label(win, text="brand",background="grey", fg="white").place(x=20, y=100)
Label(win, text="quantity",background="grey", fg="white").place(x=20, y=140)
Label(win, text="price",background="grey", fg="white").place(x=20, y=180)

id = IntVar()
name = StringVar()
brand = StringVar()
quantity = IntVar()
price = DoubleVar()

Entry(win, textvariable=id , width=22,background="grey" , fg="white").place(x=90, y=20)
Entry(win, textvariable=name, width=22,background="grey" , fg="white").place(x=90, y=60)
Entry(win, textvariable=brand, width=22,background="grey" , fg="white").place(x=90, y=100)
Entry(win, textvariable=quantity, width=22,background="grey" , fg="white").place(x=90, y=140)
Entry(win, textvariable=price, width=22,background="grey" , fg="white").place(x=90, y=180)

Button(win, text="Save", width=10, command=receive_product, background="blue").place(x=20, y=230)
Button(win, text="Edit", width=10, command=edit_click , background="yellow").place(x=150, y=230)
Button(win, text="Remove", width=10, command=remove_click , background="red").place(x=20, y=280)
Button(win, text="Total Price", width=10, command=total_price , background="grey").place(x=150, y=280)

table = ttk.Treeview(win, height=12, columns=["Id", "Name", "Brand", "Quantity", "Price"],
                     show="headings")

table.column("Id", width=60)
table.column("Name", width=100)
table.column("Brand", width=100)
table.column("Quantity", width=60)
table.column("Price", width=60)

table.heading("Id", text="Id" )
table.heading("Name", text="Name")
table.heading("Brand", text="Brand")
table.heading("Quantity", text="Quantity")
table.heading("Price", text="Price")

table.place(x=250, y=20 ,height=290)
table.bind("<<TreeviewSelect>>", select_product)


reset()
win.mainloop()
