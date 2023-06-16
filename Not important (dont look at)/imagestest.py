import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.geometry("1280x720")
frame = tk.Frame(window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5) 

image= ImageTk.PhotoImage(Image.open("test.png"))

label = tk.Label(frame, image= image)
label.pack()

window.mainloop()