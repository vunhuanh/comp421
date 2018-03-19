import Tkinter as tk

class Scroll(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame
    * Construct and pack/place/grid normally
    * This frame only allows vertical scrolling

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)            

        # create a canvas object and a vertical scrollbar for scrolling it
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0)

        self.vsbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vsbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsbar.set)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.interior, anchor='nw')

        self.interior.bind("<Configure>", self.resize)

        self.interior.grid_rowconfigure(0, minsize=100)
        self.interior.grid_rowconfigure(1, minsize=100)
        self.interior.grid_rowconfigure(2, minsize=100)
        self.interior.grid_rowconfigure(3, minsize=100)
        self.interior.grid_rowconfigure(4, minsize=100)
        self.interior.grid_rowconfigure(5, minsize=100)

        self.hp_btn = tk.Button(self.interior, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=0, column=0)

        # rows = 50
        # for i in range(1,rows):
        self.hp_btn = tk.Button(self.interior, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=2, column=0)


        

    def mainpage(self, login):
        self.controller.show_frame("Mainpage")

    def resize(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=785, height=500)
    
    

        # # track changes to the canvas and frame width and sync them,
        # # also updating the scrollbar
        # def _configure_interior(event):
        #     # update the scrollbars to match the size of the inner frame
        #     size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
        #     self.canvas.config(scrollregion="0 0 %s %s" % size)
        #     if interior.winfo_reqwidth() != self.canvas.winfo_width():
        #         # update the canvas's width to fit the inner frame
        #         self.canvas.config(width=interior.winfo_reqwidth())
        # interior.bind('<Configure>', _configure_interior)

        # def _configure_canvas(event):
        #     if interior.winfo_reqwidth() != self.canvas.winfo_width():
        #         # update the inner frame's width to fill the canvas
        #         self.canvas.itemconfigure(interior_id, width=self.canvas.winfo_width())
        # self.canvas.bind('<Configure>', _configure_canvas)


        

class Scroll2(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.canvas = tk.Canvas(parent, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")

        self.vsb = tk.Scrollbar(parent, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)


        # self.vsb.pack(side="right", fill="y")
        # self.canvas.pack(side="left", fill="both", expand=True)
        # self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
        #                           tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()

    def populate(self):
        self.grid_rowconfigure(0, minsize=100)
        self.grid_rowconfigure(1, minsize=100)
        self.grid_rowconfigure(2, minsize=100)
        self.grid_rowconfigure(3, minsize=100)
        self.grid_rowconfigure(4, minsize=100)
        self.grid_rowconfigure(5, minsize=100)
        self.hp_btn = tk.Button(self, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=2, column=0)
        self.hp_btn = tk.Button(self, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=3, column=0)
        self.hp_btn = tk.Button(self, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=4, column=0)
        self.hp_btn = tk.Button(self, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=5, column=0)
        self.hp_btn = tk.Button(self, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=6, column=0)
        self.hp_btn = tk.Button(self, text="Mainpage")
        self.hp_btn.bind('<Button-1>', self.mainpage)
        self.hp_btn.grid(row=7, column=0)
        

    def mainpage(self, login):
        self.controller.show_frame("Mainpage")

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
