import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

hostname = os.getenv("hostname")
database = os.getenv("database")
username = os.getenv("username")
pwd = os.getenv("pwd")
port_id = os.getenv("port_id")

def db_connection():
    return psycopg.connect(
                            host=hostname,
                            dbname=database,
                            user=username,
                            password=pwd,
                            port=port_id
                           )