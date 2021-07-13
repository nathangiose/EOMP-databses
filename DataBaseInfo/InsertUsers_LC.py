# Nathan John Giose

import mysql.connector

mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()

sql1 = "Insert into USERS(ID, name, surname, phone, password, role) VALUES ('9512285835083', 'Abdullah', 'Isaacs', '0734425442', '8-2fermENt2020', 'Student') "

try:
    cursor.execute(sql1)
    mydb.commit()
except:
    mydb.rollback()

mydb.close()
