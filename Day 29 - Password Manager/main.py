from tkinter import *
from tkinter import messagebox
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generator():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(web_input.get()) == 0 or len(password_input.get()) == 0 or len(email_input.get()) == 0:
        messagebox.showinfo(title="Empty entries", message="Please don't leave any fields empty!")
    elif messagebox.askokcancel(title=web_input.get(), message=f"Email: {email_input.get()}\n"
                                                              f"Password: {password_input.get()}\n\nIs it ok to save?"):
        with open("Passwords.txt", "a") as data:
            data.write(f"{web_input.get()} | {email_input.get()} | {password_input.get()} \n")
        web_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

web_text = Label(text="Website:")
web_text.grid(row=1, column=0)

web_input = Entry()
web_input.focus()
web_input.grid(row=1, column=1, columnspan=2, sticky='EW')

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)

email_input = Entry()
email_input.grid(row=2, column=1, columnspan=2, sticky='EW')

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password_input = Entry()
password_input.grid(row=3, column=1, sticky='EW', padx=(0, 5))

generate_button = Button(text="Generate Password", command=generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')

window.mainloop()