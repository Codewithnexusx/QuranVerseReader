# -*- coding: utf-8 -*-
import requests
import tkinter as tk
from tkinter import messagebox

def get_ayah():
    surah = surah_entry.get()
    ayah = ayah_entry.get()

    url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/editions/quran-uthmani,en.sahih"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"API Error:\n{e}")
        return

    data = response.json()["data"]
    arabic = data[0]["text"]
    english = data[1]["text"]

    arabic_label.config(text=arabic)
    english_label.config(text=english)


# GUI Window
root = tk.Tk()
root.title("Quran Reader")
root.geometry("700x400")

# Input fields
tk.Label(root, text="Surah Number:").pack()
surah_entry = tk.Entry(root)
surah_entry.pack()

tk.Label(root, text="Ayah Number:").pack()
ayah_entry = tk.Entry(root)
ayah_entry.pack()

tk.Button(root, text="Load Ayah", command=get_ayah).pack(pady=10)

# Arabic Display (Large font)
arabic_label = tk.Label(root, text="", font=("Arial", 28), wraplength=650, justify="right")
arabic_label.pack(pady=20)

# English Display
english_label = tk.Label(root, text="", font=("Arial", 14), wraplength=650, justify="left")
english_label.pack()

root.mainloop()
