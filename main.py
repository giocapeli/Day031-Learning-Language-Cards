import tkinter
import game_setup
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
WORDS_DICT = {}
LANGUAGE = 'italian'
TRANSLATE = 'english'
TIMER = 3000

Card = game_setup.Card(LANGUAGE)

def show_back():
    card.itemconfig(card_word, text=Card.curr_word["translation"], fill="white")
    card.itemconfig(card_title, text=TRANSLATE, fill="white")
    card.itemconfig(card_background, image=card_back_image)
    button_incorrect.grid(column=1, row=1)
    button_correct.grid(column=0, row=1)

def show_front():
    global flip_timer
    window.after_cancel(flip_timer)
    
    card.itemconfig(card_word, text=Card.curr_word["word"], fill="black")
    card.itemconfig(card_title, text=LANGUAGE, fill="black")
    card.itemconfig(card_background, image=card_front_image)
    window.after(TIMER, show_back)
    
    button_correct.grid_forget()
    button_incorrect.grid_forget()
    
    flip_timer = window.after(TIMER, show_back)
   
def save_word_true():
    Card.save_word(True)
    show_front()

def save_word_false():
    Card.save_word(False)
    show_front()
    
def timer():
    global TIMER
    
def save_progress():
    Card.save_progress(LANGUAGE)
    if messagebox.askokcancel("Exit", "Do you want to close the programm?"):
        window.destroy()
    
window = tkinter.Tk()
window.title("Language Card Game")
window.config(padx=50, pady=50, height=1000, width=1000, background=BACKGROUND_COLOR)

flip_timer = window.after(TIMER, show_back)

# --- Board
card = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file='./images/card_front.png')
card_back_image = tkinter.PhotoImage(file='./images/card_back.png')
card_background = card.create_image(400, 263, image=card_front_image)

# --- Text
card_title = card.create_text(400, 150, text=LANGUAGE, font=("Ariel", 30, "italic"))
card_word = card.create_text(400, 263, text=Card.curr_word["word"], font=("Ariel", 50, "bold"))

card.grid(column=0, row=0, columnspan=2)
# --- Buttons
image_right = tkinter.PhotoImage(file='./images/right.png')
button_correct = tkinter.Button(image=image_right, highlightthickness=0, command=save_word_true)

image_wrong = tkinter.PhotoImage(file='./images/wrong.png')
button_incorrect = tkinter.Button(image=image_wrong, highlightthickness=0, command=save_word_false)

# ---
window.protocol("WM_DELETE_WINDOW", save_progress)
window.mainloop()
