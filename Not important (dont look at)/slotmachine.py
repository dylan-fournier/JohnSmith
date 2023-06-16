import tkinter as tk
import asyncio
import random
import time
random.seed()
window= tk.Tk()
window.title("Slot Machine")
window.geometry("1280x720")
window.resizable(0,0)

num = [0,0,0,0,0]
def update():
    mainLbl['text'] = str(num[0])+str(num[1])+str(num[2])+str(num[3])+str(num[4])

mainLbl=tk.Label(window, text=str(num[0])+str(num[1])+str(num[2])+str(num[3])+str(num[4]),font=("Arial",50))
mainLbl.place(x=100,y=100)
def changeNums(Event):
    for i in range(40):
        for j in range(5):
            num[j] = random.randint(0,9)
        time.sleep(0.01)
        update()
spinBtn=tk.Button(window, text="SPIN!",font=("Arial",30))
spinBtn.place(x=580,y=500)
spinBtn.bind('<Button-1>', changeNums)
window.mainloop()