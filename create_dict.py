import json

dictionary = {
    "emp1": {
        "first name": "Lydia",
        "last name": "Parks",
        "age": "38",
        "ID": "4522",
        "email": "l.parks@company.com",

    },
    "emp2": {
        "first name": "Simon",
        "last name": "Kinney",
        "age": "27",
        "ID": "4535",
        "email": "s.kinney@company.com"

    },
    "emp3": {
        "first name": "Camilo",
        "last name": "Santiz",
        "age": "41",
        "ID": "4538",
        "email": "c.santiz@company.com",

    },
    "emp4": {
        "first name": "Kristie",
        "last name": "Tsujimoto",
        "age": "33",
        "ID": "4541",
        "email": "k.tsujimoto@company.com",
    }
}

file = open('employees.txt', 'w+')
file.write(json.dumps(dictionary))

file.close()

