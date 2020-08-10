import mysql.connector


class Database:

    def __init__(self):
        self.connection = mysql.connector.connect(  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="admin",               #password for user
  database="datamining",               #database name
    auth_plugin = 'mysql_native_password', use_pure= False)  # change here if you need any changes
        self.cursor = self.connection.cursor()
                # REMEMBER THIS. GOT STUCK HERE
    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()

    def selectAll(self):
        data = []
        users = []
        items = []
        ratings = []

        self.cursor.execute("SELECT rating, users_idUsers, Recipe_idRecipe from rating;")
        rows = self.cursor.fetchall()

        for r in rows:
            ratings.append(r[0])
            users.append(r[1])
            items.append(r[2])

        data.append(users)
        data.append(items)
        data.append(ratings)

        return data
