import mysql.connector
mycon=mysql.connector.connect(host='localhost',user="root",passwd='harsh@2002')
cur=mycon.cursor()
d="create database shop"
cur.execute(d)
mycon=mysql.connector.connect(host='localhost',user="root",passwd='harsh@2002',database='shop')
cur=mycon.cursor()
c="create  table todaysorder(id int(3),item varchar(2000),time varchar(30),day varchar(20));"
cur.execute(c)
i="insert into todaysorder values (100,NULL,NULL,NULL)"
cur.execute(i)
c="create  table login(user varchar(20),pass1 varchar(20));"
cur.execute(c)
i="insert into login values ('Admin','Admin123')"
cur.execute(i)
mycon.commit()
