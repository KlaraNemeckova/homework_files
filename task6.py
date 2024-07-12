FILE = "file_3.txt"

import re

word = input("Jaké slovo chcete nahradit?: ")
new_word = input("Nové slovo: ")


def replace(file_name):
    with open(file_name, "r+", encoding="utf-8") as f:
        data = f.read()
        try:
            new_data = re.sub(r"\b" + word + r"\b", new_word, data)
            f.seek(0)
            f.truncate()
            f.write(new_data)
            if word not in data:
                print("Toto slovo se v textu nevyskytuje.")
        except FileNotFoundError:
            print("Chyba při načítání souboru")



replace(FILE)