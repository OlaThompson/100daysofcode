from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Sport Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="question", width=270,
                                                     fill=THEME_COLOR,  font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.label = Label(text="score : ",
                           font=("Helvetica", 14, "italic"), fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.button_1 = Button(image=false, command =self.false_pressed)
        self.button_2 = Button(image=true, command=self.true_pressed)
        self.button_2.grid(row=2, column=0)
        self.button_1.grid(row=2, column=1)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You have reached the end.\nYour score is {self.quiz.score}", fg="blue")
            self.button_2.config(state="disabled")
            self.button_1.config(state="disabled")

    def true_pressed(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, response):
        if response:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)

