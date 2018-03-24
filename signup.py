import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import setGlobal, getGlobal
import tkMessageBox
import datetime


class Signup(tk.Frame):

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
        self.birthday = tk.Label(self, text="birthday")
        self.birthday.grid(row=5, column=1)
        self.birthdaybox = tk.Entry(self, width=20)
        self.birthdaybox.grid(row=5, column=2)


        self.create = tk.Button(self, text="Create", command = self.callback)
        self.create.grid(row=6, column=1)
 
    def callback(self):
        self.givenemail = self.emailbox.get()
        self.givenpassword = self.passwordbox.get()
        self.givenbirthday = self.birthdaybox.get()
        print self.givenbirthday
        if(validate_date(self.givenbirthday)==False):
            tkMessageBox.showerror("error","Invalid birthday format. Expected format is YYYY-MM-DD")
        else:
            db = DBconnection.connecting()
            conn = db.connect()
            query = "INSERT INTO users VALUES (\'{0}\', \'{1}\', default, \'{2}\');".format(self.givenemail, self.givenpassword, self.givenbirthday);

            
            try:
                result_set = conn.execute(query)
                conn.close()
            except psycopg2.Error as e:
                tkMessageBox.showerror("error","the account is already existed")
                conn.close()
            else:
                tkMessageBox.showinfo("account created", "your account is successfully created")
                conn.close()

    

    def homepage(self, login):
        self.controller.show_frame("Homepage")
    def mainpage(self, login):
        self.controller.show_frame("Mainpage")

def validate_date(d):
    try:
        datetime.datetime.strptime(d, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    



