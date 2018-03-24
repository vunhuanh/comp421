import Tkinter as tk
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

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