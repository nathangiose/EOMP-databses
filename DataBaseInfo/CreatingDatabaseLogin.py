import CreatingDatabasetbl_LC
import CreatingDatabasetble_SignIn
import mysql.connector

user_id = "NATHAN"
password = "8-2fermENt2020"

con.execute('insert into Login values("%s", "%s")' % \
            (user_id, password))
