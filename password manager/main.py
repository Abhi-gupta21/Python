import tkinter
from tkinter import messagebox
import random 
import pyperclip 
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_passwd():
    lower_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_alphabets = []
    for _ in lower_alphabets:
        upper_alphabets.append(_.upper())

    alphas = lower_alphabets + upper_alphabets
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    syms = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_alphas = random.randint(8,10)
    nr_nums = random.randint(2,4)
    nr_syms = random.randint(2,4)

    pswd_list = []

    for char in range(nr_alphas):
        pswd_list.append(random.choice(alphas))

    for char in range(nr_nums):
        pswd_list.append(random.choice(nums))

    for char in range(nr_syms):
        pswd_list.append(random.choice(syms))

    random.shuffle(pswd_list)

    created_paswd = ""
    for i in pswd_list:
        created_paswd += i
    
    password_entry.insert(0, created_paswd)
    pyperclip.copy(created_paswd)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    web = website_entry.get()
    mail = email_entry.get()
    pswd = password_entry.get()
    new_data = {web:{"email": mail, "password": pswd}}
    if web == "" or pswd == "":
        messagebox.showerror(title = "Error", message = "Please ensure all the fields are filled")

    else:
        try:
            data_file = open("day 29 pswdmanager/data.json", "r")
        except FileNotFoundError:
            data_file = open("day 29 pswdmanager/data.json", "w")
            json.dump(new_data, data_file, indent = 4)
            data_file.close()
        else:
            # Reading old data
            data = json.load(data_file)
            # Updating old data
            data.update(new_data)
            data_file.close()
            data_file = open("day 29 pswdmanager/data.json", "w")
            # Saving updated data
            json.dump(data, data_file, indent = 4)
            data_file.close()
        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

# ---------------------------- SEARCH PASSWORD --------------------------- #

def search():
    website = website_entry.get()
    try:
        datafile = open("day 29 pswdmanager/data.json", 'r')
        data_dict = json.load(datafile) 
        mail_id = data_dict[website]["email"]
        password = data_dict[website]["password"]
    
    except FileNotFoundError:
        messagebox.showerror(title = "Error", message = "The data file is not found.")

    except KeyError:
        messagebox.showerror(title = "Error", message = "Website not found in your data file.")
    
    else:
        messagebox.showinfo(title = f"credentials for {website}", message = f"Email id - {mail_id}\nPassword - {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = tkinter.Canvas(width = 200, height = 200)
lock_img = tkinter.PhotoImage(file = "day 29 pswdmanager/logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0,column = 1)



website_label = tkinter.Label(text = "Website:")
website_label.grid(row = 1, column = 0)


website_entry = tkinter.Entry(width=35)
website_entry.grid(row = 1, column = 1, columnspan = 2)
website_entry.focus()

email_label = tkinter.Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)

email_entry = tkinter.Entry(width=35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, 'ketepask@mail.uc.edu')

password_label = tkinter.Label(text = "Password:")
password_label.grid(row = 3, column = 0)

password_entry = tkinter.Entry(width=35)
password_entry.grid(row = 3, column = 1, columnspan = 2)

genpass_button = tkinter.Button(text = "Generate Password", command = gen_passwd)
genpass_button.grid(row = 3, column = 3)

add_button = tkinter.Button(text="Add", width = 30, command = add_password)
add_button.grid(row = 4, column = 1, columnspan = 2)

search_button = tkinter.Button(text = "Search", command = search)
search_button.grid(row = 1, column = 3)

window.mainloop()