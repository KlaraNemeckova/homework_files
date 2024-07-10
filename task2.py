FILE_INPUT = "složka1.txt"
FILE_OUTPUT = "složka2.txt"


def get_text(file_1):
    try:
        text = open(file_1, "r")
        source_text = text.read()
        return source_text
    except:
        print("Chyba při načítání souboru")
    finally:
        text.close()


def char(source_text):
    with open(source_text, "r") as txt:
        characters = txt.readlines()
        char_count = sum(len(word) for word in characters)
        return char_count


def lines(source_text):
    with open(source_text, "r") as txt:
        lines_count = 0
        lines = txt.readlines()
        for l in lines:                  # na jeden řádek
            lines_count += 1
        return lines_count


def vowels(source_text):
    with open(source_text, "r") as txt:
        vow = "aeiouyAEIOUY"
        find_vowels = txt.read()
        vowels_count = sum(find_vowels.count(v) for v in vow)
        return vowels_count


def consonants(source_text):
    with open(source_text, "r") as txt:
        vow = "aeiouyAEIOUY"
        find_vowels = txt.read()
        cons_count = 0
        for c in find_vowels:
            if c not in vow:            # dát do jedné funkce s vowels + not digit
                cons_count += 1
        return cons_count


def digits(source_text):
    with open(source_text, "r") as txt:
        digits = txt.read()
        digits_count = 0
        for i in digits:                # na jeden řádek
            if i.isdigit():
                digits_count += 1
        return digits_count


if __name__ == '__main__':
    try:
        char(FILE_INPUT)
        lines(FILE_INPUT)
        vowels(FILE_INPUT)
        consonants(FILE_INPUT)
        digits(FILE_INPUT)
        def result(file_2):
            with open(file_2, "a+") as txt:
                new_text = txt.write(str(char(FILE_INPUT)) + "\n")
                print(new_text)
        result(FILE_OUTPUT)
    except:
        print("Error")
