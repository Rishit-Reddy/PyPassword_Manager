# ----------------------------Imports----------------------------------------#
from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
import pyperclip
import json
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
    
    data_format = {
        web : {
            "Email":email,
            "Password":password,
        }
    }
    
    path = 'passwords.json'
        
    if web == "" or email == "" or password == "":
        messagebox.showerror(title="Enter Details", message="You have entered nothing, enter something!")
    else:
        # with open(path, 'a') as f:
        #     f.write(f"{web} | {email} | {password}\n")
        #     
        try:
            with open(path, 'r') as f:
                read_data = json.load()
        except FileNotFoundError:
            with open(path, mode="w") as f:
                json.dump(data_format, f, indent=2)
        else:
            read_data.update(data_format)
            with open(path, "w") as f:
                f.dump(read_data, f, indent=2)
            messagebox.showinfo(title="Successful", message="Details added")
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)    
            

#----------------------------Search Password ------------------------#
def search_password():
    
    website = web_entry.get()
    path = 'passwords.json'
    
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File Not Found!, Please add a password")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            msg = f"Email:{email}\nPassword:{password}"
            messagebox.showinfo(title="Success", message=msg)
            web_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            messagebox.showerror(title="Error", message="Website Not Found!, Please add a password")
    
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
#search btn
search = Button(text="Search", width=36, command=search_password)
search.grid(row=5, column=1, columnspan=2)
window.mainloop()