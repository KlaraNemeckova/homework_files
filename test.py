import json

FILE = "employees.txt"


def delete_employee(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        print(employee_list)
        del employee_list[input("číslo zaměstnance, kterého chcete smazat: ")]
        print(employee_list)
        file.write(json.dumps(employee_list))


delete_employee(FILE)
