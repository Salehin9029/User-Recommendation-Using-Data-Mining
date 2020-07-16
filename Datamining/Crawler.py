import requests
import re
url = 'http://127.0.0.1/dataminingdemo/recipes/Recipe'

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

    return users;
print(getUsers())
