from tkinter import *
from tkinter import font
from backend import Database
import tkinter

# Function

database = Database("account.db")


def bankAccount():
    global tuple_list
    global username_db
    global password_db
    global username
    global password
    try:
        tuple_list = database.search(username=username_entry_text_login.get(),
                                     password=password_entry_text_login.get()
                                     )
        username_db = tuple_list[0][1]
        password_db = tuple_list[0][2]
        username = username_entry_text_login.get()
        password = password_entry_text_login.get()
        print(username_db == username and password_db == password)
        if username_db == username and password_db == password:
            blank_login.config(text="Logged in!", font=myFont_login)
        else:
            blank_login.config(text="Check your credentials!")
    except IndexError:
        blank_login.config(text="Check your credentials!", font=myFont_login)


def login_account():
    global myFont_login
    global blank_login
    global username_entry_text_login
    global password_entry_text_login
    global username_entry_text
    global password_entry_text
    list = [username_entry_text.get(), password_entry_text.get()]
    tuple_regi = database.search(username=username_entry_text.get(), password=password_entry_text.get())
    if len(list[0]) < 1 or len(list[1]) < 1:
        blank.config(text="Fill the credentials.", font=myFont)
    elif len(tuple_regi) >= 1:
        blank.config(text="That account already exists!")
    else:
        database.insert(
            username_entry_text.get(),
            password_entry_text.get()
        )
        blank.config(text="Registered in!", font=myFont)
        print(database.view())
        newwindow = tkinter.Toplevel(window)
        newwindow.wm_title("Login")
        myFont_login = font.Font(family="Helvetica", size=10)
        newwindow.geometry("500x100")

        # Interface
        blank_login = Label(newwindow, text="")
        blank_login.grid(row=0, column=0)

        username = Label(newwindow, text="Username", font=myFont)
        username.grid(row=1, column=0)
        username_entry_text_login = StringVar()
        username_entry = Entry(
            newwindow, textvariable=username_entry_text_login, width=25, font=myFont_login)
        username_entry.grid(row=1, column=1)

        password = Label(newwindow, text="Password", font=myFont_login)
        password.grid(row=2, column=0)
        password_entry_text_login = StringVar()
        password_entry = Entry(
            newwindow, textvariable=password_entry_text_login, width=25, font=myFont_login, show="*")
        password_entry.grid(row=2, column=1)

        login_login = Button(newwindow, text="Login",
                             font=myFont_login, command=bankAccount)
        login_login.grid(row=3, column=1)


window = Tk()
window.wm_title("Create account")
window.geometry("500x100")

myFont = font.Font(family="Helvetica", size=10)


# Interface
blank = Label(window, text="")
blank.grid(row=0, column=0)

username = Label(window, text="Username", font=myFont)
username.grid(row=1, column=0)
username_entry_text = StringVar()
username_entry = Entry(
    window, textvariable=username_entry_text, width=25, font=myFont)
username_entry.grid(row=1, column=1)

password = Label(window, text="Password", font=myFont)
password.grid(row=2, column=0)
password_entry_text = StringVar()
password_entry = Entry(
    window, textvariable=password_entry_text, width=25, font=myFont, show="*")
password_entry.grid(row=2, column=1)

login = Button(window, text="Register", font=myFont, command=login_account)
login.grid(row=3, column=1)

window.mainloop()
