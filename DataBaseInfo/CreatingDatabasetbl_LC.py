# Nathan John Giose

import mysql.connector


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS USERS") # Drop table if it exists already

query = "Create table USERS(" \
        "ID varchar(13) NOT NULL," \
        "name varchar(25) NOT NULL," \
        "surname varchar(25) NOT NULL," \
        "phone varchar(13) NOT NULL," \
        "role varchar(30) NOT NULL," \
        "password varchar(25) NOT NULL," \
        "Primary key(ID))"


cursor.execute(query)

mydb.close()


