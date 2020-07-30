import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="admin",               #password for user
  database="datamining",               #database name
    auth_plugin = 'mysql_native_password', use_pure= False
)