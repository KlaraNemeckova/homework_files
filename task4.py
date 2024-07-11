FILE = "longest.txt"


def longest_line(file_name):
    with open(file_name, "r+", encoding="utf-8") as f:
        data = f.readlines()
        new_line = ""
        for line in data:
            if len(line) > len(new_line):
                new_line = line
        print("Nejdelší řádek je: " + new_line + "\na jeho délka je: " + str(len(new_line) - 1) + " znaků.")


longest_line(FILE)
