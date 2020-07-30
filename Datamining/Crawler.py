import requests
import re
import databaseCon

url = 'http://127.0.0.1/dataminingdemo/recipes/Recipe'
con = databaseCon.Database()


def getsourcecode(id):
    r = requests.get(url + str(id) + ".html");
    return r.text #getting inspect element data

def getUsers():
    users = []

    for i in range(1, 9): #we have 9 recipes in our deposition
        sourcecode = getsourcecode(i)
        for match in re.findall('<p id="userId">([0-9]+)', sourcecode):
            if match not in users:
                users.append(match) #The append() method in python adds a single item to the existing list.
                databaseCon.Database.insert(con, "INSERT INTO users(userName) VALUE ("+match+");")
    return users
print(getUsers())

def getRecipe():
    recipes = []
    for i in range(1,9):
        sourcecode = getsourcecode(i)
        for match in re.findall('<title>(.*)</title>', sourcecode):
            if match not in recipes:
                recipes.append(match)
                databaseCon.Database.insert(con, "INSERT INTO recipe(recipeName) VALUE ('" + match + "');")
    return recipes;

def getRatings():

print(getRecipe())

