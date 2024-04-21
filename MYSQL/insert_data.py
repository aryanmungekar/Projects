import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='abc'
)

cur=mydb.cursor()

#cur.execute("DROP DATABASE abc") 

#s = "CREATE TABLE subjects (dsa varchar(20), statistics varchar(20), iot varchar(20))"
#cur.execute(s)

t = "INSERT INTO subjects (dsa,statistics,iot) VALUES(%s,%s,%s)"
v=(12,23,34)
grp=[(23,12,55),(21,34,12)]

cur.execute(t,v)                   #for single data entry
cur.executemany(t,grp)             #for multiple data entry
mydb.commit()
