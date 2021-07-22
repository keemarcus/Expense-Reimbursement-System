# import connect function in order to establish a connection to out database using pyodbc
from pyodbc import connect

# import os to pull our environment variables
import os

# get db credentials from system variables so that they aren't exposed in code
db_url = os.environ['Project_0_db_url']
db_username = os.environ['Project_0_db_username']
db_password = os.environ['Project_0_db_password']
db_name = ''


# this function will return a new connection to the database
def get_connection():
    return connect(f"DRIVER={{PostgreSQL UNICODE(x64)}};SERVER={db_url};PORT=5432;DATABASE={db_name};UID={db_username};PWD={db_password};Trusted_Connection=no;BoolsAsChar=0")
