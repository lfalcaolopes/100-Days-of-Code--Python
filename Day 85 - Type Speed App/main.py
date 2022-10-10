from tkinter import *
from tkinter import ttk
import pandas as pd
from random import choice

df = pd.read_csv('most-common-words-1k.csv')

words = list(df["Word"])
in_game = []
entry_words = []
score = 0
start_timer = 30

for i in range(50):
    in_game.append(choice(words))

# ================================================================================================= #


def func(var, index, mode):
    global score
    if entry.get()[-1] == " ":
        entry_words.append(entry.get().split())
        answer_box.delete(0, END)
        if str(entry_words[-1][0]) == in_game[len(entry_words) - 1]:
            score += 1
            scoreboard.config(text=f"Score: {score}")
        if len(entry_words) % 5 == 0 and len(entry_words) > 6:
            word_var = int(len(entry_words) / 5) - 1

            row1.config(text=" ".join(in_game[5 * word_var:5 * (word_var+1)]))
            row2.config(text=" ".join(in_game[5 * (word_var+1):5 * (word_var+2)]))
            row3.config(text=" ".join(in_game[5 * (word_var+2):5 * (word_var+3)]))


def countdown(counter):
    seconds = str(counter % 60)

    timer_label.config(text=f"{seconds.zfill(2)}s")
    if counter > 0:
        root.after(1000, countdown, counter - 1)
    else:
        final_score.config(text=f"{score*2} WPM")
        result_screen.tkraise(aboveThis=main_screen_text)


def try_again():
    global score, in_game, entry_words
    score = 0
    in_game = []
    entry_words = []

    for _ in range(50):
        in_game.append(choice(words))

    # main_screen_text.grid(column=0, row=0, sticky="nsew")
    main_screen_text.tkraise(aboveThis=result_screen)

    countdown(30)
    answer_box.delete(0, END)
    scoreboard.config(text=f"Score: {score}")

    row1.config(text=" ".join(in_game[:5]))
    row2.config(text=" ".join(in_game[5:10]))
    row3.config(text=" ".join(in_game[10:15]))


# ================================================================================================= #

root = Tk()
root.title("Typing Speed")
entry = StringVar()

main_screen_text = ttk.Frame(root, padding=50)
result_screen = ttk.Frame(root, padding=50)


main_screen_text.grid(column=0, row=0)
result_screen.grid(column=0, row=0, sticky="nsew")

main_screen_text.tkraise()

entry.trace_add('write', func)

# ================================================================================================= #

timer_label = ttk.Label(main_screen_text, text=f"", font="Times 16 bold")
timer_label.grid(column=0, row=0, pady=10)

scoreboard = ttk.Label(main_screen_text, text=f"Score: {score}", font="Times 16 bold")
scoreboard.grid(column=3, row=0, pady=10)

row1 = ttk.Label(main_screen_text, text=" ".join(in_game[:5]), font="Times 16 bold")
row1.grid(column=0, row=1, columnspan=4)

row2 = ttk.Label(main_screen_text, text=" ".join(in_game[5:10]), font="Times 16 bold")
row2.grid(column=0, row=2, columnspan=4)

row3 = ttk.Label(main_screen_text, text=" ".join(in_game[10:15]), font="Times 16 bold")
row3.grid(column=0, row=3, columnspan=4)

answer_box = ttk.Entry(main_screen_text, textvariable=entry)
answer_box.grid(column=0, row=4, columnspan=4, pady=20, ipadx=10, ipady=5)

countdown(30)

# ================================================================================================= #

ttk.Label(result_screen, text=f"Your Score:", font="Times 16 bold").pack()
final_score = ttk.Label(result_screen, text=f"{score*2} WPM", font="Times 16 bold")
final_score.pack(pady=30)
ttk.Button(result_screen, text=f"Try again", command=try_again).pack()


root.mainloop()
