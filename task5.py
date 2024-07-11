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
            print(counter)
        except:
            print("Zadané slovo se v textu nenachází.")

word_count(FILE)




