#!/usr/bin/python
import Tkinter

from Tkinter import *

# Code to add widgets will go here...
class Application(Frame):

    #Customize the master window
    def __init__(self):
        self.master = Tk()
        self.master.geometry("1000x500")

        Frame.__init__(self, self.master)
        self.create_widgets()

    #Create widgets inside of the master window
    def create_widgets(self):
        self.master.bind('<Return>', self.parse)
        self.grid()

        w1 = Text(self, undo=True, height=1, width=26,wrap=NONE)
        w1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.title = Label(self, text="GOURMET")
        self.title.grid(row=0, column=1, sticky=E)

        self.desc = Label(self, text="Gourmet is an application which lets you reserve tables in our partnered restaurants, as well as buy event tickets and food.\n\n", wraplength=500)
        self.desc.grid(row=1, column=1, sticky=E)

        self.submit = Button(self, text="Submit")
        self.submit.bind('<Button-1>', self.parse)
        self.submit.grid(row=2, column=2, sticky=E)


    #Actions performed after click the button
    def parse(self, event):
        print("You clicked?")


    #Start the main loop
    def start(self):
        self.master.mainloop()


Application().start()
