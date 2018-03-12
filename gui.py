import Tkinter as tk   
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

# Other modules/functions
from mainpage import Mainpage
from homepage import Homepage
from userupcoming import UserResr
from userupcoming import UserPickup
from userupcoming import UserEvent
from pickupevent import Pickup
from pickupevent import Event
import login
import signup

# Main application container
class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.winfo_toplevel().title("Gourmet")

        # Container for frames
        self.geometry("800x500")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Define frames
        self.frames = {}
        self.frames["Mainpage"] = Mainpage(parent=container, controller=self)
        self.frames["Mainpage"].grid(row=0, column=0, sticky="nsew")
        self.frames["Homepage"] = Homepage(parent=container, controller=self)
        self.frames["Homepage"].grid(row=0, column=0, sticky="nsew")

        self.frames["UserResr"] = UserResr(parent=container, controller=self)
        self.frames["UserResr"].grid(row=0, column=0, sticky="nsew")
        self.frames["UserPickup"] = UserPickup(parent=container, controller=self)
        self.frames["UserPickup"].grid(row=0, column=0, sticky="nsew")
        self.frames["UserEvent"] = UserEvent(parent=container, controller=self)
        self.frames["UserEvent"].grid(row=0, column=0, sticky="nsew")

        #self.frames["Resr"] = Resr(parent=container, controller=self)
        #self.frames["Resr"].grid(row=0, column=0, sticky="nsew")
        self.frames["Pickup"] = Pickup(parent=container, controller=self)
        self.frames["Pickup"].grid(row=0, column=0, sticky="nsew")
        self.frames["Event"] = Event(parent=container, controller=self)
        self.frames["Event"].grid(row=0, column=0, sticky="nsew")

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