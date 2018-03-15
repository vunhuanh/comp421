import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
import globalvar

# Frame for making pickups
class Pickup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # Create widgets inside homepage
    def create_widgets(self):
        # Set min width to columns
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)
        self.grid_rowconfigure(2, minsize=10)
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.desc = tk.Label(self, text="Restaurants available for food pickup", wraplength=400)
        self.desc.grid(row=1, column=1)

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT DISTINCT r.licensenb, r.restaurantname FROM food_menu f, restaurant r WHERE f.licensenb = r.licensenb;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])
        
        irow = 3
        i = 0
        for r in restau:
            self.vmenu = tk.Button(self, text="View menu")
            self.vmenu.bind('<Button-1>', lambda event, arg=licensenb[i]: self.menu(event, arg))
            self.vmenu.grid(row=irow, column=0)

            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=1)  

            i += 1 
            irow += 1

    # Go to menu page
    def menu(self, event, arg):
        globalvar.lnb_pickup = arg
        self.controller.show_frame("R_menu")

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

# Frame for viewing restaurant menu
class R_menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # Create widgets inside homepage
    def create_widgets(self):
        # Set min width to columns
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)
        self.grid_rowconfigure(2, minsize=10)
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.desc = tk.Label(self, text="Menu")
        self.desc.grid(row=1, column=1)
        
        # Get queried restaurant licensenb
        lnb_pickup = 'shaw7223'

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT foodname, foodprice FROM food_menu WHERE licensenb='{0}';".format(lnb_pickup)
        result_set = conn.execute(query)  
        conn.close()

        food = []
        price = []
        for r in result_set:
            food.append(r[0])
            price.append(r[1])
        
        # Print relevant info
        self.cart = tk.Button(self, text="Add to cart")
        self.cart.bind('<Button-1>', self.add2cart)
        self.cart.grid(row=3, column=0)
        self.fd = tk.Label(self, text="Food")
        self.fd.grid(row=3, column=1)
        self.pc = tk.Label(self, text="Price")
        self.pc.grid(row=3, column=2)
        self.qty = tk.Label(self, text="Quantity")
        self.qty.grid(row=3, column=3) 

        irow = 4
        i = 0
        for r in food:
            self.food = tk.Label(self, text=food[i])
            self.food.grid(row=irow, column=1)  
            self.price = tk.Label(self, text=price[i])
            self.price.grid(row=irow, column=2)
            self.quantity = tk.Entry(self, width=10)
            self.quantity.insert(0, "0")
            self.quantity.grid(row=irow, column=3)

            i += 1 
            irow += 1

    def add2cart(self, event):
        print "add to cart"

    # Get global variable
    def getlnb(self):
        return globalvar.lnb_pickup

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

