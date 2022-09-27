from tkinter import *
from tkinter import ttk

counter = 0
initial_text = None
initial_morse = None


def text_converter(var, index, mode):
    global counter, initial_text, initial_morse

    text_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
                     'D': '-..', 'E': '.', 'F': '..-.',
                     'G': '--.', 'H': '....', 'I': '..',
                     'J': '.---', 'K': '-.-', 'L': '.-..',
                     'M': '--', 'N': '-.', 'O': '---',
                     'P': '.--.', 'Q': '--.-', 'R': '.-.',
                     'S': '...', 'T': '-', 'U': '..-',
                     'V': '...-', 'W': '.--', 'X': '-..-',
                     'Y': '-.--', 'Z': '--..',

                     '.': '.-.-.-', ',': '--..--', ' ': '/',

                     '0': '-----', '1': '.----', '2': '..---',
                     '3': '...--', '4': '....-', '5': '.....',
                     '6': '-....', '7': '--...', '8': '---..',
                     '9': '----.'
                     }

    try:
        text = text_var.get()
        morse_result = []

        morse_var.trace_remove(*morse_var.trace_info()[0])

        if counter == 0:
            initial_text = text_var.get()

            counter += 1

        if text != initial_text:
            for letters in text.upper():
                morse_result.append(text_to_morse[letters])

            morse_entry.delete(0, END)
            morse_entry.insert(0, " ".join(morse_result))

    except KeyError:
        pass

    finally:
        initial_text = text_var.get()
        morse_var.trace_add('write', morse_converter)


def morse_converter(var, index, mode):
    global counter, initial_text, initial_morse

    text_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
                     'D': '-..', 'E': '.', 'F': '..-.',
                     'G': '--.', 'H': '....', 'I': '..',
                     'J': '.---', 'K': '-.-', 'L': '.-..',
                     'M': '--', 'N': '-.', 'O': '---',
                     'P': '.--.', 'Q': '--.-', 'R': '.-.',
                     'S': '...', 'T': '-', 'U': '..-',
                     'V': '...-', 'W': '.--', 'X': '-..-',
                     'Y': '-.--', 'Z': '--..',

                     '.': '.-.-.-', ',': '--..--', ' ': '/',

                     '0': '-----', '1': '.----', '2': '..---',
                     '3': '...--', '4': '....-', '5': '.....',
                     '6': '-....', '7': '--...', '8': '---..',
                     '9': '----.'
                     }

    morse_to_text = {v: k for k, v in text_to_morse.items()}

    try:
        text_var.trace_remove(*text_var.trace_info()[0])

        morse = morse_var.get()
        text_result = []

        if counter == 0:
            initial_morse = morse_var.get()

            counter += 1

        if morse != initial_morse:
            morse = morse.split()

            for codes in morse:
                text_result.append(morse_to_text[codes].lower())

            text_entry.delete(0, END)
            text_entry.insert(0, "".join(text_result))

    except KeyError:
        pass

    finally:
        text_var.trace_add('write', text_converter)
        initial_morse = morse_var.get()


root = Tk()
root.title("Text to Morse Converter")
text_var = StringVar()
morse_var = StringVar()

text_var.trace_add('write', text_converter)
morse_var.trace_add('write', morse_converter)

frame = ttk.Frame(root, padding=20)

frame.grid()

text_title = ttk.Label(frame, text="Text", font="Times 20 bold")
text_title.grid(column=0, row=0)

text_entry = ttk.Entry(frame, textvariable=text_var)
text_entry.grid(column=0, row=1, ipadx=50, ipady=25, padx=10, pady=10)

morse_title = ttk.Label(frame, text="Morse", font="Times 20 bold")
morse_title.grid(column=1, row=0)

morse_entry = ttk.Entry(frame, textvariable=morse_var)
morse_entry.grid(column=1, row=1, ipadx=50, ipady=25, padx=10, pady=10)

root.mainloop()
