import Tkinter
from Tkinter import *
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData


class Application(Frame):

    #Customize the master window
    def __init__(self):
        self.master = Tk()
        self.master.geometry("800x500")

        Frame.__init__(self, self.master)
        self.grid()
        self.create_widgets()

    #Create widgets inside of the master window
    def create_widgets(self):
        #Config
        self.grid_columnconfigure(0, minsize=100)
        w1 = Text(self, undo=True, height=1, width=26,wrap=NONE)
        w1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        #Header
        self.title = Label(self, text="GOURMET")
        self.title.grid(row=0, column=1)
        self.desc = Label(self, text="Welcome, <user>.\n\n", wraplength=500)
        self.desc.grid(row=1, column=1)

        #Buttons
        self.points_btn = Button(self, text="View my points")
        self.points_btn.bind('<Button-1>', self.points)
        self.points_btn.grid(row=2, column=1, sticky=W)

        self.u_resr_btn = Button(self, text="View my upcoming reservations")
        self.u_resr_btn.bind('<Button-1>', self.u_resr)
        self.u_resr_btn.grid(row=3, column=1, sticky=W)

        self.u_pickup_btn = Button(self, text="View my upcoming pickup orders")
        self.u_pickup_btn.bind('<Button-1>', self.u_pickup)
        self.u_pickup_btn.grid(row=4, column=1, sticky=W)

        self.u_event_btn = Button(self, text="View my upcoming events")
        self.u_event_btn.bind('<Button-1>', self.u_event)
        self.u_event_btn.grid(row=5, column=1, sticky=W)

    #View points
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

    #View upcoming reservations
    def u_resr(self, event):
        print ""

    #View upcoming pickup orders
    def u_pickup(self, event):
        print ""

    #View upcoming events
    def u_event(self, event):
        print ""


    #Start the main loop
    def start(self):
        self.master.mainloop()
        
if __name__=='__main__': 
    Application().start()
