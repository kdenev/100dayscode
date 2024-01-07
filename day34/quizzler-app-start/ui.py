from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR
                           , padx= 20
                           , pady = 20
                        )
        self.window.minsize(width=350, height=600)
        self.main_canvas()
        self.buttons()
        self.score()
        self.buttons()
        self.layout()
        self.window.mainloop()

    def main_canvas(self):
        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(20, 150, text="Question", font=("Arial", 20, "italic"))

    def score(self):
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}")
        self.score_label.config(bg=THEME_COLOR, fg="white")

    def buttons(self):
        yes_img = PhotoImage(r"day34\quizzler-app-start\images\true.png")
        no_img = PhotoImage(r"day34\quizzler-app-start\images\false.png")
        self.yes_button = Button(image=yes_img)
        self.no_button = Button(image=no_img)

    def layout(self):
        self.score_label.grid(column=1, row=0)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.yes_button.grid(column=0, row=2)
        self.no_button.grid(column=1, row=2)