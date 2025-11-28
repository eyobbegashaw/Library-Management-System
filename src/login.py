from tkinter import ttk, messagebox, PhotoImage
import tkinter as tk
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "123":
        messagebox.showinfo("Login Success", "Welcome Admin!")
        window.destroy()
        import DBUtech
    
        
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
window = tk.Tk()
window.geometry('800x800')
window.title("Login form of the DBU TECH LABRARY")
 
logo = PhotoImage(file="assets/logo.png")
label_logo = tk.Label(window, image=logo)
label_logo.pack(pady=20)


label_username = tk.Label(window, text="Username:", font=("Arial", 14))
label_username.pack(pady=10)
entry_username = tk.Entry(window, font=("Arial", 14))
entry_username.pack(pady=10)

 
label_password = tk.Label(window, text="Password:", font=("Arial", 14))
label_password.pack(pady=10)
entry_password = tk.Entry(window, show="*", font=("Arial", 14))
entry_password.pack(pady=10)

 
button_login = tk.Button(window, text="Login", command=login, font=("Arial", 14))
button_login.pack(pady=20)

 
button_add = tk.Button(window, text="Add", font=("Arial", 14))
button_delete = tk.Button(window, text="Delete", font=("Arial", 14))
button_update = tk.Button(window, text="Update", font=("Arial", 14))
 
label_info = tk.Label(window, text="Welcome to the DBU Tech Library!", font=("Arial", 16))

 
window.mainloop()