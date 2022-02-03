import tkinter
import pandas
from tkinter import messagebox
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
RIGHT_SCORE = 0
WRONG_SCORE = 0


# ---------------------------- Flash Cards ------------------------------- #
en_br_pandas = pandas.read_csv("./data/en_br.csv")
en_br_dict = en_br_pandas.to_dict()

languages = [key for key in en_br_dict]
studying_lang = languages[0]
local_lang = languages[1]

index_list = [index for index in range(len(en_br_dict[studying_lang]))]
words_to_study = {studying_lang: [], local_lang: []}

NEW_INDEX = None


def front_flash_card():
    new_word = en_br_dict[studying_lang][NEW_INDEX].capitalize()

    canvas.itemconfig(card_image, image=FRONT_CARD)
    canvas.itemconfig(title, text=studying_lang.title(), fill="black")
    canvas.itemconfig(word, text=new_word, fill="black")


def back_flash_card():
    new_word = en_br_dict[local_lang][NEW_INDEX].capitalize()

    canvas.itemconfig(card_image, image=BACK_CARD)
    canvas.itemconfig(title, text=local_lang.title(), fill="white")
    canvas.itemconfig(word, text=new_word, fill="white")


def new_flash_card():
    global NEW_INDEX, flip_timer
    window.after_cancel(flip_timer)

    NEW_INDEX = choice(index_list)
    front_flash_card()

    flip_timer = window.after(3000, back_flash_card)


# ---------------------------- Score System ------------------------------- #


def right_answer():
    global RIGHT_SCORE

    RIGHT_SCORE += 1
    index_list.remove(NEW_INDEX)

    new_flash_card()


def wrong_answer():
    global WRONG_SCORE, words_to_study

    WRONG_SCORE += 1
    words_to_study[studying_lang].append(en_br_dict[studying_lang][NEW_INDEX])
    words_to_study[local_lang].append(en_br_dict[local_lang][NEW_INDEX])

    data = pandas.DataFrame(words_to_study)
    data.to_csv("data/words_to_learn.csv", index=False)

    new_flash_card()


def show_score():
    global RIGHT_SCORE, WRONG_SCORE

    messagebox.showinfo(title="Score", message=f"Your score so far:\n\nRight: {RIGHT_SCORE}\nWrong: {WRONG_SCORE}")


# ---------------------------- UI Setup ------------------------------- #

window = tkinter.Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

WRONG_IMAGE = tkinter.PhotoImage(file="./images/wrong.png")
RIGHT_IMAGE = tkinter.PhotoImage(file="./images/right.png")
FRONT_CARD = tkinter.PhotoImage(file="./images/card_front.png")
BACK_CARD = tkinter.PhotoImage(file="./images/card_back.png")

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=FRONT_CARD)
title = canvas.create_text(400, 150, font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = tkinter.Button(image=WRONG_IMAGE, highlightthickness=0, bd=0, command=wrong_answer)
wrong_button.grid(row=1, column=0)

right_button = tkinter.Button(image=RIGHT_IMAGE, highlightthickness=0, bd=0, command=right_answer)
right_button.grid(row=1, column=1)

score_button = tkinter.Button(text="Score", bg=BACKGROUND_COLOR, font=("Arial", 26, "bold"), command=show_score)
score_button.grid(row=2, column=0, columnspan=2)

# ---------------------------- Calling Functions ------------------------------- #

flip_timer = window.after(1, new_flash_card)
window.mainloop()
