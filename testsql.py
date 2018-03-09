import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection
<<<<<<< HEAD
from sqlalchemy import Table, Column, String, MetaData
=======
>>>>>>> master

def select():
    db = DBconnection.connecting()
    conn = db.connect()
<<<<<<< HEAD
    table = "restaurant"
    query = "SELECT * FROM {0}".format(table)
    query2 = "hi"
    query1 = "SELECT restaurantname, restaurant.licensenb, round (AVG (rating), 2) as average_rating FROM review JOIN restaurant ON review.licensenb = restaurant.licensenb GROUP BY restaurant.licensenb LIMIT 49;"
    result_set = conn.execute(query)  
    for r in result_set:  
        #get the first column
        print(r[0])
        #get the second column



def update():
    db = DBconnection.connecting()
    conn = db.connect()
=======
    query = "SELECT * FROM 
    result_set = conn.execute(query)  
    for r in result_set:  
        print(r)
>>>>>>> master

if __name__=='__main__': 
    select()