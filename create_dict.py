import json

dictionary = {
    "first name": "Lydia",
    "last name": "Parks",
    "age": "38",
    "ID": "4522",
    "email": "l.parks@company.com",

}, {
    "first name": "Simon",
    "last name": "Kinney",
    "age": "27",
    "ID": "4535",
    "email": "s.kinney@company.com"

}, {
    "first name": "Camilo",
    "last name": "Santiz",
    "age": "41",
    "ID": "4538",
    "email": "c.santiz@company.com",

},{
    "first name": "Kristie",
    "last name": "Tsujimoto",
    "age": "33",
    "ID": "4541",
    "email": "k.tsujimoto@company.com",

}

file = open('employees.txt', 'w+')
file.write(json.dumps(dictionary))

file.close()


