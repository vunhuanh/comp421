#!/usr/bin/python
import Tkinter

from Tkinter import *

parentw = Tkinter.Tk()
# Code to add widgets will go here...


title = Text(parentw)
title.insert(INSERT, "GOURMET\n")
title.pack()
desc = Text(parentw)
desc.insert(END, "Gourmet is an application which lets you reserve tables in our partnered restaurants, as well as buy event tickets and food.")
desc.pack()

L1 = Label(parentw, text="Username")
L1.pack(side = LEFT)
E1 = Entry(parentw, bd = 5)
E1.pack(side = RIGHT)



parentw.mainloop()