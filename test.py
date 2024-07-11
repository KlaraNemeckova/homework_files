def get_last_line(file_name):
    with open(file_name, "r+", encoding="utf-8") as f1:
        data = f1.readlines()
        result = []
        for line in range(len(data)):
            if line == len(data) -1:
                result += data[line]
        print(result)
        return result

