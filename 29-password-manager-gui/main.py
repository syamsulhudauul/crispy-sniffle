# my pass app
import tkinter

FONT_NAME = "Courier"
FONT_SIZE = 12
FONT = (FONT_NAME, FONT_SIZE, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random
import pyperclip
import string


def generate_password():
    """Generate random password"""
    password_entry.delete(0, tkinter.END)
    password = ""
    for _ in range(0, 3):
        password += random.choice(string.ascii_letters)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """Save password to file"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
       tkinter.messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: "
                                                                      f"{email}\nPassword: {password}\nIs it ok to "
                                                                      f"save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)


website_label = tkinter.Label(text="Website:", font=FONT)
website_entry = tkinter.Entry(width=35)
website_entry.focus()
email_label = tkinter.Label(text="Email/Username:", font=FONT)
email_entry = tkinter.Entry(width=35)

password_label = tkinter.Label(text="Password:", font=FONT)
password_entry = tkinter.Entry(width=21)
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password, width=15)
add_button = tkinter.Button(text="Add", width=30, command=save)


# positioning
canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)

email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2)

password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
generate_password_button.grid(column=2, row=3)

add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
