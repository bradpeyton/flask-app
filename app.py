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

CREATE_TABLE = """DROP TABLE IF EXISTS users;
                CREATE TABLE users (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                first_name VARCHAR(40) NOT NULL,
                age INT)"""

res = cursorObject.execute(CREATE_TABLE)

DATABASE.close()

print(res)

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


people = []

try:
    with open(FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print(row['name'], row['age'])
            # row['name'] = Person(row['name'].capitalize(), row['age'])
            people.append(row)
except ValueError:
    print("There was an error")

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
    name = request.args.get("name")
    if name:
        name.lower()
    # for person in people:
    #     if person['name'] == name:
    #         age = person['age']

    return render_template("index.html", len=len(people), people=people)