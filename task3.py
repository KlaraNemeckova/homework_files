ORIG_FILE = "f_original.txt"


def delete_last_line(file_name):
    with open(file_name, "r+", encoding="utf-8") as f1, open("f_new.txt", "w", encoding="utf-8") as f2:
        data = f1.readlines()
        f1.seek(0)                   # vrátí kurzor na začátek
        f1.truncate()
        f1.writelines(data[:-1])
        f2.writelines(data[:-1])


delete_last_line(ORIG_FILE)







