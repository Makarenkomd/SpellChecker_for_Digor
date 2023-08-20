from nltk.tokenize import TreebankWordTokenizer
import string
from string import punctuation

file = open("di_Di.dic", "w", encoding="UTF-8")
file_text = open("texts/НАРТЫ.txt", "r", encoding="UTF-")
lines = file_text.read().split('\n')
file_text.close()
quotation = "«»—=" +'“”'
punctuation += "– …"
punctuation += quotation
print(len(punctuation))
punctuation = punctuation.replace('’','')
print(len(punctuation), punctuation)
print("строк -", len(lines))
count_words = 0
dict_replace = str.maketrans(quotation, ' '*len(quotation))
for line in lines:
    if line:
        words = TreebankWordTokenizer().tokenize(line)
        if '’' in words:
            print(line)
        temp = len(words)
        for i in range(len(words)):
            words[i] = words[i].translate(dict_replace).rstrip(punctuation)
        #error_words = list(filter(lambda w: w in punctuation, words))
        words = list(filter(lambda w: w not in punctuation, words))
        #if temp != len(words):
        #    print(temp, len(words))
        #    print(error_words)
        count_words += len(words)
        file.write("\n".join(words) + "\n")
file.close()
#print("слов -", count_words)
