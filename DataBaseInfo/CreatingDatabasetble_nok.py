# Nathan John Giose

import mysql.connector


mydb = mysql.connector.connect(user='NATHAN', password='8-2fermENt2020', host='localhost', database='LC', auth_plugin='mysql_native_password')
cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS NOK") # Drop table if it exists already

query = "Create table NOK(" \
        "position int NOT NULL auto_increment," \
        "NOK_name varchar(25) default NOT NULL," \
        "NOK_phone varchar(13) NOT NULL," \
        "PRIMARY KEY (position)" \
        "FOREIGN KEY (NOK_name) REFERENCES `users` (`id_number`))"


cursor.execute(query)

mydb.close()


