def is_vowel(i):
    return i in ["a", "o", "e", "i", "u"]


def characters_info(pathway):
    f1 = open("text2.txt", "r")
    content = f1.read()
    f2 = open(pathway, "w+")
    input_text = content.split("\n")
    lines = [letter for letter in input_text]
    dic = {}
    fin = ""
    sorted_str = ""
    for line in lines:
        for char in line:
            if is_vowel(char):
                dic[char] = line.count(char)
        for key, value in sorted(dic.items()):
            sorted_str += key
        fin = line + sorted_str + "\n"
        dic = {}
        sorted_str = ""
        f2.write(fin)
    f2.close()


def is_consonant(i):
    return i not in ["a", "o", "e", "i", "u"]


def characters_info1(pathway):
    f1 = open("text2.txt", "r")
    content = f1.read()
    f1.close()
    s = ""
    lst_consonant = []
    f2 = open("text1.txt", "w+")
    input_text = content.split("\n")
    consonant = []
    for i in range(len(input_text[0])):
        letters = [el[i] for el in input_text]
        for letter in letters:
            if is_consonant(letter):
                if letter not in consonant:
                    consonant.append(letter)
        lst_consonant.append(sorted(consonant))
        consonant = []
    maximum = len(lst_consonant[0])
    for i in range(maximum):
        for el in lst_consonant:
            if i < len(el):
                s += el[i]
            else:
                s += " "
        s += "\n"
    f2.write(s)
    f2.close()
    return s


print(characters_info1("text1.txt"))
print(characters_info("text1.txt"))
