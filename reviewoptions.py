import Tkinter as tk
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import getGlobal, setGlobal
import tkMessageBox

inp = None

# Frame for displaying all reviews for a restaurant
class AllReviews(tk.Frame):

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
        self.desc = tk.Label(self, text="All reviews for this restaurant", wraplength=300)
        self.desc.grid(row=1, column=1)

        # Get restaurant license number from global variable
        licensenb = getGlobal('lnb_review')

        # Connect to DB and select user's points
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT reviewdate, rating, comment FROM review WHERE licensenb=\'{0}\';".format(licensenb)
        result_set = conn.execute(query)
        conn.close()

        #Putting all data from review table to arrays date, rating and comment
        date = []
        rating = []
        comment = []
        for r in result_set:
            date.append(r[0])
            rating.append(r[1])
            comment.append(r[2])

        #Print column names
        self.date = tk.Label(self, text="Date")
        self.date.grid(row=3, column=0)
        self.rating = tk.Label(self, text="Rating")
        self.rating.grid(row=3, column=1)
        self.comment = tk.Label(self, text="Comment")
        self.comment.grid(row=3, column=2)

        #Display data put in arrays date, rating and comment
        irow = 4
        i = 0
        for r in date:
            self.date.destroy()
            self.rating.destroy()
            self.comment.destroy()

            self.date = tk.Label(self, text=date[i])
            self.date.grid(row=irow, column=0)
            self.rating = tk.Label(self, text=rating[i])
            self.rating.grid(row=irow, column=1)
            self.comment = tk.Label(self, text=comment[i], wraplength = 300)
            self.comment.grid(row=irow, column=2)

            i += 1
            irow += 1

    #Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

# Frame for upcoming user reservations
class MakeReview(tk.Frame):

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

        self.rating = tk.Label(self, text="Please enter your rating here (from 1 to 5): ")
        self.rating.grid(row=1, column=0)

        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=1)

        self.intro = tk.Label(self, text="Plese write your comment here: ")
        self.intro.grid(row=2, column=0)

        self.text = tk.Text(self, borderwidth=3, width=50, height=20)
        self.text.grid(row=3, column=1)

        self.button = tk.Button(self, text="Submit comment", command=self.on_button)
        self.button.grid(row=3, column=2)


    def on_button(self):

        rating = int(self.entry.get())

        if (rating < 1) or (rating > 5):
            tkMessageBox.showerror("error","Please enter a valid rating.")

        lines = self.text.get("1.0", tk.END).splitlines()
        comment = ""
        for line in lines:
            comment += line
            comment += " "
        
        print isinstance(comment, basestring)
        # Get restaurant license number from global variable
        useremail = getGlobal('useremail')
        licensenb = getGlobal('lnb_review')
        date = getGlobal("date")


         # Connect to DB and select user's points
        db = DBconnection.connecting()
        conn = db.connect()

        query_select = "SELECT * FROM review WHERE useremail=\'{0}\' AND licensenb=\'{1}\';".format(useremail, licensenb)
        print "HERE"
        #row_count = conn.execute(query_select)
        print "HERE2"


        try:
            print "Did not find it"
            query = "INSERT INTO review VALUES (\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\');".format(useremail, licensenb, comment, rating, date)
            conn.execute(query)
            print "great"
        except (Exception):
            query = "UPDATE review SET comment = \'{0}\', rating = \'{1}\', reviewdate = \'{2}\' WHERE useremail = \'{3}\' AND licensenb = \'{4}\';".format(comment, rating, date, useremail, licensenb)
            conn.execute(query)
            print "noooo"
        finally:
            conn.close()




    #Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")
