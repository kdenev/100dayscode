from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)
my_label["text"] = "New Text"

# Entry

user_input = Entry(width=10)
user_input.grid(column=3, row=2)
print(user_input.get())

# Button
def button_clicked():
    print("I got clicked")

def change_label(label:Label = my_label, user_input:Entry = user_input):
    label.config(text=user_input.get())

my_button = Button(text="Click Me", command=change_label)
my_button.grid(column=1, row=1)

new_button = Button(text="New Button", command=change_label)
new_button.grid(column=2, row=0)

window.mainloop()
