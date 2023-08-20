from nltk.tokenize import sent_tokenize
import string
from string import punctuation

file_text = open("texts/text1.txt", "r", encoding="UTF-")
lines = file_text.read().split('\n')
file_text.close()

file = open("vowel_contraction.text", "w", encoding="UTF-8")
for line in lines:
    if line:
        for sent in sent_tokenize(line):
            if "’" in sent:
                print(sent, file=file)
                print(sent)
file.close()