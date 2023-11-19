#!/home/tedy/.pyenv/shims/python3

BOOK = "./books/frankenstein.txt"

def oper_file():
    with open(BOOK) as f:
        file_contents = f.read()
        return file_contents



def count_letters(text):
    letters = {}
    for ch in text.lower():
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1 

    return letters

def make_list(dic):
    sorted_list = []
    for k in dic:
        if k.isalpha():
            sorted_list.append((k, dic[k]))

    sorted_list.sort()

    return sorted_list


def main():
    print(f"--- Begin report of {BOOK} ---")
    file = oper_file()
    words = file.split()
    print(f"{len(words)} words found in the document")
    letters = count_letters(file)
    sorted_list = make_list(letters)
    for item in sorted_list:
        print(f"The '{item[0]}' character was found {item[1]} times.")


main()
