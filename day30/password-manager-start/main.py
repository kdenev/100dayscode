from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
                    [random.choice(letters) for _ in range(nr_letters)]
                    + [random.choice(symbols) for _ in range(nr_symbols)]
                    + [random.choice(numbers) for _ in range(nr_numbers)]
                    )

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    # Entries
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email
            , "password": password
        }
    }

    # Empty fields check
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="No info", message="Please do not leave empty fields!")
    else:
        # Message box
        is_ok = messagebox.askokcancel(title=website
                            , message=f"You have entered a new password\nIs it ok to save?")
        
        if is_ok:
            try:
                with open(r"day30\password-manager-start\data.json", "r") as file:
                    # Reading the old data
                    data = json.load(file)
                    # Updategin the old data
                    data.update(new_data)
            except FileNotFoundError:
                with open(r"day30\password-manager-start\data.json", "w") as file:
                    # Creating and writing
                    json.dump(new_data, file, indent= 4)
            else:
                with open(r"day30\password-manager-start\data.json", "w") as file:
                    # Saving updated version
                    json.dump(data, file, indent= 4)
                    
            finally:
                # Delete info in fields
                website_input.delete(0,END)
                password_input.delete(0,END)

def find_password():
    # Entries
    website = website_input.get()
    try:
        with open(r"day30\password-manager-start\data.json", "r") as file:
            # Reading the old data
            data = json.load(file)
        web_data = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Error",message="Data file do not found!")
    except KeyError:
        messagebox.showerror(title="Error",message=f"No record of {website}!")
    else:
        messagebox.showinfo(title="Info", message=f"Email: {web_data["email"]}\nPassword: {web_data["password"]}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

# Logo
img = PhotoImage(file=r"day30\password-manager-start\logo.png") 
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image = img)

# Labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="Password")

# Buttons
generate_pass_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save)
search_button = Button(text="Search", command=find_password)

# Inputs
website_input = Entry(width=35)
email_input = Entry(width=35)
password_input = Entry(width=21)

# Layout
canvas.grid(column=1, row=0,)
website_label.grid(column=0, row=1)
website_input.grid(column=1, row=1, sticky="ew")
search_button.grid(column=2, row=1, sticky="ew", padx=3)
website_input.focus()
email_label.grid(column=0, row=2)
email_input.grid(column=1, row=2, columnspan=2, sticky="ew")
email_input.insert(0, "kd@gmail.com")
password_label.grid(column=0, row=3)
password_input.grid(column=1, row=3, sticky="ew")
generate_pass_button.grid(column=2, row=3, padx=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()