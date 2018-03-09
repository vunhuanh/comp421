#!/usr/bin/python
import Tkinter

from Tkinter import *

parentw = Tkinter.Tk()
# Code to add widgets will go here...


text = Text(parentw)
text.insert(INSERT, "hello world")
text.pack()

parentw.mainloop()