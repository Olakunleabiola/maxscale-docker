#
#
#
#

import mysql.connector


connection = mysql.connector.connect(user = "maxuser", password = "maxpwd", host = "127.0.0.1", port = "4000")

cursor = connection.cursor()




query = "SELECT * FROM zipcodes_one.zipcodes_one"

cursor.execute(query)

one_data = cursor.fetchall()

for row in one_data:
	print(row)
	break



query = "SELECT * FROM zipcodes_two.zipcodes_two"

cursor.execute(query)

two_data = cursor.fetchall()

for row in two_data:
	print(row)
	break





cursor.close()

connection.close()