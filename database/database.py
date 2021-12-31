import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="hari@1234567")
mycursor=mydb.cursor()
mycursor.execute("create database org")