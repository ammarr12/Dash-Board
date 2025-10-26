import mysql.connector

mydb = mysql.connector.connect(
    
    host = "127.0.0.1",
    user = "root",
    password = "ammar123"
)

cursor=mydb.cursor()
cursor.execute("use hospitaldataanalysis")
cursor.execute("select * from hospitaldata")

rows=cursor.fetchall()
columns=[i[0] for i in cursor.description] 
del rows [0]
del rows [0]

print(rows)
cursor.close()
mydb.close()
