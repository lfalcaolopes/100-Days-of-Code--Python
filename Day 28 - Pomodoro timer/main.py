from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_TIMER = 25 * 60
LITTLE_BREAK = 5 * 60
BIG_BREAK = 20 * 60
reps = 0
check = ""
timer = None

# ==============================================================================================

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# ==============================================================================================


def countdown(counter):
    global timer

    minutes = str(math.floor(counter / 60))
    seconds = str(counter % 60)

    canvas.itemconfig(timer_text, text=f"{minutes.zfill(2)}:{seconds.zfill(2)}")
    if counter > 0:
        timer = window.after(1000, countdown, counter - 1)
    else:
        start_timer()


def start_timer():
    global reps, check
    reps += 1
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)

    if reps % 8 == 0:
        header.config(text="Break", fg=PINK)
        check += "✔"
        check_mark.config(text=check)
        countdown(BIG_BREAK)
    elif reps % 2 == 0:
        header.config(text="Break", fg=PINK)
        check += "✔"
        check_mark.config(text=check)
        countdown(LITTLE_BREAK)
    else:
        header.config(text="Work", fg=GREEN)
        countdown(WORK_TIMER)


def reset_timer():
    global reps, check, timer

    window.after_cancel(timer)

    reps = 0
    check = ""
    check_mark.config(text=check)
    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")

# ==============================================================================================


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Courier", 26, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

header = Label(text="Timer", bg=YELLOW, fg=GREEN, font=("Courier", 36, "bold"))
header.grid(row=0, column=1)

check_mark = Label(bg=YELLOW, fg=GREEN, font=("Courier", 12, "bold"))
check_mark.grid(row=3, column=1)

# ==============================================================================================

window.mainloop()
