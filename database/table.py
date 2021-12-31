import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="hari@1234567",database="company")
mycursor=mydb.cursor()
mycursor.execute("create table employee(id int,ename varchar(50))")