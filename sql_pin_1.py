

'''This is a test for using sqLite 3 with PINCode 
It creates a database for storing pins and names
Do not run if already made, I think it will make a blank copy
'''
import sqlite3 as lite
from sqlite3 import Error


sqlite_file='pin_database.db'
'''
table_name1= 'admin_pin_config'
new_field1='First Name'
field_type1='STRING'
new_field2='4 digit pin'
field_type2='STRING'
'''

def create_connection(sqlite_file):

    try:
        conn = lite.connect(sqlite_file)
        print lite.version
        print "PIN Database is now open for use"
    except Error as e:
        print e
    finally:
        close_con(conn)

def close_con(connection):
    connection.close()

if __name__ == '__main__':
    create_connection("C:\Users\aamim\Documents\GitHub\ele_408_final_project")
#c = conn.cursor()