def get_last_line(file_name):
    with open(file_name, "r+", encoding="utf-8") as f1:
        data = list(f1.readlines())
        result = []
        for line in range(len(data)):
            if line == len(data) -1:
                result += data[line]
                print(data[line])


get_last_line("f_original.txt")

#with open("f_new.txt", "w", encoding="utf-8") as f2:
# f2.writelines(line)


