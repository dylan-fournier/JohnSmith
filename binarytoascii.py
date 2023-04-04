from tkinter import *
import pyperclip
window=Tk()
window.title("Binary To ASCII Converter")
window.geometry("1280x720")
window.resizable(0,0)

buttonone = 0
buttontwo = 0
buttonthree = 0
buttonfour = 0
buttonfive = 0
buttonsix = 0
buttonseven = 0
buttoneight = 0
letter=""
mode=0
modelabel = "ASCII"

def copycharacter(event):
    pyperclip.copy(letter)
def update():
    global letter
    global modelabel
    if mode==0:
        modelabel="ASCII"
        letter = str(buttonone) + str(buttontwo)+str(buttonthree)+str(buttonfour)+str(buttonfive)+str(buttonsix)+str(buttonseven)+str(buttoneight)
        letter = chr(int(letter,2))
        lbl['text']=letter
    else:
        modelabel="Decimal"
        letter = str(buttonone) + str(buttontwo)+str(buttonthree)+str(buttonfour)+str(buttonfive)+str(buttonsix)+str(buttonseven)+str(buttoneight)
        letter = int(letter,2)
        lbl['text']=str(letter)
    window.title("Binary To "+modelabel+" Converter")
    btnswitch['text']=modelabel + " Mode"
def switchclick(event):
    global mode
    if mode == 0:
        mode = 1
    else:
        mode = 0
    update()
def buttononeclick(event):
    global buttonone
    if buttonone == 0:
        buttonone=1
    else:
        buttonone=0
    btn1['text'] = str(buttonone)
    update()
def buttontwoclick(event):
    global buttontwo
    if buttontwo == 0:
        buttontwo=1
    else:
        buttontwo=0
    btn2['text'] = str(buttontwo)
    update()
def buttonthreeclick(event):
    global buttonthree
    if buttonthree == 0:
        buttonthree=1
    else:
        buttonthree=0
    btn3['text'] = str(buttonthree)
    update()
def buttonfourclick(event):
    global buttonfour
    if buttonfour == 0:
        buttonfour=1
    else:
        buttonfour=0
    btn4['text'] = str(buttonfour)
    update()
def buttonfiveclick(event):
    global buttonfive
    if buttonfive == 0:
        buttonfive=1
    else:
        buttonfive=0
    btn5['text'] = str(buttonfive)
    update()
def buttonsixclick(event):
    global buttonsix
    if buttonsix == 0:
        buttonsix=1
    else:
        buttonsix=0
    btn6['text'] = str(buttonsix)
    update()
def buttonsevenclick(event):
    global buttonseven
    if buttonseven == 0:
        buttonseven=1
    else:
        buttonseven=0
    btn7['text'] = str(buttonseven)
    update()
def buttoneightclick(event):
    global buttoneight
    if buttoneight == 0:
        buttoneight=1
    else:
        buttoneight=0
    btn8['text'] = str(buttoneight)
    update()

lbl = Label(window, text=letter,font=("Arial", 50))
lbl.place(x=620,y=200)
btnswitch = Button(window, text="ModeSwitch",font=("Arial",15))
btnswitch.place(x=200,y=600)
btn1 = Button(window, text=buttonone,font=("Arial", 20))
btn1.place(x=200,y=450)
btn2 = Button(window, text=buttontwo,font=("Arial", 20))
btn2.place(x=300,y=450)
btn3 = Button(window, text=buttonthree,font=("Arial", 20))
btn3.place(x=400,y=450)
btn4 = Button(window, text=buttonfour,font=("Arial", 20))
btn4.place(x=500,y=450)
btn5 = Button(window, text=buttonfive,font=("Arial", 20))
btn5.place(x=600,y=450)
btn6 = Button(window, text=buttonsix,font=("Arial", 20))
btn6.place(x=700,y=450)
btn7 = Button(window, text=buttonseven,font=("Arial", 20))
btn7.place(x=800,y=450)
btn8 = Button(window, text=buttoneight,font=("Arial", 20))
btn8.place(x=900,y=450)
copybtn = Button(window,font=("Arial", 15), text="Copy Character To Clipboard")
copybtn.place(x=520,y=600)
#function calling time yay
btnswitch.bind('<Button-1>',switchclick)
btn1.bind('<Button-1>', buttononeclick)
btn2.bind('<Button-1>', buttontwoclick)
btn3.bind('<Button-1>', buttonthreeclick)
btn4.bind('<Button-1>', buttonfourclick)
btn5.bind('<Button-1>', buttonfiveclick)
btn6.bind('<Button-1>', buttonsixclick)
btn7.bind('<Button-1>', buttonsevenclick)
btn8.bind('<Button-1>', buttoneightclick)
copybtn.bind('<Button-1>',copycharacter)
#endy  bit
update()
window.mainloop()