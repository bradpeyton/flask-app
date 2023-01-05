import csv
from flask import Flask, render_template
from mysql.connector import connect, Error
import yaml
from mysqlconf import kwargs

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# with open('database.yml', encoding='utf-8') as file:
#     db = yaml.safe_load(file)


FILE = "people.csv"

try:
    DATABASE = connect(**kwargs)
except Error as error_message:
    print("Could not connect to database: ", error_message)
    exit(1)

QUERY = """
        DROP TABLE IF EXISTS `users`;
        CREATE TABLE `users` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(40) NOT NULL,
            age INT
        ) ENGINE = InnoDB;
        """
try:
    cursor = DATABASE.cursor()
    cursor.execute(QUERY, multi=True)
except Error as error_message:
    print("Error creating table: ", error_message)
    exit(1)


try:
    DATABASE = connect(**kwargs)
except Error as error_message:
    print("Error connecting to database: ", error_message)
    exit(1)


try:
    cursor = DATABASE.cursor()
    with open(FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            QUERY = "INSERT INTO `users` (first_name, age) VALUES (%s, %s);"
            VALUES = (row['name'].capitalize(), row['age'])
            cursor.execute(QUERY, VALUES)
        DATABASE.commit()
except Error as error_message:
    print("Error inserting data: ", error_message)
    exit(1)

try:
    QUERY = "SELECT * FROM `users`;"
    cursor.execute(QUERY)
    result = cursor.fetchall()
    cursor.close()
    DATABASE.close()
except Error as error_message:
    print("Error selecting data: ", error_message)
    exit(1)

people = []

for key, name, age in result:
    person = {'key': key, 'name': name, 'age': age}
    people.append(person)

for person in people:
    print(person['key'], person['name'], person['age'])


@ app.route("/")
def index():
    return render_template("index.html", len=len(people), people=people)
