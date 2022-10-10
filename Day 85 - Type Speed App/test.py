from tkinter import *
from tkinter import messagebox
from random import shuffle
import pandas as pd
THEME_COLOR = "#375362"
TIME_REMAIN = 60


class Interface:
    def __init__(self):
        self.time_remain = TIME_REMAIN
        self.best = 0
        self.typed_words = []
        self.start = False
        self.row = 0
        self.timer = None
        self.window = Tk()
        # self.window.eval('tk::PlaceWindow . center')
        self.window.title("A Typing Speed Test!")
        self.window.config(padx=20, bg=THEME_COLOR)
        self.user_typed = StringVar()
        self.words = list(pd.read_csv('most-common-words-1k.csv')["Word"])
        shuffle(self.words)
        self.words = '\n'.join(self.words)
        # ===== Status Frame ===== #
        self.status_frame = LabelFrame(self.window, text="Status", fg="white", bg=THEME_COLOR, height=200)
        self.status_frame.config(padx=20, pady=20, bg=THEME_COLOR)
        self.status_frame.grid(row=0, column=0, padx=25, pady=10)

        self.label_best = Label(self.status_frame, text="Your best: ",
                                width=10, height=1, fg="white", bg=THEME_COLOR)
        self.label_best.grid(row=0, column=0, padx=5, pady=5)

        self.label_best_v = Label(self.status_frame, text="", width=10)
        self.label_best_v.grid(row=0, column=1, sticky="W", padx=(5, 35), pady=5)

        self.label_CPM = Label(self.status_frame, text="Corrected CPM: ",
                               anchor="w", width=15, height=1, fg="white", bg=THEME_COLOR)
        self.label_CPM.grid(row=0, column=2, sticky="W", padx=5, pady=5)

        self.label_CPM_v = Label(self.status_frame, text="", width=10)
        self.label_CPM_v.grid(row=0, column=3, sticky="W", padx=5, pady=5)

        self.label_WPM = Label(self.status_frame, text="WPM: ",
                               anchor="w", width=7, height=1, fg="white", bg=THEME_COLOR)
        self.label_WPM.grid(row=0, column=4, sticky="W", padx=5, pady=5)

        self.label_WPM_v = Label(self.status_frame, text="", width=10)
        self.label_WPM_v.grid(row=0, column=5, sticky="W", padx=5, pady=5)

        # ===== Main Frame ===== #
        self.main_frame = LabelFrame(self.window, text="Words", fg="white", bg=THEME_COLOR, height=300)
        self.main_frame.config(padx=20, pady=20, bg=THEME_COLOR)
        self.main_frame.grid(row=1, column=0, padx=25, pady=10, sticky='WENS')
        self.main_frame.grid_propagate(False)

        self.label_time = Label(self.main_frame, text="Time left: ",
                                anchor="w", width=10, height=1, fg="white", bg=THEME_COLOR)
        self.label_time.grid(row=0, column=0, sticky="W", padx=5, pady=(0, 5))

        self.label_time_v = Label(self.main_frame, text="", width=10)
        self.label_time_v.grid(row=0, column=0, sticky="W", padx=(80, 0), pady=(0, 5))

        self.text_words = Text(self.main_frame, width=48, height=9, font=('Arial', 14))
        self.text_words.grid(row=1, column=0, padx=(5, 0), pady=5, sticky='NWS')
        self.text_words.insert(1.0, self.words)
        self.text_words.tag_config("correct", background="green")
        self.text_words.tag_config("wrong", foreground="orange")

        self.vsb = Scrollbar(self.main_frame, orient="vertical", command=self.text_words.yview)
        self.text_words.configure(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=1, column=1, padx=(0, 50), pady=5, sticky='WNS')

        # ===== Typing Frame ===== #
        self.typing_frame = LabelFrame(self.window, text="Typing", fg="white", bg=THEME_COLOR, height=80)
        self.typing_frame.config(padx=20, pady=20, bg=THEME_COLOR)
        self.typing_frame.grid(row=2, column=0, padx=25, pady=10, sticky='WENS')
        self.typing_frame.grid_propagate(False)
        detect_text_change_wrapper = (self.window.register(self.detect_text_change), '%S')

        self.entry_typing = Entry(self.typing_frame, width=50, textvariable=self.user_typed, font=('Arial', 14),
                                  validate='key', validatecommand=detect_text_change_wrapper)
        self.entry_typing.grid(row=0, column=0, padx=5, pady=0, sticky='NEWS')

        self.entry_typing.bind('<Return>', self.start_test)

        self.words = self.words.split('\n')
        self.entry_typing.focus()
        self.window.mainloop()

    def detect_text_change(self, key):
        if key == ' ':
            return False
        return True

    def del_word(self, event):
        typing = self.entry_typing.get()
        print(f'press back, typed "{typing}"')
        if typing == '':
            if self.row > 0:
                self.text_words.delete(f"{self.row+1}.{len(self.words[self.row]) }", f'{self.row+1}.end')
                self.text_words.tag_remove("wrong", f"{self.row+1}.{0}", f"{self.row+1}.end")
                self.row -= 1
                self.text_words.tag_remove("correct", f"{self.row+1}.{0}", f"{self.row+1}.end")
                self.text_words.insert(f"{self.row + 1}.{len(self.words[self.row])}", '←')
                self.entry_typing.delete(0, 'end')
                self.text_words.see(f"{self.row}.{len(self.words[self.row])}")

    def send_word(self, event):
        print('press space')
        typing = self.entry_typing.get()
        print(f'打字:{typing}')
        print(f"::: {self.words[self.row]} and {typing} ::: {self.words[self.row] == typing}")
        if self.words[self.row] == typing:
            self.text_words.tag_add("correct", f"{self.row+1}.0", f"{self.row+1}.end")
            self.text_words.tag_remove("wrong", f"{self.row+1}.0", f"{self.row+1}.end")
        else:
            min_c = min(len(self.words[self.row]), len(typing))
            for i in range(min_c):
                if typing[i] != self.words[self.row][i]:
                    self.text_words.tag_add("wrong", f"{self.row+1}.{i}")
                else:
                    self.text_words.tag_remove("wrong", f"{self.row+1}.{i}")
            if len(self.words[self.row]) > len(typing):
                self.text_words.tag_add("wrong", f"{self.row+1}.{len(typing)}", f"{self.row+1}.end")

        self.text_words.delete(f"{self.row+1 }.{len(self.words[self.row])}", f'{self.row+1 }.end')
        self.row += 1
        self.text_words.insert(f"{self.row+1}.{len(self.words[self.row])}", '←')
        self.text_words.see(f"{self.row+4}.{len(self.words[self.row])}")

        self.typed_words.append(typing)
        self.entry_typing.delete(0, 'end')

    def countdown(self, last_secs):
        self.label_time_v.config(text=last_secs)
        if last_secs > 0:
            self.timer = self.window.after(1000, self.countdown, last_secs - 1)
        else:
            self.window.after_cancel(self.timer)
            self.entry_typing.unbind('<Return>')
            self.entry_typing.unbind('<BackSpace>')
            self.calc_pm()

    def start_test(self, event):
        self.countdown(self.time_remain)

        self.entry_typing.bind('<BackSpace>', self.del_word)
        print('press Enter')
        print(f"{self.row}.{len(self.words[self.row])}")

        self.text_words.insert(f"{self.row+1}.{len(self.words[self.row])}", '←')
        self.entry_typing.unbind('<Return>')
        self.entry_typing.bind('<Return>', self.send_word)
        pass

    def calc_pm(self):
        correct_char = 0
        correct_word = 0
        for i, words in enumerate(self.typed_words):
            if words == self.words[i]:
                correct_word += 1
                correct_char += len(self.words[i])
            else:
                min_c = min(len(self.words[i]), len(words))
                for j in range(min_c):
                    if words[j] == self.words[i][j]:
                        correct_char += 1

        self.label_CPM_v.config(text=correct_char)
        self.label_WPM_v.config(text=correct_word)
        messagebox.showinfo(title='Game over!', message=f"CPM: {correct_char}\nWPM: {correct_word}")
        pass


a = Interface()
