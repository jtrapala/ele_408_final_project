

'''This is a test for using sqLite 3 with PINCode 
It creates a database for storing pins and names
Do not run if already made, I think it will make a blank copy
'''
import sqlite3 as lite
from sqlite3 import Error


conn = lite.connect('pin_dtb.db')
c = conn.cursor()

#Creates admin table
def adt():
	c.execute("""
		create table admins(
			user,
			pw);""")

#Creates user/pin/time table
def upt():
	c.execute("""create table users_pin(
		userN,
		userPin,
		time);""")

#u=(nm,users[nm])
#c.execute('insert into admins values (?,?)',u)

def unk_pin(c, code, time):
	u=('unknown', code, time)
	c.execute('insert into users_pin values (?,?,?)',u)


def kn_pin(c, users, nm, time):	
	u=(nm, users[nm], time)
	c.execute('insert into users_pin values (?,?,?)',u)



def db_upr(c):
	#from PINCode_1 import conn,c
	#Print USERS
	print "---------------USERS------------------------" 
	for row in c.execute('SELECT * FROM admins ORDER BY user'):
		print row
	print "\n"

def db_ppr(c):
	#from PINCode_1 import conn,c
	#Print PIN_ENTRIES
	print "---------------PIN_ENTRIES------------------" 
	for row in c.execute('SELECT * FROM users_pin ORDER BY userN'):
		print row
def db_close(conn):
	#from PINCode_1 import conn,c
	conn.close
	print "\nPIN Database is now closed"
	print "\n#####################################\n"






