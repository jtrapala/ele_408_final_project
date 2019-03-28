

'''This is a test for using sqLite 3 with PINCode 
It creates a database for storing pins and names
Do not run if already made, I think it will make a blank copy
'''
import sqlite3 as lite
from sqlite3 import Error


#sqlite_file='pin_database.db'
'''
table_name1= 'admin_pin_config'
new_field1='First Name'
field_type1='STRING'
new_field2='4 digit pin'
field_type2='STRING'
'''
    
     
conn = lite.connect("pin_database.db")
print lite.version
print "PIN Database is now open for use"
conn.close
print "PIN Database is now closed"

def create_table(conn, table_name):
    cu = conn.cursor()
    cu.execute()