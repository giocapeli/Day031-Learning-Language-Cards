import tkinter
import json
import random
import game_setup

BACKGROUND_COLOR = "#B1DDC6"
WORDS_DICT = {}
LANGUAGE = 'italian'

Card = game_setup.Card(LANGUAGE)

window = tkinter.Tk()
window.title("Language Card Game")
window.config(padx=50, pady=50, height=1000, width=1000, background=BACKGROUND_COLOR)
    

def show_back():
    card.create_image(400, 263, image=card_back_image)

def show_front():
    card.create_image(400, 263, image=card_front_image)
    
def get_random_word():
    with open(f"./language-files/{LANGUAGE}-english.json") as data_file:
        data = json.load(data_file)
        word = data[LANGUAGE][random.randint(0, len(data[LANGUAGE]) -1)]
    card.itemconfig(card_word, text=word["word"])
    card.itemconfig(card_title, text=LANGUAGE)

# --- Board
card = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file='./images/card_front.png')
card_back_image = tkinter.PhotoImage(file='./images/card_back.png')
card.create_image(400, 263, image=card_front_image)

# --- Text
card_title = card.create_text(400, 150, text="Language", font=("Ariel", 30, "italic"))
card_word = card.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))

card.grid(column=0, row=0, columnspan=2)
# --- Buttons
image_right = tkinter.PhotoImage(file='./images/right.png')
button_correct = tkinter.Button(image=image_right, highlightthickness=0)
button_correct.grid(column=0, row=1)

image_wrong = tkinter.PhotoImage(file='./images/wrong.png')
button_correct = tkinter.Button(image=image_wrong, highlightthickness=0, command=get_random_word)
button_correct.grid(column=1, row=1)

# ---
window.mainloop()