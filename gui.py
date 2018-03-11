import Tkinter
from Tkinter import *

#Other pages/functions
import homepage
import login
import signup


# Code to add widgets will go here...
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
        self.grid_columnconfigure(0, minsize=100)
        w1 = Text(self, undo=True, height=1, width=26,wrap=NONE)
        w1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.title = Label(self, text="GOURMET")
        self.title.grid(row=0, column=1)

        self.desc = Label(self, text="Gourmet is an application which lets you reserve tables in our partnered restaurants, as well as buy event tickets and food.\n\n", wraplength=500)
        self.desc.grid(row=1, column=1, sticky=E)

        self.signup_btn = Button(self, text="Sign up")
        self.signup_btn.bind('<Button-1>', self.signup)
        self.signup_btn.grid(row=2, column=1, sticky=W)

        self.login_btn = Button(self, text="Log in")
        self.login_btn.bind('<Button-1>', self.login)
        self.login_btn.grid(row=2, column=1, sticky=E)

    #Signup
    def signup(self, event):
        hp = signup.display(self)

    #Login
    def login(self, event):
        hp = login.display(self)
        ### once logged in, display the homepage.py frame




    #Start the main loop
    def start(self):
        self.master.mainloop()
        


Application().start()
