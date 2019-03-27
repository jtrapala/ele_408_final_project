

'''This is a test for using sqLite 3 with PINCode 
It creates a database for storing pins and names
Do not run if already made, I think it will make a blank copy
'''
import sqlite3

sqlite_file='pin_database.sqlite'
table_name1= 'admin_pin_config'
new_field1='First Name'
field_type1='STRING'
new_field2='4 digit pin'
field_type2='STRING'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
print "PIN Database is now open for use"
