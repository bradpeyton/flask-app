import csv
from flask import Flask, request, render_template
import mysql.connector

DATABASE = mysql.connector.connect(
    host='mysql',
    user='root',
    password='secret',
    database='ecomm'
)

cursorObject = DATABASE.cursor()

DROP_TABLE = """DROP TABLE IF EXISTS `users`;"""
CREATE_TABLE = """CREATE TABLE `users` (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(40) NOT NULL, age INT);"""

cursorObject.execute(DROP_TABLE)
cursorObject.execute(CREATE_TABLE)
DATABASE.commit()
cursorObject.close()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

FILE = "people.csv"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def print(self):
        print(self.name, self.age)



try:
    with open(FILE, "r", encoding="utf-8") as file:
        cursorObject = DATABASE.cursor()
        reader = csv.DictReader(file)

        for row in reader:
            QUERY = "INSERT INTO `users` (first_name, age) VALUES (%s, %s);"
            VALUES = (row['name'].capitalize(), row['age'])
            cursorObject.execute(QUERY, VALUES)
            # row['name'] = Person(row['name'].capitalize(), row['age'])
            # people.append(row)

        DATABASE.commit()
        cursorObject.close()
        DATABASE.close()

except ValueError:
    print("There was an error")


DATABASE = mysql.connector.connect(
    host='mysql',
    user='root',
    password='secret',
    database='ecomm'
)
cursorObject = DATABASE.cursor()
QUERY = "SELECT * FROM `users`;"
cursorObject.execute(QUERY)
result = cursorObject.fetchall()
cursorObject.close()
DATABASE.close()

people = []

for key, name, age in result:
    person = {'key': key, 'name': name, 'age': age}
    people.append(person)


for person in people:
    print(person['key'], person['name'], person['age'])

# for person in people:
#     if person['name'] == 'Brad':
#         print(person['name'], person['age'])

# people = [
#     {"name": "Brad", "age": 51},
#     {"name": "Johnna", "age": 49},
#     {"name": "Ashlan", "age": 26},
#     {"name": "Skyler", "age": 25},
#     {"name": "Blake", "age": 22}
# ]

# for person in people:
#     # print(person["name"], person["age"])
#     person["name"] = Person(person["name"], person["age"])

# for person in people:
#     person["name"].print()
#     person["name"].birthday()
#     person["name"].print()
#     print()

# p1 = Person("Basil", 5)

# p1.print()
# p1.birthday()
# p1.print()


@ app.route("/")
def index():
    # name = request.args.get("name")
    # if name:
        # name.lower()
    # for person in people:
    #     if person['name'] == name:
    #         age = person['age']

    return render_template("index.html", len=len(people), people=people)
