import tkinter as tk
from tkinter import ttk
import subprocess
import sys

def open_window(filename):
    subprocess.Popen([sys.executable, filename])

def create_button(frame, text, command):
    button = ttk.Button(frame, text=text, command=command, style="Custom.TButton")
    button.pack(fill=tk.BOTH, padx=20, pady=10)
    return button

root = tk.Tk()
root.title("Gestion de Stock")
root.geometry("800x600")
root.resizable(True, True)

# Update the background color
root.configure(bg="lightgray")

title_label = tk.Label(root, text="Project Base Donnée - Gestion de Stock", font=("Arial", 30), padx=10, pady=10)
title_label.pack(pady=25)

button_frame = ttk.Frame(root)
button_frame.pack(pady=50)

button_style = ttk.Style()

# Update the style for the buttons
button_style.configure("Custom.TButton", font=("Arial", 18), padding=10, width=30, background="gray", foreground="black")

button1 = create_button(button_frame, "ARTICLES", lambda: open_window("articles.py"))
button2 = create_button(button_frame, "COMMANDES", lambda: open_window("commandes.py"))
button3 = create_button(button_frame, "CATÉGORIES", lambda: open_window("categories.py"))
button4 = create_button(button_frame, "LIVRAISONS", lambda: open_window("livraisons.py"))
button5 = create_button(button_frame, "CLIENTS", lambda: open_window("clients.py"))
button6 = create_button(button_frame, "FOURNISSEURS", lambda: open_window("fournisseurs.py"))
#button7 = create_button(button_frame, "STOCK", lambda: open_window("displayall.py"))
#button8 = create_button(button_frame, "STATISTIQUES", lambda: open_window("g-stat.py"))

root.mainloop()
