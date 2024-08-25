# database create and tanle create
# >pip install mysqlx.connector.python
import mysql.connector as mc
conn=mc.connect(host="localhost",user="root",password="nisha@21",database="bikes")
# if(conn.is_connected()):
#     print("connection established")
# else:
#     print("unable")
# for sqlite user-------->
# import sqlite3
# conn=sqlite3('bikedata.db')
query_to_create_table="""
CREATE TABLE Bike_details(owner INT,
brand VARCHAR(40),
kms_driven INT,
age INT,
predicted_price INT)"""
cur=conn.cursor()
cur.execute(query_to_create_table)
print("your database and table is created")
cur.close()
conn.close()