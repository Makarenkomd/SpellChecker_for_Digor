import class_sort_digor
from class_sort_digor import dict_word

file = open("di_Di.dic", "r", encoding="UTF-8")
words = file.read().split('\n')
file.close()
print(len(words))
set_words = list(set(words))
print(len(set_words))
list_words = set([dict_word(word).word for word in set_words if word])
print(len(list_words))
list_words.sort()
#print(list_words)
file = open("unic_digor_words.txt", "w", encoding="UTF-8")
for word in list_words:
    file.write(word.word + "\n")
file.close()