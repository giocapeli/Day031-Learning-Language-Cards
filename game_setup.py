import json
import random

class Card():
    
    def __init__(self, language):
        self.word_dict = []
        self.words_right = []
        self.words_wrong = []
        self.curr_word = {}
        self.loaded_data = {}
        
        self.get_dict(language)
        self.load_data(language)
        self.get_new_word()

    def get_dict(self, language):
        try:
            with open(f"./language-files/{language}-english.json", encoding='utf-8') as data_file:
                data = json.load(data_file)
                self.word_dict = data[language]
        except FileNotFoundError:
            print("No word database. Please Create dictionary first.")
    
    def load_data(self, language):
        try:
            with open(f"./language-files/{language}-english-saved.json", "r", encoding='utf-8') as data_file:
                data = json.load(data_file)
                self.words_wrong = data["incorrect"]
                self.words_right = data["correct"]
                data_file.close()
        except FileNotFoundError:
            pass
            
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
        
    def save_progress(self, language):
        self.loaded_data.update(
            {
                "correct": self.words_right,
                "incorrect": self.words_wrong
            }
        )
        with open(f"./language-files/{language}-english-saved.json", "w", encoding='utf-8') as data_file:
            json.dump(self.loaded_data, data_file, indent=4, ensure_ascii=False)
            data_file.close()