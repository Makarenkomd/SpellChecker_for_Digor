import json


file = open("forms_digor_forms.txt", "r", encoding="UTF8")

lines = file.readlines()
dict_forms = dict()
print(lines[:10])
k = 0
for line in lines:
    if '\t' in line:
        dict_forms[normal].add(line.strip().lower())
    else:
        k += 1
        normal = line.strip().lower()
        if normal not in dict_forms:
            dict_forms[normal] = set()
print(dict_forms)
print(k, len(dict_forms))
file.close()
for key in dict_forms:
    dict_forms[key] = list(dict_forms[key])
file_correct = open("digor_forms.txt", "w", encoding="utf-8")
json.dump(dict_forms, file_correct, ensure_ascii=False)
file_correct.close()
