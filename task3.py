ORIG_FILE = "f_original.txt"


def get_last_line(file_name):
    with open(file_name, "r+", encoding="utf-8") as f1:
        data = f1.readlines()
        result = []
        for line in range(len(data)):
            if line == len(data) -1:
                result += data[line]


def delete_last_line(file_name):
    with open(file_name, "r+", encoding="utf-8") as f1:
        data = f1.readlines()
        f1.seek(0)                   # vrátí kurzor na začátek
        f1.truncate()
        f1.writelines(data[:-1])



get_last_line(ORIG_FILE)
delete_last_line(ORIG_FILE)



#with open("f_new.txt", "w", encoding="utf-8") as f2:
# f2.writelines(line)


