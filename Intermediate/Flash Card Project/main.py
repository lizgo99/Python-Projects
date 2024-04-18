from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
to_learn = {}

try: 
    data = pandas.read_csv("Intermediate/Flash Card Project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Intermediate/Flash Card Project/data/german_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def know():
    to_learn.remove(random_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Intermediate/Flash Card Project/data/words_to_learn.csv", index=False)
    new_card()
    

def new_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    print(random_word)
    canvas.itemconfigure(title_text, text="German", fill="black")
    canvas.itemconfigure(word_text, text=random_word['word'], fill="black")
    canvas.itemconfigure(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfigure(title_text, text="English", fill="white")
    canvas.itemconfigure(word_text, text=random_word['translation'], fill="white")
    canvas.itemconfigure(canvas_img, image=card_back_img)
    
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="Intermediate/Flash Card Project/images/card_front.png")
card_back_img = PhotoImage(file="Intermediate/Flash Card Project/images/card_back.png")
canvas_img = canvas.create_image(400,263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill='black')
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


right_img = PhotoImage(file="Intermediate/Flash Card Project/images/right.png")
right_button = Button(image=right_img, command=know, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="Intermediate/Flash Card Project/images/wrong.png")
wrong_button = Button(image=wrong_img, command= new_card, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

new_card()

window.mainloop()


