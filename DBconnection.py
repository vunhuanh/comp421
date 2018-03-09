#import psycopg2
import sshtunnel
import sqlalchemy
import pandas.io.sql as psql
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine

try:

    with sshtunnel.SSHTunnelForwarder(
         ('comp421.cs.mcgill.ca', 22),
         #ssh_private_key="</path/to/private/ssh/key>",
         ### in my case, I used a password instead of a private key
         ssh_username="cs421g53",
         ssh_password="Gourmet53[]", 
         remote_bind_address=('localhost', 5432)) as server:

         server.start() #start ssh server
         print("server connected via SSH")


         engine = create_engine(r'postgres://cs421g53:Gourmet53[]@comp421.cs.mcgill.ca:5432/cs421')
         c = engine.connect()
         #conn = connect(host='comp421.cs.mcgill.ca',password='Gourmet53[]', database='cs421', user='cs421g53', port='5432')
         conn = c.connection
         curs = conn.cursor()
         print("database connected")
         conn.close()

except:
    print("Connection Failed")
