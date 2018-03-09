import psycopg2
import sqlalchemy
import pandas.io.sql as psql
import DBconnection

def select():
    db = DBconnection.connecting()
    conn = db.connect()
    query = "SELECT * FROM 
    result_set = conn.execute(query)  
    for r in result_set:  
        print(r)

if __name__=='__main__': 
    select()