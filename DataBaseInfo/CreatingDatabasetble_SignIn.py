# Nathan John Giose

import mysql.connector


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()

'''mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()'''
cursor.execute("DROP TABLE IF EXISTS SIGN_IN") # Drop table if it exists already

query1 = "Create table SIGN_IN(" \
       "Sign_In int not null auto_increment," \
       "Sign_in_date date not null," \
       "Sign_in_time time not null," \
       "Sign_out_date date not null," \
       "Sign_out_time time not null," \
       "Primary key(Sign_In))"


cursor.execute(query1)

mydb.close()

