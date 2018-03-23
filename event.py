import Tkinter as tk
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import getGlobal, setGlobal
import tkMessageBox

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

        self.desc = tk.Label(self, text="Restaurants hosting events soon", wraplength=300)
        self.desc.grid(row=1, column=1)

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT DISTINCT licensenb, restaurantname, eventname, eventdate, eventprice FROM upcomingevents ORDER BY eventdate;"
        result_set = conn.execute(query)
        conn.close()

        licensenb = []
        restau = []
        event = []
        date = []
        price = []
        attendees = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])
            event.append(r[2])
            date.append(r[3])
            price.append(r[4])

        # Print relevant info
        self.cart = tk.Button(self, text="Add to cart")
        self.cart.bind('<Button-1>', lambda event, arg1=attendees, arg2=licensenb, arg3=event, arg4=date, arg5=price:self.add2cart(event, arg1, arg2, arg3, arg4, arg5))
        self.cart.grid(row=3, column=0)
        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=1)
        self.event = tk.Label(self, text="Event")
        self.event.grid(row=3, column=2)
        self.date = tk.Label(self, text="Date (y-m-d)")
        self.date.grid(row=3, column=3)
        self.price = tk.Label(self, text="Price")
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
            attendees.append(self.quantity)

            i += 1
            irow += 1

    def add2cart(self, event, arg1, arg2, arg3, arg4, arg5):
        #arg1=attendees, arg2=licensenb, arg3=event, arg4=date, arg5=price
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
        event_price = float(getGlobal('event_price'))

        #Connect to the db
        db = DBconnection.connecting()
        conn = db.connect()

        for entry in arg1:
            num = entry.get()
            if int(num) > 0:

                licensenb = arg2[i]
                event = arg3[i]
                date = arg4[i]
                price = arg5[i]
                event_price += float(num) * price
                query = "INSERT INTO event_order VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')".format(realid, licensenb, event, date, num);
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
        setGlobal('event_price', str(event_price))

        #Show the cart window
        self.controller.show_frame("Cart")

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")
