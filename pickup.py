import Tkinter as tk
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import getGlobal, setGlobal
import tkMessageBox

# Frame for making pickups
class Pickup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

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
        setGlobal('lnb_pickup', arg)
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
        lnb_pickup = getGlobal('lnb_pickup')

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT foodname, foodprice FROM food_menu WHERE licensenb='{0}';".format(lnb_pickup)
        result_set = conn.execute(query)
        conn.close()

        food = []
        price = []
        quantities = []
        for r in result_set:
            food.append(r[0])
            price.append(r[1])

        # Print relevant info
        self.cart = tk.Button(self, text="Add to cart", )
        self.cart.bind('<Button-1>', lambda event, arg1=quantities, arg2=food, arg3=price:self.add2cart(event, arg1, arg2, arg3))
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
            quantities.append(self.quantity)
            i += 1
            irow += 1

    #arg1=quantities, arg2=food, arg3=price
    def add2cart(self, event, arg1, arg2, arg3):
        #If the cart is new and cartid is not yet set
        cartid_global = getGlobal('cartid')

        if cartid_global == 'None':

            #Connect to the db
            db = DBconnection.connecting()
            conn = db.connect()

            #create a new cart id
            query = "INSERT INTO cart VALUES (default);";
            conn.execute(query)
            query = "SELECT cartid FROM cart ORDER BY cartid DESC LIMIT 1;"
            cartid = conn.execute(query)
            for c in cartid:
                realid = c[0]
            conn.close()

        else:
            realid = cartid_global


        #insert new records into pickup_order
        i = 0
        invalid_count = 0
        pickup_price = float(getGlobal('pickup_price'))
        licensenb = getGlobal('lnb_pickup')
        #Connect to the db
        db = DBconnection.connecting()
        conn = db.connect()

        for entry in arg1:
            num = entry.get()
            if int(num) > 0:

                foodname = arg2[i]
                price = arg3[i]
                pickup_price += float(num) * price
                query = "INSERT INTO pickup_order VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\')".format(realid, licensenb, foodname, num);
                conn.execute(query)
                i += 1
            else:
                i += 1
                invalid_count += 1
                continue

        conn.close()

        #When all the quantities user entered are invalid
        if invalid_count == i:
            tkMessageBox.showerror("error","You did not select anything. Please check your selections again.")


        setGlobal('cartid', str(realid))
        setGlobal('pickup_price', str(pickup_price))

        #Show the cart window
        self.controller.show_frame("Cart")


    # Get global variable
    def getlnb(self):
        return getGlobal('lnb_pickup')

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")
