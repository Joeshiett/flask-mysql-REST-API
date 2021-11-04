import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='joseph',
    password='password'
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE test")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)