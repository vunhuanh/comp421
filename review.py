import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import getGlobal, setGlobal  

# Frame for buying event tickets
class Review(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)

        self.display_btn = tk.Button(self, text="Display")
        self.display_btn.bind('<Button-1>', self.display)
        self.display_btn.grid(row=0, column=4)

        #create_widgets(self.interior)

    # def create_widgets(self):
    #     Set min width to columns
    #     self.grid_columnconfigure(0, minsize=150)
    #     self.grid_columnconfigure(1, minsize=150)
    #     self.grid_columnconfigure(2, minsize=150)
    #     self.grid_rowconfigure(2, minsize=10)

    #     # Display
    #     self.display_btn = tk.Button(self, text="Display")
    #     self.display_btn.bind('<Button-1>', display(self.interior))
    #     self.display_btn.grid(row=0, column=4)

    def resize(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=785, height=500)
        
    # Display page contents
    def display(self, event):

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0)

        self.vsbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vsbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsbar.set)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.interior, anchor='nw')

        self.interior.bind("<Configure>", self.resize)
        self.interior.grid_columnconfigure(0, minsize=150)
        self.interior.grid_columnconfigure(1, minsize=150)
        self.interior.grid_columnconfigure(2, minsize=150)

        # self.display_btn = tk.Button(self.interior, text="Display")
        # self.display_btn.bind('<Button-1>', self.display)
        # self.display_btn.grid(row=0, column=4)

        rows = 100
        for i in range(1,rows):
            self.interior.grid_rowconfigure(i, minsize=10)

        # Header
        self.hp_btn = tk.Button(self.interior, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

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
        self.name = tk.Label(self.interior, text="Restaurant")
        self.name.grid(row=3, column=0)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self.interior, text=restau[i])
            self.res.grid(row=irow, column=0)

            self.allrev = tk.Button(self.interior, text="See other users' reviews")
            self.allrev.bind('<Button-1>', lambda event, arg=licensenb[i]:self.allreview(event, arg))
            self.allrev.grid(row=irow, column=1)
            self.urev = tk.Button(self.interior, text="Make a review")
            self.urev.bind('<Button-1>', lambda event, arg=licensenb[i]:self.userreview(event, arg))
            self.urev.grid(row=irow, column=2)
            
            i += 1 
            irow += 1


    #See all reviews of other users
    def allreview(self, event, arg):
        setGlobal('lnb_review', arg)
        self.controller.show_frame("AllReviews")
        
         
    #Make a new review for this restaurant
    def userreview(self, event, arg):
        setGlobal('lnb_review', arg)
        self.controller.show_frame("MakeReview")

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

    
    

