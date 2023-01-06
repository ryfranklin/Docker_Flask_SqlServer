# from flask import current_app, g
from dotenv import dotenv_values
import pyodbc
# dictionary containing environment variables
config = dotenv_values("../.env")
print(config["SERVER"])

cnxn = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                      + 'SERVER={};DATABASE={};ENCRYPT=yes;UID={};PWD={}'
                      .format(config["SERVER"],
                              config["DATABASE"],
                              config["USERNAME"],
                              config["PASSWORD"]))

cursor = cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
