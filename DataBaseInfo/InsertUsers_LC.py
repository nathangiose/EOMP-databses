# Nathan John Giose

import mysql.connector

mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC_online', auth_plugin='mysql_native_password')
cursor = mydb.cursor()

sql1 = "Insert into LC(ID, First_Name, Last_Name, ID_number, phone_number, Password, Role) VALUES ('1', 'Abdullah', 'Isaacs', '9512285835083', '0734425442', '8-2fermENt2020', 'Student') "

try:
    cursor.execute(sql1)
    mydb.commit()
except:
    mydb.rollback()

mydb.close()
