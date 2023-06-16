from tkinter import *
import pyperclip
window=Tk()
window.title("Binary To ASCII Converter")
window.geometry("1280x720")
window.resizable(0,0)

buttonzero = 0
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
        letter = str(buttonzero) + str(buttonone) + str(buttontwo)+str(buttonthree)+str(buttonfour)+str(buttonfive)+str(buttonsix)+str(buttonseven)+str(buttoneight)
        letter = chr(int(letter,2))
        lbl['text']=letter
    elif mode==1:
        modelabel="Decimal"
        letter = str(buttonzero) + str(buttonone) + str(buttontwo)+str(buttonthree)+str(buttonfour)+str(buttonfive)+str(buttonsix)+str(buttonseven)+str(buttoneight)
        letter = int(letter,2)
        lbl['text']=str(letter)
    elif mode==2:
        modelabel="Hex"
        letter = str(buttonzero) + str(buttonone) + str(buttontwo)+str(buttonthree)+str(buttonfour)+str(buttonfive)+str(buttonsix)+str(buttonseven)+str(buttoneight)
        letter = str(hex(int(letter,2)))
        #fun fact! truncating because hex always has a prefix in python
        letter = letter[2:]
        letter = letter.upper()
        lbl['text']=letter
    elif mode==3:
        modelabel="Octal"
        letter = str(buttonzero) + str(buttonone) + str(buttontwo)+str(buttonthree)+str(buttonfour)+str(buttonfive)+str(buttonsix)+str(buttonseven)+str(buttoneight)
        letter = str(oct(int(letter,2)))
        #again, trunkating because there is a mandatory prefix
        letter = letter[2:]
        lbl['text']=letter
    btn0['text'] = str(buttonzero)
    btn1['text'] = str(buttonone)
    btn2['text'] = str(buttontwo)
    btn3['text'] = str(buttonthree)
    btn4['text'] = str(buttonfour)
    btn5['text'] = str(buttonfive)
    btn6['text'] = str(buttonsix)
    btn7['text'] = str(buttonseven)
    btn8['text'] = str(buttoneight)
    
    window.title("Binary To "+modelabel+" Converter")
    btnswitch['text']=modelabel + " Mode"
def switchclick(event):
    global mode
    if mode == 0:
        mode = 1
    elif mode==1:
        mode = 2
    elif mode ==2:
        mode = 3
    elif mode ==3:
        mode = 0
    update()
def clear(event):
    global buttonzero
    global buttonone
    global buttontwo
    global buttonthree
    global buttonfour
    global buttonfive
    global buttonsix
    global buttonseven
    global buttoneight
    buttonzero = 0
    buttonone=0
    buttontwo=0
    buttonthree=0
    buttonfour=0
    buttonfive=0
    buttonsix=0
    buttonseven =0
    buttoneight = 0
    update()
def buttonzeroclick(event):
    global buttonzero
    if buttonzero ==0:
        buttonzero = 1
    else:
        buttonzero = 0
    update()
def buttononeclick(event):
    global buttonone
    if buttonone == 0:
        buttonone=1
    else:
        buttonone=0
    update()
def buttontwoclick(event):
    global buttontwo
    if buttontwo == 0:
        buttontwo=1
    else:
        buttontwo=0
    update()
def buttonthreeclick(event):
    global buttonthree
    if buttonthree == 0:
        buttonthree=1
    else:
        buttonthree=0
    update()
def buttonfourclick(event):
    global buttonfour
    if buttonfour == 0:
        buttonfour=1
    else:
        buttonfour=0
    update()
def buttonfiveclick(event):
    global buttonfive
    if buttonfive == 0:
        buttonfive=1
    else:
        buttonfive=0
    update()
def buttonsixclick(event):
    global buttonsix
    if buttonsix == 0:
        buttonsix=1
    else:
        buttonsix=0
    update()
def buttonsevenclick(event):
    global buttonseven
    if buttonseven == 0:
        buttonseven=1
    else:
        buttonseven=0
    update()
def buttoneightclick(event):
    global buttoneight
    if buttoneight == 0:
        buttoneight=1
    else:
        buttoneight=0
    update()
def secretbutton(event):
    btn0.place(x=200,y=450)



lbl = Label(window, text=letter,font=("Arial", 50))
lbl.place(x=620,y=200)
btnswitch = Button(window, text="ModeSwitch",font=("Arial",15))
btnswitch.place(x=200,y=600)
btn0 = Button(window, text=buttonzero,font=("Minecraftia",20))
btn1 = Button(window, text=buttonone,font=("Arial", 20))
btn1.place(x=300,y=450)
btn2 = Button(window, text=buttontwo,font=("Arial", 20))
btn2.place(x=400,y=450)
btn3 = Button(window, text=buttonthree,font=("Arial", 20))
btn3.place(x=500,y=450)
btn4 = Button(window, text=buttonfour,font=("Arial", 20))
btn4.place(x=600,y=450)
btn5 = Button(window, text=buttonfive,font=("Arial", 20))
btn5.place(x=700,y=450)
btn6 = Button(window, text=buttonsix,font=("Arial", 20))
btn6.place(x=800,y=450)
btn7 = Button(window, text=buttonseven,font=("Arial", 20))
btn7.place(x=900,y=450)
btn8 = Button(window, text=buttoneight,font=("Arial", 20))
btn8.place(x=1000,y=450)
copybtn = Button(window,font=("Arial", 15), text="Copy Character To Clipboard")
copybtn.place(x=520,y=600)
#function calling time yay
btnswitch.bind('<Button-1>',switchclick)
btnswitch.bind('<Button-3>',clear)
btn0.bind('<Button-1>',buttonzeroclick)
btn1.bind('<Button-1>', buttononeclick)
btn2.bind('<Button-1>', buttontwoclick)
btn3.bind('<Button-1>', buttonthreeclick)
btn4.bind('<Button-1>', buttonfourclick)
btn5.bind('<Button-1>', buttonfiveclick)
btn6.bind('<Button-1>', buttonsixclick)
btn7.bind('<Button-1>', buttonsevenclick)
btn8.bind('<Button-1>', buttoneightclick)
copybtn.bind('<Button-1>',copycharacter)
copybtn.bind('<Button-3>',secretbutton)
#endy  bit
update()
window.mainloop()