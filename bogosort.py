import random
import time
global myList
global myListStatic
random.seed()
myListStatic = [2,1,3,4,5,6,7,8,9,17,18,19,20]
#myListStatic = [1,3,2]
def bogoSort():
    random.shuffle(myList)
def orderChecker():
    for i in range(len(myList)):
        if i == 0:
            pass
        else:
            if myList[i] >= myList[i-1]:
                pass
            else:
                return False
            if i == len(myList):
                return True
timefinal = 0
#woah
numofloops = 20
#woah
myList=myListStatic.copy()
for x in range(numofloops):
    time1 = time.time()
    myList=myListStatic.copy()
    while orderChecker() == False:
        bogoSort()
    time2 = time.time()
    timefinal = timefinal + (time2-time1)
    print("done in "+ str(time2-time1))
print("That Bogosort took "+str(timefinal/numofloops)+" Seconds, on average")
