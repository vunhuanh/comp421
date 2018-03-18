import Tkinter as tk
from Tkinter import *
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

# Other modules/functions
import globalvar #file containing global variables - not sure if we should keep
    #either keep these as functions and just have textboxes right on the mainpage
    #or have separate signup/login pages
import login
import signup 
from mainpage import Mainpage
from homepage import Homepage
from cart import Cart
from userupcoming import UserResr
from userupcoming import UserPickup
from userupcoming import UserEvent
from reserve import Reserve
from pickup import Pickup
from pickup import R_menu
from event import Event
from review import Review


# Main application container
class Application(tk.Tk):
    '''# Global variables idk why it doesn't work HELP
    global useremail
    global lnb_reserve
    global lnb_pickup
    global lnb_event'''

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("Gourmet")

        # Container for frames
        self.geometry("800x500")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Define frames
        self.frames = {}
        for F in (Mainpage, Homepage, UserResr, UserPickup, UserEvent, Reserve, Pickup, R_menu, Event, Cart, Review):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Go to mainpage (before login)
        self.show_frame("Mainpage")

    # Show a frame for the given page name
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# Start application
if __name__ == "__main__":
    app = Application()
    app.mainloop()