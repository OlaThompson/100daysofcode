import tkinter

def convert():
    number_miles = user_input.get()
    number_km = float(number_miles) * 1.60934
    result.config(text = round(number_km))



window = tkinter.Tk()
window.title("mile to Km converter")
window.minsize(150,150)
window.config(padx=20,pady=20)

miles = tkinter.Label(text="   miles", font=("Arial", 24, "bold"))
miles.grid(row=0, column=2)
km = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
km.grid(row=1, column=2)
result = tkinter.Label(text=0, font=("Arial", 24, "bold"))
result.grid(row=1, column=1)
equal_line = tkinter.Label(text="is equal to", font=("Arial", 10,))
equal_line.grid(row=1, column=0)

user_input = tkinter.Entry(width=8)
user_input.grid(row=0, column=1)
print(user_input.get())

calculate_button = tkinter.Button(text="Convert", command=convert)
calculate_button.grid(row=2, column=1)

window.mainloop()