THEME_COLOR = "#375362"
FONT=("arial",20,"italic")
from quiz_brain import QuizBrain
from tkinter import *


class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score=Label(text=f"Score: {self.quiz.score}",fg="white",font=("arial",10,"bold"),bg=THEME_COLOR,highlightthickness=0)
        self.score.grid(row=0,column=1)

        self.canvas=Canvas(height=250,width=300,bg="white")
        self.question_text=self.canvas.create_text(150,125,text=f"text",width=280,font=FONT,fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        true_image=PhotoImage(file="images/true.png")
        false_image=PhotoImage(file="images/false.png")

        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        self.false_button=Button(image=false_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2,column=1)


        self.get_nxt_question()

        self.window.mainloop()

    def get_nxt_question(self):
        self.window.after_cancel(self.get_nxt_question)
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))


    def give_feedback(self,response):
        if response==True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_nxt_question)

