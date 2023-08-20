# нужна библиотека xlxml
import lingcorpora

def save_to_file():
    file = open("forms_digor_forms.txt", "a", encoding="UTF8")
    for key in dict_words_and_pos:
        print(*key, file=file)
        for el in dict_words_and_pos[key]:
            print('\t', el, file=file)
    file.close()
    file_error = open("error_words.txt", "a", encoding="UTF-8")
    for word in list_error:
        print(word, file=file_error)
    file_error.close()

corp = lingcorpora.Corpus('dig')

file = open("target/unic_digor_words_hand_edit.txt", "r", encoding="UTF-8")
words = file.read().split('\n')
file.close()
#words =
#print(words)
dict_words_and_pos = dict()
list_error = []
for ind, word in enumerate(words[19799:]):
    if ind % 100 == 0:
        save_to_file()
    results = corp.search(word, n_results=1, get_analysis = True)
    target = results[0][0]
    if target != False:
        for tok in target.analysis:
            key = (tok['lemma'], tok['PoS'])
            #print(key)
            if key not in dict_words_and_pos:
                dict_words_and_pos[key] = []
            dict_words_and_pos[key].append(word)
    else:
        print(ind, "bad target", word)
        list_error.append(word)
save_to_file()
