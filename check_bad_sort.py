from class_sort_digor import word_code_symbols, dict_word

words = ["ӕрбадун",'ӕвӕрӕнтӕ', 'ӕрийафта', 'Ӕрфӕнбӕл']
list_words_for_sort = []
for word in words:
    print(word_code_symbols(word))
    list_words_for_sort.append(dict_word(word))
list_words_for_sort.sort()
print(list_words_for_sort)