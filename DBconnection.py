import sshtunnel
import sqlalchemy
import pandas.io.sql as psql
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine


def connecting():
    try:

        with sshtunnel.SSHTunnelForwarder(
            ('comp421.cs.mcgill.ca', 22),
            ssh_username="cs421g53",
            ssh_password="Gourmet53[]", 
            remote_bind_address=('localhost', 5432)) as server:

            server.start() #start ssh server
            print "Server connected"

<<<<<<< HEAD
         db = create_engine('postgres://cs421g53:Gourmet53[]@comp421.cs.mcgill.ca:5432/cs421')
         print("yes")
         conn = db.connect()
         #conn = connect(host='comp421.cs.mcgill.ca',password='Gourmet53[]', database='cs421', user='cs421g53', port='5432')
         print("database connected")
         result = conn.execute('SELECT * from restaurant')
         for r in result:
            print(r)
         conn.close()

except:
    print("Connection Failed")




=======
            db = create_engine(r'postgres://cs421g53:Gourmet53[]@comp421.cs.mcgill.ca:5432/cs421')
            return db


    except:
        print("Connection Failed")

>>>>>>> master
