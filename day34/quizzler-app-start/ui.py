from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR
                           , padx= 20
                           , pady = 20
                        )
        self.window.minsize(width=350, height=400)
        self.main_canvas()
        self.score()
        self.buttons()
        self.layout()
        self.get_next_question()
        self.window.mainloop()

    def main_canvas(self):
        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(145, 110
                            , text="Question"
                            , font=("Arial", 17, "italic")
                            , fill=THEME_COLOR
                            , width= 280
                        )

    def score(self):
        self.score_label = Label(text=f"Score: {self.quiz.score}")
        self.score_label.config(bg=THEME_COLOR, fg="white")

    def buttons(self):
        self.yes_img = PhotoImage(file=r"day34\quizzler-app-start\images\true.png")
        self.no_img = PhotoImage(file=r"day34\quizzler-app-start\images\false.png")
        self.yes_button = Button(image=self.yes_img, highlightthickness=0, command=self.yes_answer)
        self.no_button = Button(image=self.no_img, highlightthickness=0, command=self.no_answer)

    def layout(self):
        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.yes_button.grid(column=0, row=2)
        self.no_button.grid(column=1, row=2)

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")

    def yes_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.get_next_question()
            
    
    def no_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.get_next_question()
        

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.update()
        self.window.after(1000, self.canvas.config(bg="white"))