FILE = "file_3.txt"

word = input("Jaké slovo chcete nahradit?: ")
new_word = input("Nové slovo: ")


def replace(file_name):
    with open(file_name, "r+", encoding="utf-8") as f:
        text = f.read()
        try:
            pass
        except:
            print("Chyba při načítání souboru")

replace(FILE)