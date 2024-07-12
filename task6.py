FILE = "file_3.txt"

word = input("Jaké slovo chcete nahradit?: ")
new_word = input("Nové slovo: ")


def replace(file_name):
    with open(file_name, "r+", encoding="utf-8") as f:
        data = f.read()
        try:
            new_data = data.replace(word, new_word)
            f.seek(0)
            f.truncate()
            f.write(new_data)
            #if word not in f:
                #print("Toto slovo se v textu nevyskytuje.")
        except FileNotFoundError:
            print("Chyba při načítání souboru")



replace(FILE)