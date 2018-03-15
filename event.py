import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
import globalvar

global lnb_event

# Frame for buying event tickets
class Event(tk.Frame):

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

        self.desc = tk.Label(self, text="Restaurants that are hosting events soon", wraplength=400)
        self.desc.grid(row=1, column=1)

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT DISTINCT licensenb, restaurantname, eventname, eventdate, eventprice FROM upcomingevents;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        event = []
        date = []
        price = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])
            event.append(r[2])
            date.append(r[3])
            price.append(r[4])

        # Print relevant info
        self.cart = tk.Button(self, text="Add to cart")
        self.cart.bind('<Button-1>', self.add2cart)
        self.cart.grid(row=3, column=0)
        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=1)
        self.event = tk.Label(self, text="Event")
        self.event.grid(row=3, column=2)
        self.date = tk.Label(self, text="Date")
        self.date.grid(row=3, column=3)
        self.price = tk.Label(self, text="Price (CAD)")
        self.price.grid(row=3, column=4)
        self.quantity = tk.Label(self, text="Quantity")
        self.quantity.grid(row=3, column=5)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=1)  
            self.event = tk.Label(self, text=event[i])
            self.event.grid(row=irow, column=2)
            self.date = tk.Label(self, text=date[i])
            self.date.grid(row=irow, column=3)
            self.price = tk.Label(self, text=price[i])
            self.price.grid(row=irow, column=4)
            self.quantity = tk.Entry(self, width=10)
            self.quantity.insert(0, "0")
            self.quantity.grid(row=irow, column=5)
            
            i += 1 
            irow += 1

    def add2cart(self, event):
        print "add to cart"

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")
