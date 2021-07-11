# Nathan John Giose

import mysql.connector


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC_online', auth_plugin='mysql_native_password')
cursor = mydb.cursor()

'''mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()'''
cursor.execute("DROP TABLE IF EXISTS LC") # Drop table if it exists already

query = "Create table LC(" \
       "ID int unsigned not null auto_increment," \
       "First_Name varchar(25) not null," \
       "Last_Name varchar(25) not null," \
       "ID_number int(13) not null," \
       "phone_number varchar(12) not null," \
       "Password varchar(30) not null," \
       "Role varchar(25) not null," \
       "Primary key(ID))"


cursor.execute(query)

mydb.close()

