import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="hari@1234567",database="company")
mycursor=mydb.cursor()
mycursor.execute("insert into employee(id,ename) values(52,'hari')")

sql="insert into employee(id,ename)values(%s,%s)"
values=[(23,"prasanth"),
        (24,"kiran")
]

mycursor.executemany(sql,values)
mydb.commit()
mydb.close()
