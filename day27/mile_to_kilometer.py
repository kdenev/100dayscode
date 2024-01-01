from tkinter import *

MILES_KM = 1.60934

app = Tk()

app.title("Mile to Km Converter")
app.minsize(width=300, height=100)

miles_input  = Entry(width=7)
miles_label = Label(text="Miles")
equal_label = Label(text="Is equal to")
converted_label = Label(text=0)
km_label = Label(text="Km")

def conver_miles(miles_input:Entry = miles_input, converted_label:Label = converted_label):
    converted_label.config(text=round(int(miles_input.get())*MILES_KM))
calculate_button = Button(text="Calculate", command=conver_miles)

miles_input.grid(column=1, row=0, pady=10)
miles_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1, padx=50)
converted_label.grid(column=1, row=1)
km_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)


app.mainloop()