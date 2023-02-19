import json
import random

class Card():
    
    def __init__(self, language):
        self.word_dict = []
        self.words_right = []
        self.words_wrong = []
        self.curr_word = {}
        
        self.get_dict(language)
        self.get_new_word()

    def get_dict(self, language):
        with open(f"./language-files/{language}-english.json", encoding='utf-8') as data_file:
            data = json.load(data_file)
            self.word_dict = data[language]
            
    def get_new_word(self):
        if len(self.word_dict) >= 20:
            i = random.randint(0, 19) #stick in the first 20 records
        else:
            i = random.randint(0, len(self.word_dict) - 1) #use the length
        self.curr_word = self.word_dict[i]
        self.word_dict.pop(i)
        print(self.curr_word)
        
    def save_word(self, is_right):
        if is_right:
            self.words_right.append(self.curr_word)
            print(self.words_right)
        else:
            self.words_wrong.append(self.curr_word)
            print(self.words_wrong)
        self.get_new_word()
            