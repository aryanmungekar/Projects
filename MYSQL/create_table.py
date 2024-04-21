import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='abc'    
    )

cur = mydb.cursor()

t = "CREATE TABLE subjects(dsa varchar(20), statistics float(5,2), iot varchar(20))"
cur.execute(t)




