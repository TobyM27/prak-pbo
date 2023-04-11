import tkinter as tk

nyoba = tk.Tk()
readimage = tk.PhotoImage(file="download.jpg")
def pushed():
	nyoh = tk.Label(nyoba, image=readimage)
	nyoh.pack()

nyoba.geometry("300x300")
nyoba.title("MAIN GUI")
title = tk.Label(nyoba, text="Kita rehat sejenak")
button = tk.Button(nyoba, text="Klik disini", command=pushed)
title.pack()
button.pack()

nyoba.mainloop()
