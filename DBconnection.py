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

            db = create_engine(r'postgres://cs421g53:Gourmet53[]@comp421.cs.mcgill.ca:5432/cs421')
            return db


    except:
        print("Connection Failed")


if __name__ == "__main__":
    connecting()

