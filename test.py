import json
FILE = "employees.txt"


def edit_list(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        emp_num = input("Zaměstnanec('emp_'): ")
        user_choice = input("Editovat (1 - first name, 2 - last name, 3- age, 4 - email): ")
        user_edit = input("Nový údaj: ")
        if user_choice == 1:
            new_list = employee_list.update({'emp1': {'first name': 'OOOO'}})
            a = {"first name: " + user_edit}
            for k1 in employee_list.keys():
                k1 == emp_num
                new_list = employee_list[k1][a]
            print(new_list)
        elif user_choice == 2:
            pass
        #elif user_choice == 3:
        #elif user_choice == 4:

        print(employee_list)

edit_list(FILE)