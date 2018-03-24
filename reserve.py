import Tkinter as tk  
import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
from sqlalchemy import Table, Column, String, MetaData
from changeglobal import setGlobal, getGlobal
import datetime

# Frame for buying event tickets
class Reserve(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.hp_btn = tk.Button(self, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.display_btn = tk.Button(self, text="Display")
        self.display_btn.bind('<Button-1>', self.display)
        self.display_btn.grid(row=1, column=0)

        #create_widgets(self.interior)

    # def create_widgets(self):
    #     Set min width to columns
    #     self.grid_columnconfigure(0, minsize=150)
    #     self.grid_columnconfigure(1, minsize=150)
    #     self.grid_columnconfigure(2, minsize=150)
    #     self.grid_rowconfigure(2, minsize=10)

    #     # Display
    #     self.display_btn = tk.Button(self, text="Display")
    #     self.display_btn.bind('<Button-1>', display(self.interior))
    #     self.display_btn.grid(row=0, column=4)

    def resize(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"), width=985, height=500)
        
    # Display page contents
    def display(self, event):

        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0)

        self.vsbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.vsbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsbar.set)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.interior, anchor='nw')

        self.interior.bind("<Configure>", self.resize)
        self.interior.grid_columnconfigure(0, minsize=150)
        self.interior.grid_columnconfigure(1, minsize=150)
        self.interior.grid_columnconfigure(2, minsize=150)

        self.hp_btn = tk.Button(self.interior, text="Homepage")
        self.hp_btn.bind('<Button-1>', self.homepage)
        self.hp_btn.grid(row=0, column=0)

        self.display_btn = tk.Button(self.interior, text="Display")
        self.display_btn.bind('<Button-1>', self.display)
        self.display_btn.grid(row=1, column=0)

        self.desc = tk.Label(self.interior, text="Make a reservation", wraplength=400)
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
        self.name = tk.Label(self.interior, text="Restaurant")
        self.name.grid(row=3, column=1)

        irow = 4
        i = 0
        for r in restau:
            self.res = tk.Label(self.interior, text=restau[i])
            self.res.grid(row=irow, column=1)  
            self.ures = tk.Button(self.interior, text="Reserve")
            print(licensenb[i])
            self.ures.bind('<Button-1>', lambda event, arg=licensenb[i]: self.mkres(event, arg))
            self.ures.grid(row=irow, column=2)

            i += 1 
            irow += 1

    def mkres(self, event, arg):
        setGlobal('lnb_reserve',arg)
        self.controller.show_frame("MakeReservation")

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

        # Display
        self.display_btn = tk.Button(self, text="Display")
        self.display_btn.bind('<Button-1>', self.display)
        self.display_btn.grid(row=1, column=0)
        
    # Display page contents
    def display(self, event):

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
        #Get user input 
        self.u_time = self.time2.get()
        self.u_date = self.date2.get()
        self.u_quantity = self.quantity.get()

        licensenb = getGlobal('lnb_reserve')
        useremail = getGlobal('useremail')

        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT r_table.licensenb, r_table.tableid, r_table.capacity FROM r_table, (SELECT licensenb, tableid FROM r_table EXCEPT SELECT reservation_contains.licensenb, reservation_contains.tableid FROM reservation, reservation_contains WHERE reservation.reservationid = reservation_contains.reservationid AND reservation.time::date = '{0}') AS e WHERE r_table.licensenb = e.licensenb AND r_table.tableid = e.tableid AND r_table.licensenb = '{1}' ORDER BY r_table.tableid;".format(self.u_date,licensenb)
        result_set = conn.execute(query)
        conn.close()

        db = DBconnection.connecting()
        conn = db.connect()
        query = "SELECT licensenb FROM restaurant WHERE restaurant.licensenb = '{0}' AND (restaurant.openinghours < '{1}' OR restaurant.closinghours > '{2}');".format(licensenb,self.u_time,self.u_time)
        result_set2 = conn.execute(query)
        conn.close()


        licenseNB = []
        tables = []
        capty = []


        for r in result_set:
            licenseNB.append(r[0])
            print(r[0])
            tables.append(r[1])
            print(r[1])
            capty.append(r[2])
            print(r[2])

        licenseNB2 = []
        for r2 in result_set2:
            licenseNB2.append(r2[0])

        #FOR TESTING PURPOSES, CHECKING IF TABLES SORTED BY TABLE ID NUMBER
        # print("BREAK///")

        # print(tables)
        # print(capty)

        #get total seats available across all tables
        total_seats = 0
        for c in capty:
            total_seats+=c

        print("total seats avail: ")
        print(total_seats)

        print("total quant input: " + self.u_quantity)

        timestamp = self.u_date + " " + self.u_time

        if(int(self.u_quantity) > total_seats):
            print("There aren't enough seats to accomodate the number of diners mentioned.")
            print("Reservation failed")

        #Checking if time input falls between opening hours and closing hours for the restaurant
        elif(not licenseNB2):
            print("Nope, not happening.")

        #Verifying date format
        # elif(validate(self.u_date)):
        #     print("Wrong date format")

        else:
            print(useremail)

            db = DBconnection.connecting()
            conn = db.connect()
            conn.autocommit = True
            query = "SELECT reservationid FROM reservation ORDER BY reservationid DESC LIMIT 1;"
            rid = conn.execute(query)
            conn.close()

            for r in rid:
                real_rid = r[0] + 1

            # db = DBconnection.connecting()
            # conn = db.connect()
            # conn.autocommit = True
            # query2 = "SELECT * FROM make_reservation('{0}',{1},'{2}','{3}',{4});".format(useremail,real_rid,licensenb,timestamp,self.u_quantity)
            # result3 = conn.execute(query2)
            # conn.close()

            # for e in result3:
            #     wreck = e[0]


            db = DBconnection.connecting()
            conn = db.connect()
            conn.autocommit = True
            query = "INSERT INTO reservation VALUES({0},'{1}',{2});".format(real_rid,timestamp,self.u_quantity)
            conn.execute(query)
            conn.close()

            db = DBconnection.connecting()
            conn = db.connect()
            conn.autocommit = True
            query = "INSERT INTO user_books VALUES('{0}',{1});".format(useremail,real_rid)
            conn.execute(query)
            conn.close()

            peopleLeft = int(self.u_quantity)
            i = 0
            while(peopleLeft > 0):
                print(tables[i])
                db = DBconnection.connecting()
                conn = db.connect()
                conn.autocommit = True
                query = "INSERT INTO reservation_contains VALUES({0},'{1}',{2});".format(real_rid,licensenb,tables[i])
                conn.execute(query)
                conn.close()

                peopleLeft=peopleLeft-capty[i]
                i=i+1


            # for r in res:
            #     print(r)

            # db = DBconnection.connecting()
            # conn = db.connect()
            # query ="WITH email AS (SELECT '{0}' AS var), rid AS (SELECT reservationid AS var FROM reservation WHERE reservationid >= ALL (SELECT reservationid FROM reservation)) INSERT INTO user_books SELECT email.var, rid.var FROM email, rid;".format(useremail)
            # conn.execute(query)
            # conn.close()

            # db = DBconnection.connecting()
            # conn = db.connect()
            # query = "WITH att AS (SELECT reservationid AS var FROM (SELECT * FROM reservation WHERE reservationid >= ALL (SELECT reservationid FROM reservation)) as latest WHERE reservationid = latest.reservationid), restau AS (SELECT '{0}' AS var), tablenb AS (SELECT 2 AS var) INSERT INTO reservation_contains SELECT att.var, restau.var, tablenb.var FROM att, restau, tablenb;".format(licensenb)
            # conn.execute(query)
            # conn.close()


        # Go to homepage
    def homepage(self, event):
        self.controller.show_frame("Homepage") 

    # def validate(date_text):
    #         try:
    #             datetime.datetime.strptime(date_text, '%Y-%m-%d')
    #         except:
    #             raise ValueError("Incorrect data format, should be YYY-MM-DD")

