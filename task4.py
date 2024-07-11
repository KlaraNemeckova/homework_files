FILE = "longest.txt"


def longest_line(file_name):
    with open(file_name, "r+", encoding="utf-8") as f:
        data = f.readlines()
        new_line = ""
        for line in data:
            if len(line) > len(new_line):
                print(line)
                new_line = line
            print(len(new_line) -1)

longest_line(FILE)
