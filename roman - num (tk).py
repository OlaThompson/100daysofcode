from tkinter import *
roman_key = {
    "m":1000,
    "d":500,
    "c":100,
    "l":50,
    "x":10,
    "v":5,
    "i":1
}


def switch():
    roman_letter = user_input_roman.get()
    value = roman_key[roman_letter[-1]]
    for index in range(len(roman_letter) - 2, -1, -1):
        current_value = roman_key[roman_letter[index]]
        next_value = roman_key[roman_letter[index + 1]]
        if current_value < next_value:
            value -= current_value
        else:
            value += current_value
    conversion.config(text= value)


window = Tk()
window.title("Roman numerals // numerals")
window.config(padx=50, pady=90, bg="brown")

roman = Label(fg="white", bg="brown", text="Roman numeral:", highlightthickness=0, font=("Courier", 20, "bold"))
roman.grid(column= 0, row=0)
numeral = Label(fg="white", bg="brown", text="Numeral:", highlightthickness=0, font=("Courier", 20, "bold"))
numeral.grid(column= 0, row=2)

conversion = Label(text=0, font=("Arial", 30, "bold"))
conversion.grid(column =1, row=2)

user_input_roman = Entry(width=10)
user_input_roman.grid(column= 1, row=0)
print(user_input_roman.get())

convert = Button(text="CONVERT", bd=10, bg="white", fg= "brown", command = switch)
convert.grid(column= 1, row=1)


window.mainloop()