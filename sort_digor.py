import class_sort_digor

file = open("Дигорон-Уруссаг.txt", "r", encoding="utf-8")

list_words = list()
word = ""
define = list()


for line in file.readlines():

    if line.startswith("\t"):
        define.append(line.rstrip())
    else:
        if word:
            list_words.append(dict_word(word, define))
        word = line.strip()
        define = list()
# создаем список экземпляров класса dict_word
list_words.append(dict_word(word, define))
file.close()
print(len(list_words))
print(list_words[26696])

sort_dict = sorted(list_words)

file = open("sort_words.txt", "w", encoding="utf-8")

for w in sort_dict:
    print(w.word, file=file)
    try:
        for line in w.define:
            print(line, file=file)
    except:
        print(w.word, type(w.define)) 
        print(f"|{w.define}|")

file.close()