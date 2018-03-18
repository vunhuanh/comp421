import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
import globalvar

# Frame for buying event tickets
class Reserve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        # Set min width to columns
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=150)
        self.grid_columnconfigure(2, minsize=150)
        self.grid_rowconfigure(2, minsize=10)
        
        # Header
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.desc = tk.Label(self, text="Make a reservation", wraplength=400)
        self.desc.grid(row=1, column=1)

        # Connect to DB and get info
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT licensenb, restaurantname FROM restaurant ORDER BY restaurantname;"
        result_set = conn.execute(query)  
        conn.close()

        licensenb = []
        restau = []
        for r in result_set:
            licensenb.append(r[0])
            restau.append(r[1])

        # Print relevant info
        self.name = tk.Label(self, text="Restaurant")
        self.name.grid(row=3, column=1)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self, text=restau[i])
            self.res.grid(row=irow, column=1)  
            self.ures = tk.Button(self, text="Reserve")
            print(licensenb[i])
            self.ures.bind('<Button-1>', lambda event, arg=licensenb[i]: self.mkres(event, arg))
            self.ures.grid(row=irow, column=2)

            i += 1 
            irow += 1

    def mkres(self, event, arg):
        globalvar.lnb_reserve = arg
        self.controller.show_frame("MakeReservation")
        print(globalvar.lnb_reserve)

    # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage")

# Frame for reserving table at a restaurant
class MakeReservation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):

        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize =150)
        self.grid_columnconfigure(2, minsize=150)
        self.grid_rowconfigure(2, minsize=10)

        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.desc = tk.Label(self, text="Make a Reservation")
        self.desc.grid(row=1, column=1)


        self.submit = tk.Button(self, text="Submit reservation")
        self.submit.bind('<Button-1>', self.submitReservation)
        self.submit.grid(row=3, column=0)
        self.time = tk.Label(self, text="Time")
        self.time.grid(row=3, column=1)
        self.date = tk.Label(self, text="Date")
        self.date.grid(row=3, column=2)
        self.qty = tk.Label(self, text="Number of diners")
        self.qty.grid(row=3, column=3)
        
        self.time2 = tk.Entry(self, width=10)
        self.time2.insert(0, "0")
        self.time2.grid(row=4, column=1)

        self.date2 = tk.Entry(self, width=10)
        self.date2.insert(0, "0")
        self.date2.grid(row=4, column=2)

        self.quantity = tk.Entry(self, width=10)
        self.quantity.insert(0, "0")
        self.quantity.grid(row=4, column=3)
       
    def submitReservation(self,event):
        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT r_table.licensenb, r_table.tableid, r_table.capacity FROM r_table,(SELECT licensenb, tableid FROM r_table WHERE exists (SELECT licensenb FROM restaurant WHERE LOCALTIME(0) > openinghours AND LOCALTIME(0) < closinghours AND restaurant.licensenb = r_table.licensenb) EXCEPT SELECT reservation_contains.licensenb, reservation_contains.tableid FROM reservation_contains WHERE EXISTS (SELECT licensenb FROM restaurant WHERE LOCALTIME(0) > openinghours AND LOCALTIME(0) < closinghours AND restaurant.licensenb = reservation_contains.licensenb)) as e WHERE r_table.licensenb = e.licensenb AND r_table.tableid = e.tableid AND r_table.licensenb = '{0}';".format(globalvar.lnb_reserve)
        result_set = conn.execute(query)
        conn.close()

        licenseNB = []
        tables = []
        capty = []

        # for r in result_set:
        #     licenseNB.append(r[0])
        #     print(r[0])
        #     tables.append(r[1])
        #     print(r[1])
        #     capty.append(r[2])
        #     print(r[2])
        u_time = time2.get()
        u_date = date2.get()
        u_quantity = quantity.get()

        print(u_time)
        print(u_date)
        print(u_quantity)

        # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage") 


