import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import setGlobal, getGlobal
import tkMessageBox

class Login(tk.Frame):

    def __init__(self, parent, controller):
        self.parent = parent
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
        self.hp_btn = tk.Button(self, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=0, column=0)

 

        self.email = tk.Label(self, text="email")
        self.email.grid(row=3, column=1)
        self.emailbox = tk.Entry(self, width=20)
        self.emailbox.grid(row=3, column=2)
        self.password = tk.Label(self, text="password")
        self.password.grid(row=4, column=1)
        self.passwordbox = tk.Entry(self, width=20)
        self.passwordbox.grid(row=4, column=2)


        self.submit = tk.Button(self, text="Submit", command = self.callback)
        self.submit.grid(row=5, column=1)
 
    def callback(self):
        self.givenemail = self.emailbox.get()
        self.givenpassword = self.passwordbox.get()

        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT COUNT(*) FROM users u WHERE u.useremail = \'{0}\' AND u.password = \'{1}\'; ".format(self.givenemail, self.givenpassword);
        result_set = conn.execute(query)

        count = []
        for r in result_set:
            count.append(r[0]);

        if int(count[0]) == 1: 
            setGlobal('useremail', self.givenemail)
            self.emailbox.delete(0, tk.END)
            self.passwordbox.delete(0, tk.END)
            self.controller.show_frame("Homepage")
            
        else:
            tkMessageBox.showerror("error","please recheck your password or email")

            

    def homepage(self, login):
        self.controller.show_frame("Homepage")
    def mainpage(self, login):
        self.controller.show_frame("Mainpage")


   



