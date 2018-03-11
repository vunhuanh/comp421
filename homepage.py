import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

# Frame for home page
class Homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # Show a frame for the given page name
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # Create widgets inside homepage
    def create_widgets(self):
        # Set width to column 0
        self.grid_columnconfigure(0, minsize=100)
        
        # Header
        self.title = tk.Label(self, text="GOURMET")
        self.title.grid(row=0, column=1)
        self.desc = tk.Label(self, text="Welcome, <user>.\n\n", wraplength=500)
        self.desc.grid(row=1, column=1)

        # Buttons
        self.points_btn = tk.Button(self, text="View my points")
        self.points_btn.bind('<Button-1>', self.points)
        self.points_btn.grid(row=2, column=1, sticky=tk.W)

        self.u_resr_btn = tk.Button(self, text="View my upcoming reservations")
        self.u_resr_btn.bind('<Button-1>', self.u_resr)
        self.u_resr_btn.grid(row=3, column=1, sticky=tk.W)

        self.u_pickup_btn = tk.Button(self, text="View my upcoming pickup orders")
        self.u_pickup_btn.bind('<Button-1>', self.u_pickup)
        self.u_pickup_btn.grid(row=4, column=1, sticky=tk.W)

        self.u_event_btn = tk.Button(self, text="View my upcoming events")
        self.u_event_btn.bind('<Button-1>', self.u_event)
        self.u_event_btn.grid(row=5, column=1, sticky=tk.W)

    # View points
    def points(self, event):
        db = DBconnection.connecting()
        conn = db.connect()
        table = "users"
        useremail = "nhu.vu@mail.mcgill.ca"
        query = "SELECT points FROM {0} WHERE username = {1}".format(table, useremail)
        result_set = conn.execute(query)  
        for r in result_set:  
            #get the first column
            print(r[0])
            #get the second column

    # View upcoming reservations
    def u_resr(self, event):
        print "a"

    # View upcoming pickup orders
    def u_pickup(self, event):
        print ""

    # View upcoming events
    def u_event(self, event):
        print ""


