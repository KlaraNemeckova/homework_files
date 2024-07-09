FILE_1 = "file_1.txt"
FILE_2 = "file_2.txt"

def compare_files(f1_name, f2_name):
    with open("file_1.txt", "r", encoding="utf8") as f1_text:
        f1 = f1_text.readlines()
    with open("file_2.txt", "r", encoding="utf8") as f2_text:
        f2 = f2_text.readlines()

    for line_1 in f1:
        for line_2 in f2:
            if line_1 != line_2:
                pass
            elif line_1 == line_2:
                print(line_1)
            else:
                print("kontrola")

compare_files(FILE_1, FILE_2)



