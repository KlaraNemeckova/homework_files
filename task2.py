FILE_INPUT = "složka1.txt"
FILE_OUTPUT = open("složka2.txt", "w")


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
        print(char_count)
        return char_count


def lines (source_text):
    with open(source_text, "r") as txt:
        line_count = 0
        lines = txt.readlines()
        for l in lines:
            line_count += 1
        print(line_count)
        return line_count


def vowels(source_text):
    with open(source_text, "r") as txt:
        vow = "aeiouyAEIOUY"
        find_vowels = txt.read()
        vowels_count = sum(find_vowels.count(v) for v in vow)
        print(vowels_count)
        return vowels_count


def consonants (file_1, file_2):
    pass

def digits (file_1, file_2):
    pass


if __name__ == '__main__':
    try:
        char(FILE_INPUT)
        lines(FILE_INPUT)
        vowels(FILE_INPUT)
    except:
        print("Error")
