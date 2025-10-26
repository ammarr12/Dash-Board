import mysql.connector

mydb = mysql.connector.connect(
    
    host = "Your host_name",
    user = "Your user_name",
    password = "Your password"
)

cursor=mydb.cursor()
cursor.execute("use hospitaldataanalysis")
cursor.execute("select * from hospitaldata")

rows=cursor.fetchall()
columns=[i[0] for i in cursor.description] 
del rows [0]
del rows [0]


cursor.close()
mydb.close()
