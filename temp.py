file = open("error_words.txt", "r", encoding="UTF-8")
lines = file.readlines()

print(len(lines))
words = list(set(map(lambda x: x.strip().lower(),lines)))
print(len(words))

