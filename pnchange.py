import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Nilesh@123",database="Atm")
s = con.cursor()

s.execute("update table account_details set")


