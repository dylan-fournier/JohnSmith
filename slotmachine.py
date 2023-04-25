import tkinter as tk
window= tk.Tk()
window.title("Slot Machine")
window.geometry("1280x720")
window.resizable(0,0)

mainLbl=tk.Label(window, text="wazzup",font=("Arial",50))
mainLbl.place(x=100,y=100)

spinBtn=tk.Button(window, text="SPIN!",font=("Arial",30))
spinBtn.place(x=580,y=500)
window.mainloop()