import json

FILE = "employees.txt"


def add_employee(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        new_employee = {}
        new_dict = {}
        my_keys = ["first name", "last name", "age", "ID", "email"]
        my_values = [input("first name: "), input("last name: "), input("age: "), input("ID: "), input("email: ")]
        for key, value in zip(my_keys, my_values):
            new_dict[key] = value
        new_employee[input("")] = new_dict                 # automatické počítání "emp" + n
        employee_list.update(new_employee)
        file.write(json.dumps(employee_list))

add_employee(FILE)