import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import setGlobal, getGlobal

# Frame for home page
class Homepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    # Create widgets inside homepage
    def create_widgets(self):
        # Set min width to columns

        self.grid_rowconfigure(0, minsize=10)
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)
        
        # Header
            # Get user email from session variable

        #get the global variable from config.ini laterrr
        useremail = getGlobal('useremail')

        
        self.title = tk.Label(self, text="GOURMET")
        self.title.grid(row=1, column=1)
        msg = "Welcome, "
        msg += useremail
        self.desc = tk.Label(self, text=msg)
        self.desc.grid(row=2, column=1)

        # Logout
        self.logout_btn = tk.Button(self, text="Logout")
        self.logout_btn.bind('<Button-1>', self.logout)
        self.logout_btn.grid(row=0, column=0)

        # Cart
        self.cart_btn = tk.Button(self, text="My cart")
        self.cart_btn.bind('<Button-1>', self.cart)
        self.cart_btn.grid(row=2, column=0)

        # Buttons for all actions user can take
        self.points_btn = tk.Button(self, text="View my points")
        self.points_btn.bind('<Button-1>', self.points)
        self.points_btn.grid(row=3, column=1, sticky=tk.W)

        self.u_resr_btn = tk.Button(self, text="View my upcoming reservations")
        self.u_resr_btn.bind('<Button-1>', self.u_resr)
        self.u_resr_btn.grid(row=4, column=1, sticky=tk.W)

        self.u_pickup_btn = tk.Button(self, text="View my upcoming pickup orders")
        self.u_pickup_btn.bind('<Button-1>', self.u_pickup)
        self.u_pickup_btn.grid(row=5, column=1, sticky=tk.W)

        self.u_event_btn = tk.Button(self, text="View my upcoming events")
        self.u_event_btn.bind('<Button-1>', self.u_event)
        self.u_event_btn.grid(row=6, column=1, sticky=tk.W)

        self.resr_btn = tk.Button(self, text="Make a reservation")
        self.resr_btn.bind('<Button-1>', self.resr)
        self.resr_btn.grid(row=7, column=1, sticky=tk.W)

        self.pickup_btn = tk.Button(self, text="Make a food pickup order")
        self.pickup_btn.bind('<Button-1>', self.pickup)
        self.pickup_btn.grid(row=8, column=1, sticky=tk.W)

        self.event_btn = tk.Button(self, text="Purchase tickets for an event")
        self.event_btn.bind('<Button-1>', self.event)
        self.event_btn.grid(row=9, column=1, sticky=tk.W)

        self.review_btn = tk.Button(self, text="Review a restaurant")
        self.review_btn.bind('<Button-1>', self.review)
        self.review_btn.grid(row=10, column=1, sticky=tk.W)

    # Logout
    def logout(self, event):
        setGlobal('useremail', 'None')
        self.controller.show_frame("Mainpage")

    def cart(self, event):
        self.controller.show_frame("Cart")

    # View points
    def points(self, event):
        # Get user email from session variable
        useremail = getGlobal('useremail')


        # Connect to DB and select user's points
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT points FROM users WHERE useremail='{0}';".format(useremail)
        result_set = conn.execute(query)  
        conn.close()
        for r in result_set:  
            nbpoints = r[0]
        
        strpoints = "You have "
        strpoints += str(nbpoints)
        strpoints += " points"
        self.point = tk.Label(self, text=strpoints)
        self.point.grid(row=3, column=2)

    # View upcoming reservations
    def u_resr(self, event):
        self.controller.show_frame("UserResr")

    # View upcoming pickup orders
    def u_pickup(self, event):
        self.controller.show_frame("UserPickup")

    # View upcoming events
    def u_event(self, event):
        self.controller.show_frame("UserEvent")

    # View upcoming reservations
    def resr(self, event):
        self.controller.show_frame("Reserve")

    # View upcoming pickup orders
    def pickup(self, event):
        self.controller.show_frame("Pickup")

    # View upcoming events
    def event(self, event):
        self.controller.show_frame("Event")

    # Review restaurant
    def review(self, event):
        print "review"
        self.controller.show_frame("Review")



