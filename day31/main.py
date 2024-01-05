from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
row = 0
i = 0

# Import data
try:
    data = pd.read_csv(r"day31\data\words_to_lear.csv")
except FileNotFoundError:
    data = pd.read_csv(r"day31\data\french_words.csv")

# Define random word selects
def select_random_row():
    global row, i
    i = random.randint(0, len(data)-1)
    row = data.loc[i]
    language_title.config(text="French", bg="white", fg="black")
    word_title.config(text=row.French, bg="white", fg="black")
    canvas.itemconfig(flashcard, image = front_img)
    window.update()
    window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(flashcard, image = back_img)
    language_title.config(text="English", bg="#91c2af", fg="white")
    word_title.config(text=row.English, bg="#91c2af", fg="white")

def known_word():
    data.drop(i, axis=0, inplace=True)
    data.to_csv(r"day31\data\words_to_lear.csv", index=False)
    select_random_row()


# Create the app
window = Tk()
window.minsize(width=500, height=400)
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Flashcards
front_img = PhotoImage(file=r"day31\images\card_front.png")
back_img = PhotoImage(file=r"day31\images\card_back.png")
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard = canvas.create_image(400, 265, image=front_img)


# Words
language_title = Label(text="Title", font=TITLE_FONT, bg="white")
word_title = Label(text="word", font=WORD_FONT, bg="white")


# Buttons
yes_img = PhotoImage(file=r"day31\images\right.png")
no_img = PhotoImage(file=r"day31\images\wrong.png")
yes_button = Button(image=yes_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word)
no_button = Button(image=no_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=select_random_row)

# Layout
canvas.grid(column=0, row=0, columnspan=2)
language_title.place(x=300, y=150)
word_title.place(x=270, y=250)
yes_button.grid(column=0, row=1)
no_button.grid(column=1, row=1)

select_random_row()

window.mainloop()