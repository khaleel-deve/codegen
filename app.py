import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime

# Functions
def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)

def rename_files():
    folder = folder_path.get()
    pre = prefix.get()
    suf = suffix.get()

    if not os.path.isdir(folder):
        messagebox.showerror("Error", "Invalid folder path.")
        return

    files = os.listdir(folder)
    count = 0

    for filename in files:
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            name, ext = os.path.splitext(filename)
            new_name = f"{pre}_{name}_{suf}{ext}"
            new_path = os.path.join(folder, new_name)
            os.rename(filepath, new_path)
            count += 1

    messagebox.showinfo("Success", f"Renamed {count} files.")

# UI Setup
app = tk.Tk()
app.title("Bulk File Renamer")
app.geometry("420x260")
app.configure(bg="#2e2e2e")

# Style (No external themes required)
style = ttk.Style(app)
style.theme_use("clam")
style.configure("TLabel", background="#2e2e2e", foreground="white", font=("Segoe UI", 10))
style.configure("TButton", background="#4b4b4b", foreground="white", font=("Segoe UI", 10))
style.configure("TEntry", fieldbackground="#4b4b4b", foreground="white", background="#4b4b4b")

# Variables
folder_path = tk.StringVar()
prefix = tk.StringVar()
suffix = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))

# Widgets
ttk.Label(app, text="Select Folder:").pack(pady=5)
ttk.Entry(app, textvariable=folder_path, width=50).pack()
ttk.Button(app, text="Browse", command=select_folder).pack(pady=5)

ttk.Label(app, text="Prefix:").pack()
ttk.Entry(app, textvariable=prefix, width=50).pack()

ttk.Label(app, text="Suffix:").pack()
ttk.Entry(app, textvariable=suffix, width=50).pack()

ttk.Button(app, text="Rename Files", command=rename_files).pack(pady=15)

app.mainloop()
