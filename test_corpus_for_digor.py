# нужна библиотека xlxml
import lingcorpora

corp = lingcorpora.Corpus('dig')
words = ['адтӕ']

for ind, word in enumerate(words):
    results = corp.search(word, n_results=1, get_analysis = True)
    target = results[0][0]
    if target != False:
        for tok in target.analysis:
            key = (tok['lemma'], tok['PoS'])
            print(key)
