import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="aniket",passwd="12345",database="college")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result = mycursor.fetchall() #also use ( fecthone ) data 

for i in result:
	print(i)