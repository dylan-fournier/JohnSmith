import time
import random
random.seed()
def orderChecker(myList):
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

#bubble sort
def bubble(myList):
        for i in range(len(myList)):
            if i == 0:
                pass
            else:
                if myList[i] >= myList[i-1]:
                    pass
                else:
                    temp = myList[i]
                    myList[i] = myList[i-1]
                    myList[i-1] = temp
                if i == len(myList):
                    return myList
def bubbleSort(myListStatic,numofloops=1):
    timefinal = 0
    myList =myListStatic
    for x in range(numofloops):
        time1 = time.time()
        myList=myListStatic.copy()
        while orderChecker(myList) == False:
            myList = bubble(myList)
        time2 = time.time()
        timefinal = timefinal + (time2-time1)
    return timefinal/numofloops

#bogosort
def bogoSort(myListStatic,numofloops=1):
    timefinal = 0
    myList=myListStatic.copy()
    for x in range(numofloops):
        time1 = time.time()
        myList=myListStatic.copy()
        while orderChecker(myList) == False:
            random.shuffle(myList)
        time2 = time.time()
        timefinal = timefinal + (time2-time1)
    return(timefinal/numofloops)