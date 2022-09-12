# ----------------------------Imports----------------------------------------#
from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    web = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    path = 'passwords.txt'
    if not os.path.exists(path):
        with open(path, 'w') as f:
            pass 
    
    if web == "" or email == "" or password == "":
        messagebox.showerror(title="Enter Details", message="You have entered nothing, enter something!")
    else:
        with open(path, 'a') as f:
            f.write(f"{web} | {email} | {password}\n")
            web_entry.delete(0, END)
            password_entry.delete(0, END)    
        messagebox.showinfo(title="Successful", message="Details added")
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#image
canvas = Canvas(width=200, height=200)
img_logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=img_logo)
canvas.grid(row=0, column=1, sticky="W")

#Website input
website_label = Label(text="Website:")
website_label.grid(row=1, column=0 )
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(row=1, column=1, columnspan=2)

#TODO change it to listbox with list of emails, let emails = []
#Email/username Input
website_label = Label(text="Email/Username:")
website_label.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.insert(0, "rpalle1@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

#Password Input
website_label = Label(text="Password:")
website_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()