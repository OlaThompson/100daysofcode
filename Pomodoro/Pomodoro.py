from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN =10
rep = 0
timer = None

def force_stop():
    window.after_cancel(timer)
    canvas.item_config(timer_text, text="00:00")
    label.config(text = "Timer")
    global rep
    rep= 0
    label2.confid(text="")


def resetting():
    global rep
    rep+=1
    WORK_SEC = WORK_MIN * 60
    SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
    LONG_BREAK_SEC = LONG_BREAK_MIN * 60
    if rep%8 == 0:
        count_down(LONG_BREAK_SEC)
        label.config(fg=GREEN, bg=PINK, text="      REST\nYOU DESERVE IT", highlightthickness=0, font=(FONT_NAME, 40,
                                                                                                       "bold"))
    elif rep%2 == 0:
        label.config(fg=YELLOW, bg=PINK, text="SHORT BREAK", highlightthickness=0, font=(FONT_NAME, 40, "bold"))
        count_down(SHORT_BREAK_SEC)
    else:
        label.config(fg=RED, bg=PINK, text="STUDY", highlightthickness=0, font=(FONT_NAME, 40, "bold"))
        count_down(WORK_SEC)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        resetting()
        marks = ""
        sessions = math.floor(rep/2)
        for complete in range (sessions):
            marks += "🙃"
        label2.config(text= marks)


window = Tk()
window.title("POMODORO")
window.config(padx=90, pady=70, bg=PINK)

label = Label(fg=GREEN, bg=PINK, text="Timer", relief="groove", highlightthickness=0, font=(FONT_NAME, 40, "bold"))
label.grid(column=1, row=0)

label2 = Label(fg=GREEN, bg=PINK, text="", highlightthickness=0, font=(FONT_NAME, 10, "bold"))
label2.grid(column=1, row=3)

t_image = PhotoImage(file="tomato.png")
canvas = Canvas(bg=PINK, width=200, height=224, highlightthickness=0)
canvas.create_image(100, 100, image=t_image)
timer_text = canvas.create_text(100, 115, text="00:00", fill=GREEN, font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", highlightthickness=0, bd=5, bg=GREEN, command=resetting)
start_button.grid(column=0, row=2)
reset_button = Button(text="RESET", highlightthickness=0, bd=5, bg=RED, command = force_stop)
reset_button.grid(column=2, row=2)


window.mainloop()
