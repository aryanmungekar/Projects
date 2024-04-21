import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='12345678')


cur = mydb.cursor()

cur.execute("CREATE DATABASE abc")  #creates a new database

#cur.execute("DROP DATABASE abc")    #deletes the database