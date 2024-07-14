import json

FILE = "employees.txt"


def search_by_name(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        for k1 in employee_list.keys():
            for k2,v in zip(employee_list[k1].values(),employee_list[k2].values()):
                employee_list[k2.lower()] = v.lower()
        print(employee_list)
        last_name = input("Příjmení zaměstnance: ")
        try:
            for k1 in employee_list.keys():
                if last_name in employee_list[k1].values():
                    print(k1, employee_list[k1])
        except:
            print("Nenalezeno")

search_by_name(FILE)
