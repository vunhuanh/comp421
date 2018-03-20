import Tkinter as tk
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import getGlobal, setGlobal

# Frame for upcoming user cart
class Cart(tk.Frame):

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

        # Display
        self.display_btn = tk.Button(self, text="Display")
        self.display_btn.bind('<Button-1>', self.display)
        self.display_btn.grid(row=1, column=0)

    # Display page contents
    def display(self, event):

        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)
        self.desc = tk.Label(self, text="Current items in your cart")
        self.desc.grid(row=1, column=1)

        cartid_global = getGlobal('cartid')
        #When the user hasn't put anything in the cart
        if cartid_global == 'None':
            print "Is None"
            self.controller.show_frame("Empty_Cart")

        else:
            print "Not None"
            self.type = tk.Label(self, text="Order type")
            self.type.grid(row=3, column=0)
            self.res = tk.Label(self, text="Restaurant")
            self.res.grid(row=3, column=1)
            self.name = tk.Label(self, text="Name")
            self.name.grid(row=3, column=2)
            self.date = tk.Label(self, text="Date")
            self.date.grid(row=3, column=3)
            self.qty = tk.Label(self, text="Quantity")
            self.qty.grid(row=3, column=4)
            self.price = tk.Label(self, text="Price")
            self.price.grid(row=3, column=5)

            ordertype = []
            licensenb = []
            restau = []
            foodname = []
            date = []
            quantity = []
            price = []

            # Connect to DB and get all pickup_order records
            db = DBconnection.connecting()
            conn = db.connect()
            query = "SELECT licensenb, foodname, quantity FROM pickup_order WHERE cartid = \'{0}\'".format(cartid_global);
            result_set = conn.execute(query)
            conn.close()

            current_date = getGlobal('date')
            for r in result_set:
                ordertype.append('Pickup')
                licensenb.append(r[0])
                foodname.append(r[1])
                date.append(current_date)
                quantity.append(r[2])

            #Get the restaurant names and price for each pickup record
            i = 0
            db = DBconnection.connecting()
            conn = db.connect()
            for r in licensenb
                this_licensenb = licensenb[i]
                this_food = foodname[i]
                #Get restaurant name
                query_restau = "SELECT restaurantname FROM restaurant WHERE licensenb = \'{0}\'".format(this_licensenb);
                result_set_restau = conn.execute(query_restau)
                for r in result_set_restau
                    restau.append(0)
                #Get price for each pickup record
                query_price = "SELECT foodprice FROM food_menu WHERE licensenb = \'{0}\' AND foodname = \'{1}\'".format(this_licensenb, this_food);
                result_set_price = conn.execute(query_price)
                for r in result_set_price
                    restau.append(0)
                i += 1
            conn.close()

            # Connect to DB and get all event_order records
            db = DBconnection.connecting()
            conn = db.connect()
            query = "SELECT licensenb, eventname, eventdate, eventattendees FROM event_order WHERE cartid = \'{0}\'".format(cartid_global);
            result_set = conn.execute(query)
            conn.close()

            for r in result_set:
                ordertype.append('Event')
                licensenb.append(r[0])
                foodname.append(r[1])
                date.append(r[2])
                quantity.append(r[3])

            #Get the restaurant names and price for each pickup record
            i = 0
            db = DBconnection.connecting()
            conn = db.connect()
            for r in licensenb
                this_licensenb = licensenb[i]
                this_food = foodname[i]
                #Get restaurant name
                query_restau = "SELECT restaurantname FROM restaurant WHERE licensenb = \'{0}\'".format(this_licensenb);
                result_set_restau = conn.execute(query_restau)
                for r in result_set_restau
                    restau.append(0)
                #Get price for each pickup record
                query_price = "SELECT foodprice FROM food_menu WHERE licensenb = \'{0}\' AND foodname = \'{1}\'".format(this_licensenb, this_food);
                result_set_price = conn.execute(query_price)
                for r in result_set_price
                    restau.append(0)
                i += 1
            conn.close()

            irow = 4
            i = 0
            for r in food:
                self.ordertype = tk.Label(self, text=ordertype[i])
                self.ordertype.grid(row=irow, column=1)
                self.restau = tk.Label(self, text=restau[i])
                self.restau.grid(row=irow, column=2)
                self.foodname = tk.Label(self, text=foodname[i])
                self.foodname.grid(row=irow, column=3)
                self.date = tk.Label(self, text=current_date)
                self.restau.grid(row=irow, column=2)
                self.quantity = tk.Label(self, text=quantity[i])
                self.quantity.grid(row=irow, column=5)
                quantities.append(self.quantity)
                i += 1
                irow += 1


        # Display cart contents

        # Checkout
        self.hp_btn = tk.Button(self, text="Checkout")
        self.hp_btn.bind('<Button-1>', self.checkout)
        self.hp_btn.grid(row=4, column=0)

    # Checkout and make transaction
    def checkout(self, event):
        print "checkout"

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

class Empty_Cart(tk.Frame):

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

        # Display
        self.display_btn = tk.Button(self, text="Display")
        self.display_btn.bind('<Button-1>', self.display)
        self.display_btn.grid(row=1, column=0)

    # Display page contents
    def display(self, event):
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)
        self.desc = tk.Label(self, text="Your cart is empty.")
        self.desc.grid(row=1, column=1)

    def homepage(self, event):
        self.controller.show_frame("Homepage")
