FILE_1 = "file_1.txt"
FILE_2 = "file_2.txt"

def compare_files(f1_name, f2_name):
    with open("file_1.txt", "r", encoding="utf8") as f1_text:
        f1 = list(f1_text.readlines())
    with open("file_2.txt", "r", encoding="utf8") as f2_text:
        f2 = list(f2_text.readlines())
    txt1_diff = " "
    txt2_diff = " "
    for line_1,line_2 in zip(f1,f2):
        if line_1 not in f2:
            txt1_diff += line_1
    for line_1,line_2 in zip(f1,f2):
        if line_2 not in f1:
            txt2_diff += line_2

    print(f"odlišný text v {FILE_1}: {txt1_diff}")
    print(f"odlišný text v {FILE_2}: {txt2_diff}")
compare_files(FILE_1, FILE_2)




