totalEggs = 0
def doInputs():
    global chickenCount
    global eggsPerChicken
    try:
        chickenCount = int(input("how many chickens? "))
        eggsPerChicken = int(input("how many eggs does each chicken produce? "))
    except:
        print("both values must be numbers!")
        doInputs()
doInputs()
#mon
totalEggs += eggsPerChicken * chickenCount
#tues
chickenCount += 1
totalEggs += eggsPerChicken * chickenCount
#wed
chickenCount /= 2
totalEggs += eggsPerChicken * chickenCount
print("you have "+ str(int(totalEggs)) + " Eggs by wednesday.")