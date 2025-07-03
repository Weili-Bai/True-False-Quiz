from tkinter import *
import html

import data

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class QuizInterface:
    def __init__(self):
        self.score = 0
        self.correct_answer = ""
        self.question_number = 0
        self.is_started = False
        self.question_bank = data.question_data
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        check_image = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.check_button)
        self.check_button.grid(row=2, column=0)
        cross_image = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.cross_button)
        self.cross_button.grid(row=2, column=1)

        self.question_text = self.canvas.create_text(150, 125, fill="black", font=FONT, width=280,
                                                     text="Press any button to start")
        self.score_text = Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        self.window.mainloop()

    def get_next_q_a(self):
        self.canvas.config(bg="white")
        if self.question_number < len(self.question_bank):
            temp = self.question_bank[self.question_number]
            question = html.unescape(temp['question'])
            self.correct_answer = temp['correct_answer']
            self.canvas.itemconfig(self.question_text, text=f"Q{self.question_number + 1} {question}")
        else:
            self.canvas.itemconfig(self.question_text, text=f"All questions finished. Your final score: {self.score}")
            self.correct_answer = None

    def check_button(self):
        self.get_next_q_a()
        if not self.is_started:
            self.is_started = True
            return
        if self.correct_answer is not None:
            if self.correct_answer == "True":
                self.score += 1
                self.score_text.config(text=f"Score: {self.score}")
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.question_number += 1
            self.window.after(3000, self.get_next_q_a)

    def cross_button(self):
        self.get_next_q_a()
        if not self.is_started:
            self.is_started = True
            return
        if self.correct_answer is not None:
            if self.correct_answer == "False":
                self.score += 1
                self.score_text.config(text=f"Score: {self.score}")
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.question_number += 1
            self.window.after(3000, self.get_next_q_a)
