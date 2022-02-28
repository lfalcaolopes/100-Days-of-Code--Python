from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.right_image = PhotoImage(file="./images/true.png")
        self.wrong_image = PhotoImage(file="./images/false.png")

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_question = self.canvas.create_text(150, 125, width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_button = Button(image=self.right_image, highlightthickness=0, bd=0, command=self.right_answer)
        self.right_button.grid(row=3, column=1)

        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, bd=0, command=self.wrong_answer)
        self.wrong_button.grid(row=3, column=0)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_question, text=question)
        else:
            self.canvas.itemconfig(self.canvas_question, text="The quiz is over")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_answer(self):
        is_right = self.quiz.check_answer("True")

        self.give_feedback(is_right)

        player_score = self.quiz.score
        self.score.config(text=f"Score: {player_score}")

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")

        self.give_feedback(is_right)

        player_score = self.quiz.score
        self.score.config(text=f"Score: {player_score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)

