import mysql.connector

mydb = mysql.connector.connect(
    
    host = "127.0.0.1",
    user = "root",
    password = "qwerty1234"
)

cursor=mydb.cursor()
cursor.execute("use dashboard")
cursor.execute("select * from hospitaldataanalysis")

rows=cursor.fetchall()
columns=[i[0] for i in cursor.description] 
del rows [0]
del rows [0]

print(rows)
cursor.close()
mydb.close()
