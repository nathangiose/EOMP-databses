# Nathan John Giose
# Testing Database Connection


import mysql.connector

# Open Database Connetion


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC_online', auth_plugin='mysql_native_password')
cursor = mydb.cursor()

'''mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()'''


# Execute SQL query1
cursor.execute("Select Version()")
data = cursor.fetchone()
print("Database version : %s " % data)


# Disconnect from server
mydb.close()
