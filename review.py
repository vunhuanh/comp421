import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

# Frame for buying event tickets
class Review(tk.Frame):

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

        self.desc = tk.Label(self, text="Restaurant reviews", wraplength=400)
        self.desc.grid(row=1, column=1)

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT licensenb, restaurantname FROM restaurant ORDER BY restaurantname;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])

        # Print relevant info
        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=0)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=0)  
            self.allrev = tk.Button(self, text="See other users' reviews")
            self.allrev.bind('<Button-1>', self.allreview)
            self.allrev.grid(row=irow, column=1)
            self.urev = tk.Button(self, text="Make a review")
            self.urev.bind('<Button-1>', self.userreview)
            self.urev.grid(row=irow, column=2)
            
            i += 1 
            irow += 1

    #See all reviews of other users
    def allreview(self, event):
        self.controller.show_frame("AllReviews")
         
    #Make a new review for this restaurant
    def userreview(self, event):
        self.controller.show_frame("MakeReview")

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")
        

