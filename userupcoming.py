import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import setGlobal, getGlobal

# Frame for upcoming user reservations
class UserResr(tk.Frame):

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
        self.desc = tk.Label(self, text="You have upcoming reservations from the following restaurants:", wraplength=300)
        self.desc.grid(row=1, column=1)

        #get the global variable from config.ini later
        useremail = getGlobal('useremail')

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT restaurantname, r.time FROM (SELECT * FROM user_books WHERE useremail = '{0}') as u JOIN (SELECT * FROM reservation WHERE time > now()) as r ON u.reservationid = r.reservationid JOIN (SELECT * FROM reservation_contains) as rc ON r.reservationid = rc.reservationid JOIN (SELECT licenseNB, restaurantname FROM restaurant) as res ON rc.licenseNB = res.licenseNB ORDER BY r.time;".format(useremail)
        result_set = conn.execute(query)  
        conn.close()

        restau = []
        time = []
        for r in result_set:
            restau.append(r[0])
            time.append(r[1])
        
        # Print relevant info
        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=1)
        self.time = tk.Label(self, text="Time (y-m-d h:s)")
        self.time.grid(row=3, column=2)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=1)  
            self.time = tk.Label(self, text=time[i])
            self.time.grid(row=irow, column=2)  
            i += 1 
            irow += 1

    def display(self, event):
        

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")


# Frame for upcoming user pickups
class UserPickup(tk.Frame):

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

        self.desc = tk.Label(self, text="You have upcoming food pickups from the following restaurants:", wraplength=300)
        self.desc.grid(row=1, column=1)

        #get the global variable from config.ini later
        useremail = getGlobal('useremail')

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT restaurantname FROM (SELECT * FROM transaction WHERE useremail = '{0}' AND transactiondate = current_date) as t JOIN (SELECT * FROM pickup_order) as p ON t.cartid = p.cartid JOIN  (SELECT licenseNB, restaurantname FROM restaurant) as res ON p.licenseNB = res.licenseNB;".format(useremail)
        result_set = conn.execute(query)  
        conn.close()

        restau = []
        for r in result_set:
            restau.append(r[0])
        
        # Print relevant info
        irow = 3
        i = 0
        for r in restau:
            self.resr = tk.Label(self, text=restau[i])
            self.resr.grid(row=irow, column=1)  
            i += 1 
            irow += 1

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

# Frame for upcoming user events
class UserEvent(tk.Frame):

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

        self.desc = tk.Label(self, text="You have upcoming events from the following restaurants", wraplength=300)
        self.desc.grid(row=1, column=1)

        #get the global variable from config.ini later
        useremail = getGlobal('useremail')

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT restaurantname, eventname, eventdate FROM (SELECT * FROM transaction WHERE useremail = '{0}') as t JOIN (SELECT * FROM event_order WHERE eventdate > now()) as e ON t.cartid = e.cartid JOIN (SELECT licenseNB, restaurantname FROM restaurant) as res ON e.licenseNB = res.licenseNB ORDER BY eventdate;".format(useremail)
        result_set = conn.execute(query)  
        conn.close()

        restau = []
        event = []
        date = []
        for r in result_set:
            restau.append(r[0])
            event.append(r[1])
            date.append(r[2])
        
        # Print relevant info
        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=0)
        self.event = tk.Label(self, text="Event")
        self.event.grid(row=3, column=1)
        self.time = tk.Label(self, text="Date (y-m-d)")
        self.time.grid(row=3, column=2)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=0) 
            self.event = tk.Label(self, text=event[i])
            self.event.grid(row=irow, column=1)
            self.time = tk.Label(self, text=date[i])
            self.time.grid(row=irow, column=2)   
            i += 1 
            irow += 1

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")


