from uniparser_ossetic import OsseticAnalyzer


analyzer = OsseticAnalyzer(mode='nodiacritics')
analyzer.load_grammar()
dict_word_forms = {}
words = ['ӕй', 'ӕрбадун', 'ӕриййафта', 'Ӕрфӕнбӕл', 'ӕвӕрӕнтӕ']
for word in words:
    analyses = analyzer.analyze_words(word)
    print(analyses[0].lemma)
    print(analyses[0].gramm)