import tkinter
from PIL import Image, ImageTk
from tkinter import END
from tkinter import messagebox
import random
import pyperclip
import json


# --------------------------- SEARCH PASSWORD GENERATOR -------------------------- #

def search():

    website = entry_website.get()
    print(website)

    try:
        with open("password.json","r") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data File Found")
        # with open("password.json") as f:
        #     data = json.load(f)
        #     json.dump(data)

    else:
        if website in data:
            print(data)
            email = data[website]['email']
            password = data[website]['password']

            print(email,password)

            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")

# --------------------------- PASSWORD GENERATOR -------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)


    password_final = "".join(password_list)

    print(f"Your password is: {password_final}")
    entry_password.insert(0,password_final)

    pyperclip.copy(password_final)

# --------------------------- SAVE PASSWORD -------------------------- #

def save():

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    new_data = {website:{"email":email,"password":password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops",message="Please make sure you haven't left any fields empty.")
    else:
        # is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n{email} \n{password}")
        # print(is_ok)
        #
        # if is_ok:
        #     with open("password.txt","a") as f:
        #         f.write(f"{website} | {email} | {password}\n")
        #         entry_website.delete(0,END)
        #         entry_password.delete(0,END)
        try:
            with open("password.json","r") as f:

                 # Reading old data
                 data = json.load(f)

        except FileNotFoundError:
            with open("password.json","w") as f:
                 json.dump(new_data,f,indent=4)

        else:
            # Updating old data with new_data
            data.update(new_data)

            with open("password.json", "w") as f:

                 # Saving updated data
                 json.dump(data,f,indent=4)

        finally:
            entry_website.delete(0, END)
            entry_password.delete(0,END)


# --------------------------- UI SETUP -------------------------- #

window = tkinter.Tk()
window.geometry("600x400")
window.title("Password Manager")
window.config(padx=20,pady=20,bg="white")

canvas_add = tkinter.Canvas(width=200,height=200,bg="white",highlightthickness=0)


image_add = Image.open("logo.png")
image = ImageTk.PhotoImage(image_add)
canvas_add.create_image(100,100,image=image)
canvas_add.grid(row=0,column=1,pady=10)


label_website = tkinter.Label(text="Website:",font=("Arial",12,"bold"),bg="white")
label_website.grid(row=1,column=0, sticky="e", pady=5)


entry_website = tkinter.Entry(width=35)
entry_website.grid(row=1,column=1,columnspan=2, sticky="w", pady=5)
entry_website.focus()


label_email_user_name = tkinter.Label(text="Email/Username:",font=("Arial",12,"bold"),bg="white")
label_email_user_name.grid(row=2,column=0, sticky="e", pady=5)

entry_email = tkinter.Entry(width=35)
entry_email.grid(row=2,column=1,columnspan=2, sticky="w", pady=5)
entry_email.insert(0,"akshitmunjal479@gmail.com")

password_website = tkinter.Label(text="Password:",font=("Arial",12,"bold"),bg="white")
password_website.grid(row=3,column=0, sticky="e", pady=5)

entry_password = tkinter.Entry(width=21)
entry_password.grid(row=3,column=1, sticky="w", pady=5)


generate_password_button = tkinter.Button(text="Generate Password",bg="white",command=generate_password)
generate_password_button.grid(row=3,column=2, sticky="w", pady=5)


add_button = tkinter.Button(text="Add",bg="white",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2, pady=10)

search_button = tkinter.Button(text="Search",bg="white",command=search)
search_button.grid(row=1,column=2,sticky="w",pady=10)

window.mainloop()