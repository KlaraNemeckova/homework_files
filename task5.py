FILE = "f_original.txt"

word = input("Hledané slovo: ")


def word_count(file_name):
    with (open(file_name, "r+", encoding="utf-8") as f):
        text = f.read().split()
        counter = 0
        try:
            for line in text:
                if word in line:
                    counter += 1
            if counter != 0:
                print(f"´{word}´ se v textu vyskytuje {counter}x.")
            else:
                print("Zadané slovo se v textu nenachází.")
        except:
            print("Chyba při načítání souboru")

word_count(FILE)




