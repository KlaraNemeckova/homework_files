import json

FILE = "employees.txt"


def load_data(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        print(employee_list)
        for k, v in employee_list.items():
            print(k, v)
load_data(FILE)


def search_by_name(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        dict_low = json.dumps(employee_list)
        dict_lowercase = json.loads(dict_low.lower())
        print(dict_lowercase)
        last_name = input("Příjmení zaměstnance: ").lower()
        try:
            for k1 in dict_lowercase.keys():
                if last_name in dict_lowercase[k1].values():
                    print(k1, dict_lowercase[k1])
        except:
            print("Chyba při načítání souboru")
        file.write(json.dumps(employee_list))
    # main()


def edit_list():
    pass

    # main()



def add_employee(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        new_employee = {}
        new_dict = {}
        my_keys = ["first name", "last name", "age", "ID", "email"]
        my_values = [input("first name: "), input("last name: "), input("age: "), input("ID: "), input("email: ")]
        for key, value in zip(my_keys, my_values):
            new_dict[key] = value
        new_employee[input("")] = new_dict           # chyba...(zdvojený dictionary)
        employee_list.update(new_employee)
        file.write(json.dumps(employee_list))
        # main()


def delete_employee(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        del employee_list[input("Kterého zaměstnance chcete smazat? (´emp_´):  ")]
        file.write(json.dumps(employee_list))
        # main()


def search_by_name(file_name):
    with open(file_name, "r+") as file:
        employee_list = json.load(file)
        last_name = input("Příjmení zaměstnance: ")
        try:
            for k1 in employee_list.keys():
                if last_name in employee_list[k1].values():
                    print(k1, employee_list[k1])
        except:
            print("Nenalezeno")

       # main()


def select():
    pass
    # main()


def save_data():
    pass
    # main()


def main(file_name):
    while True:
        print("""--MENU-- \n1 = načíst data ze souboru \n2 = editace \n3 = přidat zaměstnance \n4 = smazat zaměstnance
              \n5 = vyhledat podle příjmení \n6 = vybrat zaměstnance dle věku nebo počátečního písmena
              \n7 = uložit změny \n8 = ukončit program""")

        choice = input("Vyberte možnost: ")

        if choice == "1":
            load_data(FILE)
        elif choice == "2":
            edit_list(FILE)
        elif choice == "3":
            add_employee(FILE)
        elif choice == "4":
            delete_employee(FILE)
        elif choice == "5":
            search_by_name(FILE)
        elif choice == "6":
            select(FILE)
        elif choice == "7":
            save_data(FILE)
        elif choice == "8":
            # save_data()
            break
        else:
            print("Neplatná volba")


main(FILE)
