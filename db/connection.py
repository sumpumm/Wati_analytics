import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

hostname = os.getenv("host")
database = os.getenv("database")
username = os.getenv("user_name")
password = os.getenv("password")
port_id = os.getenv("port_id")


def db_connection():
    return psycopg.connect(
                            host=hostname,
                            dbname=database,
                            user=username,
                            password=password,
                            port=port_id
                           )