import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog, messagebox

def open_file():
    """Fungsi ini berguna untuk membuka file yang nanti akan diedit"""
    filepath = askopenfilename(
        filetypes=[("Dokumen Teks", "*.txt"),("Semua Files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        text_edit.insert(tk.END, text)
    window.title(f"Microsoft Word v2.0 bajakan - {filepath}")

def save_file():
    """Fungsi ini berguna untuk menyimpan sebuah file yang telah diedit"""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Dokumen Teks", "*.txt"), ("Semua Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = text_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Microsoft Word v2.0 Bajakan - {filepath}")

    if filepath: 
        try:
            with open(filepath, mode="w", encoding="utf-8") as output_file:
                text = text_edit.get("1.0", tk.END)
                output_file.write(text)
            window.title(f"Microsoft Word v2.0 Bajakan - {filepath}")
        except Exception as e:
            messagebox.showerror("error", f"File tidak berhasil disimpan! {str(e)}")

def new_file():
    text_edit.delete('1.0', tk.END)
                 

window = tk.Tk()
window.title("Microsoft Word v2.0 Bajakan")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

text_edit = tk.Text(window)
frame_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
button_open = tk.Button(frame_buttons, text="Buka file", command=open_file)
button_save = tk.Button(frame_buttons, text="Save file sebagai...", command=save_file)
button_renew = tk.Button(frame_buttons, text="Kosongkan halaman ", command=new_file)

button_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
button_save.grid(row=1, column=0, sticky="ew", padx=5)
button_renew.grid(row=2,column=0, sticky="ew", padx=5)

frame_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
