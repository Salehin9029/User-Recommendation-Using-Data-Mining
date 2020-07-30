import mysql.connector


class Database:

    def __init__(self):
        self.connection = mysql.connector.connect(  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="admin",               #password for user
  database="datamining",               #database name
    auth_plugin = 'mysql_native_password', use_pure= False)  # change here if you need any changes
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()
