import tkinter as tk
from tkinter import messagebox
import string

def is_palindrome(text):
    
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def check_palindrome():
    user_input = entry.get()

    if not user_input:
        messagebox.showwarning("Warning", "Please enter a string or number!")
        return

    if is_palindrome(user_input):
        result_label.config(text="It is a PALINDROME ✔️", fg="green")
    else:
        result_label.config(text="It is NOT a palindrome ✖️", fg="red")

root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("400x250")
root.resizable(False, False)

label = tk.Label(root, text="Enter a string or number:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Palindrome", command=check_palindrome, font=("Arial", 12))
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=20)

root.mainloop()