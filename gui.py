#!/usr/bin/python
import Tkinter

from Tkinter import *

parentw = Tkinter.Tk()
# Code to add widgets will go here...

#General intro text
title = Label(parentw, text="GOURMET\n\n", anchor=CENTER)
title.pack()
desc = Label(parentw, text="Gourmet is an application which lets you reserve tables in our partnered restaurants, as well as buy event tickets and food.\n\n", anchor=CENTER)
desc.pack()

#Login, signup
L1 = Label(parentw, text="Username")
L1.pack(side = LEFT)
E1 = Entry(parentw)
E1.pack(side = RIGHT)

L2 = Label(parentw, text="Password")
L2.pack(side = LEFT)
E2 = Entry(parentw)
E2.pack(side = RIGHT)



mainloop()