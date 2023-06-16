from tkinter import *
import random
import numbers
from PIL import ImageTk,Image
import csv
import math
#hey dylan you need to fix the thing for big numbers in the mybuttonclicked event
gourd = 0
#what is clkamt used for? 
autosave = False
clkamt = 0
midski = 0
helper = 0
helpercost = 0
skunk = 0
skunkcost = 0
totalgourd = 0
zero = 0
saveconfirm = 0
loadconfirm = 0
midskicost = 0
#savefile = open("save.txt","w+")
print("Version 23.03.24 Rev. You")
#print the skunk
window=Tk()
window.title("You Smell: The Game")
window.geometry("1280x720")
window.resizable(0,0)
#MyButtonClicked = (
   # gourd = gourd + 1
    #gourdstr = str(gourd)
    #lbl2=Label(window, text=gourdstr + "%")
#)
helpercost = int(helper*1.2)
autosave = False
#functions go brrrr
def SaveForRealzies():
    with open('save.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([gourd, helper, helpercost, skunk, skunkcost, totalgourd, midski, midskicost, autosave, zero, zero, zero, zero, zero, zero, zero, zero, zero, zero]) #have at least 5 zeroes betweeen version so save files can update properly
    file.close()
def ScreenRefresh():
    lbl2['text'] = "You are " + str(gourd) + "%" + " smelly"
    lbl3['text'] = str(int(helper + skunk+(midski*100)) + 1) + "% SPC (Smell Per Click)"
    btn2['text'] = "Dirt (Cost " + str(helpercost+100) + "%) (+1% SPC)"
    btn3['text'] = "Skunk (Cost " + str(skunkcost + 1000) + "%) (+7% SPC)"
    midskibuybtn['text'] = "Mitski Songs (Cost " + str(midskicost + 10000) + "%) (+100% SPC)"
    numofhlp['text'] = str(helper) + " Dirt"
    numofsku['text'] = str(int(skunk/7)) + " Skunk"
    numofmidski['text']=str(int(midski))+" Midski Songs Playing"
def BuyHelper(event):
    global gourd
    global helper
    global helpercost
    global skunk
    if gourd >= helpercost + 100:
        helper = helper + 1
        gourd = gourd - (100 + helpercost)
        helpercost = int(helper * 1.4)
        ScreenRefresh()
    else:
        pass
def BuySkunk(event):
    global gourd
    global skunk
    global skunkcost
    if gourd >= skunkcost + 1000:
        skunk = skunk + 7
        gourd = gourd - (skunkcost + 1000)
        skunkcost = int(skunk * 1.7)
        ScreenRefresh()
        # lbl2['text'] = "You are " + str(gourd) + "%" + " smelly"
        # lbl3['text'] = str(int(helper + skunk) + 1) + "% SPC (Smell Per Click)"
        # btn3['text'] = "Skunk (Cost " + str(skunkcost + 1000) + "%) (+7% SPC)"
        # numofhlp['text'] = str(helper) + " Dirt"
        # numofsku['text'] = str(int(skunk/7)) + " Skunk"
    else:
        pass
def BuyMidski(event):
    global midski
    global gourd
    global midskicost
    midskicost = math.ceil(float(midski * 20.5))
    if gourd >= midskicost+10000:
        
        midski = midski + 1
        gourd = gourd - (midskicost+10000)
        midskicost = math.ceil(float(midski * 20.5))
        ScreenRefresh()
        # lbl2['text'] = "You are " + str(gourd) + "%" + " smelly"
        # lbl3['text'] = str(int(helper + skunk+(midski*100)) + 1) + "% SPC (Smell Per Click)"
        # btn3['text'] = "Skunk (Cost " + str(skunkcost + 1000) + "%) (+7% SPC)"
        # midskibuybtn['text'] = "Mitski Songs (Cost " + str(midskicost + 10000) + "%) (+100% SPC)"
        # numofhlp['text'] = str(helper) + " Dirt"
        # numofsku['text'] = str(int(skunk/7)) + " Skunk"
        # numofmidski['text']=str(int(midski))+" Midski Songs Playing"
def MyButtonClicked(event):
    global helper
    global gourd
    global skunk
    global totalgourd
    global loadconfirm
    global saveconfirm
    alertlbl['text'] = ""
    gourd = int(gourd) + int(helper) + 1 + int(skunk) + int(midski*100)
    if totalgourd < gourd:
        totalgourd = gourd
    else:
        totalgourd = int(totalgourd) + int(helper) + 1 + int(skunk)
    loadconfirm = 0
    saveconfirm = 0
    lbl2['text'] = "You are " + str(gourd) + "%" + " smelly"
def Crash(event):
    print("Error 1, Contact <developer> If You See This More Than Once")
    exit()
def AutosaveToggle(event):
    global autosave
    if autosave == True:
        autosave = False
        alertlbl['text'] = "Autosave Off"
    else:
        autosave = True
        alertlbl['text'] = "Autosave On"
def SaveGame(event):
    global gourd
    global helper
    global helpercost
    global skunk
    global skunkcost
    global totalgourd
    global saveconfirm
    import csv
    if saveconfirm == 0:
        alertlbl['text'] = 'Click again to Save'
        saveconfirm = 1
    elif saveconfirm == 1:
        SaveForRealzies()
        saveconfirm = 0
        alertlbl['text'] = 'Saved Sucsessfully'
        print("Save Pass")
    else:
        alertlbl['text'] = 'Error 2: Save fail'
        print("Save Fail")
def LoadGame(event):
    global gourd
    global helper
    global helpercost
    global skunk
    global skunkcost
    global totalgourd
    global loadconfirm
    global midski
    global midskicost
    global autosave
    if loadconfirm == 0:
        alertlbl['text'] = 'Click again to load'
        loadconfirm = 1
    elif loadconfirm == 1:
        try:
            with open('save.csv', 'r') as file:
                reader = csv.reader(file)
                for column in reader:
                    savelist = column
                    gourd = int(savelist[0])
                    helper = int(savelist[1])
                    helpercost = int(savelist[2])
                    skunk = int(savelist[3])
                    skunkcost = int(savelist[4])
                    totalgourd = int(savelist[5])
                    midski = int(savelist[6])
                    midskicost = int(savelist[7])
                    autosave = bool(savelist[8])
            helpercost = int(helper * 1.4)
            skunkcost = int(skunk * 1.7)
            ScreenRefresh()
            file.close()
            loadconfirm = 0
            alertlbl['text'] = 'Loaded Sucsessfully'
            print("Load Pass")
        except IndexError:
            alertlbl['text'] = 'Error 2.2: Load fail - File Corrupted'
        except FileNotFoundError:
            alertlbl['text'] = 'Error 2.1: Load fail - File Not Found'
        except:
            alertlbl['text'] = 'Error 2: Load fail'
    else:
        alertlbl['text'] = 'Error 2: Load fail'
        print("Load Fail")
        loadconfirm=0
    #print(savefile.read())
def OpenAchevements(event):
    global totalgourd
    print(str(totalgourd) + " Total Smell")
    alertlbl['text'] = "You have had " + str(totalgourd) + "% Smell Overall"
#no more functions!
btn=Button(window, text="Click Here!")
btn.place(x=600, y=550)
lbl=Label(window, text="How much do You smell?", font=("Arial", 50))
lbl.place(x=300, y=150)
lbl2=Label(window, text="You are " + str(gourd) + "%" + " smelly", font=("Arial", 35))
lbl2.place(x=450, y=300)
lbl3=Label(window, text=str(int(helper + skunk) + 1) + "% SPC (Smell Per Click)", font=("Arial", 20))
lbl3.place(x=450, y=400)
btn2=Button(window, text="Dirt (Cost " + str(helpercost+100) + "%) (+1% SPC)")
btn2.place(x=340, y=500)
btn3=Button(window, text="Skunk (Cost " + str(skunkcost + 1000) + "%) (+7% SPC)")
btn3.place(x=530, y=500)
midskibuybtn=Button(window, text="Mitski Songs (Cost " + str(midskicost + 10000) + "%) (+100% SPC)")
midskibuybtn.place(x=730, y=500)
savebtn=Button(window, text="Save")
savebtn.place(x=700, y=50)
alertlbl=Label(window, text="", font=("Arial", 15))
alertlbl.place(x=550, y=650)
loadbtn=Button(window, text="Load")
loadbtn.place(x=600, y=50)
#what is up with the achevement button's name
acvmtbtn=Button(window, text="Stats")
acvmtbtn.place(x=100, y=100)
numofhlp=Label(window, text=str(gourd) + " Dirt", font=("Arial", 15))
numofhlp.place(x=390, y=470)
numofsku=Label(window, text=str(int(skunk/7)) + " Skunk", font=("Arial", 15))
numofsku.place(x=530, y=470)
numofmidski=Label(window, text=str(int(midski))+" Midski Songs Playing",font=("Arial",15))
numofmidski.place(x=740, y=470)
#possible things are skunk or no shower
loadbtn.bind('<Button-1>', LoadGame)
btn3.bind('<Button-1>', BuySkunk)
btn.bind('<Button-1>', MyButtonClicked)
btn2.bind('<Button-1>', BuyHelper)
midskibuybtn.bind('<Button-1>',BuyMidski)
#btn2.bind('<Button-3>', Crash)
savebtn.bind('<Button-1>', SaveGame)
savebtn.bind('<Button-3>', AutosaveToggle)
acvmtbtn.bind('<Button-1>', OpenAchevements)
#having the mainloop right before the exit means the window closing closes the program
window.mainloop()
#unnecesary pause
#dnu = input("")
if autosave == True:
    SaveForRealzies()