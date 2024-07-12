import json

FILE = "employees.txt"


def load_data():
    pass


def edit_list():
    pass


def add_employee(file_name):
    with open(file_name, "r+") as file:
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

add_employee(FILE)


def delete_employee():
    pass


def search_by_name():
    pass


def select():
    pass


def save_data():
    pass


# def main(file_name):
#     while True:
#         print("""--MENU-- \n1 = načíst data ze souboru \n2 = editace \n3 = přidat zaměstnance \n4 = smazat zaměstnance
#               \n5 = vyhledat podle příjmení \n6 = vybrat zaměstnance dle věku nebo počátečního písmena
#               \n7 = uložit změny \n8 = ukončit program""")
#
#         choice = input("Vyberte možnost: ")
#
#         if choice == "1":
#             load_data()
#         elif choice == "2":
#             edit_list()
#         elif choice == "3":
#             add_employee(FILE)
#         elif choice == "4":
#             delete_employee()
#         elif choice == "5":
#             search_by_name()
#         elif choice == "6":
#             select()
#         elif choice == "7":
#             save_data()
#         elif choice == "8":
#             # save_data()
#             break
#         else:
#             print("Neplatná volba")
#
#
# main()



