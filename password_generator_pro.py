import tkinter as tk
from tkinter import messagebox
import random
import string

def check_strength(password):

    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength <= 1:
        return "Weak"
    elif strength == 2:
        return "Medium"
    elif strength == 3:
        return "Strong"
    else:
        return "Very Strong"


def generate_password():

    try:
        length = int(length_entry.get())

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters

        if var_numbers.get():
            characters += string.digits

        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error","Select character type")
            return

        password = "".join(random.choice(characters) for i in range(length))

        result_entry.delete(0,tk.END)
        result_entry.insert(0,password)

        strength = check_strength(password)
        strength_label.config(text=f"Strength: {strength}")

    except:
        messagebox.showerror("Error","Enter valid length")


def copy_password():

    password = result_entry.get()

    if password == "":
        messagebox.showwarning("Warning","Generate password first")
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    messagebox.showinfo("Copied","Password copied")


def save_password():

    password = result_entry.get()

    if password == "":
        messagebox.showwarning("Warning","Generate password first")
        return

    with open("passwords.txt","a") as file:
        file.write(password+"\n")

    messagebox.showinfo("Saved","Password saved successfully")


root = tk.Tk()
root.title("Cyber Password Generator")
root.geometry("420x400")
root.configure(bg="#0f172a")

title = tk.Label(root,text="CYBER PASSWORD GENERATOR",
                 font=("Arial",16,"bold"),
                 fg="lime",
                 bg="#0f172a")

title.pack(pady=15)

tk.Label(root,text="Password Length",
         fg="white",
         bg="#0f172a").pack()

length_entry = tk.Entry(root)
length_entry.pack()

var_letters = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root,text="Include Letters",
               variable=var_letters,
               bg="#0f172a",
               fg="white",
               selectcolor="black").pack()

tk.Checkbutton(root,text="Include Numbers",
               variable=var_numbers,
               bg="#0f172a",
               fg="white",
               selectcolor="black").pack()

tk.Checkbutton(root,text="Include Symbols",
               variable=var_symbols,
               bg="#0f172a",
               fg="white",
               selectcolor="black").pack()

generate_btn = tk.Button(root,text="Generate Password",
                         command=generate_password,
                         bg="lime")

generate_btn.pack(pady=10)

result_entry = tk.Entry(root,width=30)
result_entry.pack(pady=10)

strength_label = tk.Label(root,text="Strength:",
                          fg="yellow",
                          bg="#0f172a")

strength_label.pack()

copy_btn = tk.Button(root,text="Copy Password",
                     command=copy_password)

copy_btn.pack(pady=5)

save_btn = tk.Button(root,text="Save Password",
                     command=save_password)

save_btn.pack()

root.mainloop()