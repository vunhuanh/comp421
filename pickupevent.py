import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData


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
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=3)

        self.desc = tk.Label(self, text="Here are all restaurants available for food pickup")
        self.desc.grid(row=1, column=1)

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
        
        irow = 2
        i = 0
        for r in restau:
            self.resr = tk.Label(self, text=restau[i])
            self.resr.grid(row=irow, column=1)  
            i += 1 
            irow += 1


    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

# Frame for buying event tickets
class Event(tk.Frame):

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
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=3)

        self.desc = tk.Label(self, text="Search for restaurants that are hosting events soon")
        self.desc.grid(row=1, column=1)

        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT DISTINCT licensenb, restaurantname, eventname, eventdate, eventprice FROM upcomingevents;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])
        
        irow = 2
        i = 0
        for r in restau:
            self.resr = tk.Label(self, text=restau[i])
            self.resr.grid(row=irow, column=1)  
            i += 1 
            irow += 1

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")


