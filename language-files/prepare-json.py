import json
import csv

language = 'dutch'
from_filename = "Dutch.csv"
cleaned_filename = f'./language-files/{language}-english.csv'
final_filename = f'./language-files/{language}-english.json'

def prepare_file():
    words_str = ''
    with open(from_filename, encoding='utf-8', newline='') as data_file:
        for i, word in enumerate(data_file):
            word = word.split()
            words_str = words_str + '\n' + word[0]
    with open(f"{language}-english.csv", "w", encoding='utf-8') as data_file:
        data_file.write(words_str)
        
def prepare_dict():
    new_dict = {language:[]}
    with open(cleaned_filename, encoding='utf-8', newline='') as data_file:
        for i, word in enumerate(data_file):
            word = word.split(',')
            new_dict[language].append({"word":word[0].strip(),
                                       "translation":word[1].strip()})
    with open(final_filename, "w", encoding='utf-8') as data_file:
        json.dump(new_dict, data_file, indent=4, ensure_ascii=False)
        data_file.close()


# Run prepare_file, paste the final file in an excel sheet and use the =GOOGLETRANSLATE(A1, "nl", "en") function to translate it, after, run function prepare_dict

# prepare_file()
prepare_dict()