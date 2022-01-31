from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=20, bg="white")


def conversion():
    result.config(text=str(round(float(mile.get())*1.609, 2)))


text = Label(text="is equal to ", bg="white")
text.grid(column=0, row=2)

result = Label(text="0", bg="white")
result.grid(column=1, row=2)
result.config(padx=30, pady=10)

km_symbol = Label(text="Km", bg="white")
km_symbol.grid(column=2, row=2)

mile = Entry(width=10)
mile.grid(column=1, row=1)

mile_symbol = Label(text="Miles", bg="white")
mile_symbol.grid(column=2, row=1)

calculate = Button(text="Calculate", command=conversion)
calculate.grid(column=1, row=3)

window.mainloop()
