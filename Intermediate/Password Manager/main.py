from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
 
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("Intermediate/Password Manager/data.json", "r") as data_file:
                data = json.load(data_file)      
        except FileNotFoundError:      
            with open("Intermediate/Password Manager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)      
        else:        
            data.update(new_data)
            with open("Intermediate/Password Manager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
            
# ---------------------------- SEARCH PASSWORD ------------------------------- #  

def search():
    website = website_input.get().capitalize()
    try:
        with open("Intermediate/Password Manager/data.json", "r") as data_file:
            data = json.load(data_file)
            try:
                web_dict = data[website] 
            except KeyError:
                messagebox.showinfo(title="Oops", message="Website not found.")
            else:
                messagebox.showinfo(title=website, message=f"Email: {web_dict['email']}\nPassword: {web_dict['password']}")
                   
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    
    
             
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Intermediate/Password Manager/logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

email_username_input = Entry(width=37)
email_username_input.grid(row=2, column=1, columnspan=2)
email_username_input.insert(0,"liz.gokhvat@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

gen_button = Button(text= "Generate Password", command=generate_password, width=12)
gen_button.grid(row=3, column=2)

add_button = Button(text= "Add", command=save_password, width=35)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text= "Search",command=search ,width=12)
search_button.grid(row=1, column=2)

window.mainloop()



        # is_ok = messagebox.askokcancel(title=website, 
        #                             message=f"These are the details entered:\nEmail: {email} "
        #                                         f"\nPassword: {password} \nIs it ok to save?")
        # if is_ok:
        
        
    #         website = website_input.get()
    # email = email_username_input.get()
    # password = password_input.get()
    
    # new_data = {
    #     website: {
    #         "email": email,
    #         "password": password
    #     }
    # }
    
    # info = f"{website} | {email} | {password}\n"
    
    # if len(website) == 0 or len(password):
    #     print(len(website))
    #     print(len(password))
    #     print(info)
    #     messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    # else:
    #     with open("Intermediate/Password Manager/data.txt", "a") as data_file:
    #         json.dump(new_data, data_file)
    #         website_input.delete(0,END)
    #         password_input.delete(0,END)
