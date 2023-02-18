import json

language = 'italian'
from_filename = "italian.csv"

def first_load():
    words_list = []
    new_dict = {language:[]}
    with open(from_filename, encoding='utf-8', newline='') as data_file:
        for i, word in enumerate(data_file):
            word = word.split()
            new_dict[language].append(word[0])
    with open(f"{language}.json", "w", encoding='utf-8') as data_file:
        json.dump(new_dict, data_file, indent=4, ensure_ascii=False)
        data_file.close()

first_load()