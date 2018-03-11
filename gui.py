import Tkinter as tk   
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData

# Other modules/functions
from mainpage import Mainpage
from homepage import Homepage
import login
import signup

# Main application container
class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Container for frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.geometry("800x500")
        self.grid()

        # Define frames
        self.frames = {}
        self.frames["mainpage"] = Mainpage(parent=container, controller=self)
        self.frames["mainpage"].grid(row=0, column=0, sticky="nsew")

        self.frames["homepage"] = Homepage(parent=container, controller=self)
        self.frames["homepage"].grid(row=0, column=0, sticky="nsew")

        # Go to mainpage (before login)
        self.show_frame("mainpage")

    # Show a frame for the given page name
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# Start application
if __name__ == "__main__":
    app = Application()
    app.mainloop()