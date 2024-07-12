import json

with open("employees.txt", "r+") as file:
    employee_list = json.load(file)[0:]
    print(employee_list)
    print(type(employee_list))

    new_dict = {}
    my_keys = ["first name", "last name", "age", "ID", "email"]
    my_values = [input("first name: "), input("last name: "), input("age: "), input("ID: "), input("email: ")]
    for key, value in zip(my_keys, my_values):
        new_dict[key] = value
    employee_list.append(new_dict)
    print(employee_list)
    file.write(json.dumps(employee_list))