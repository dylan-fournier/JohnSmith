import time

myListStatic = [21, 9, 142, 39, 112, 96, 159, 132, 88, 94, 143, 125, 12, 129, 105, 63, 181, 45, 35, 104, 66, 183, 128, 72, 32, 174, 14, 91, 139, 60, 98, 176, 180, 198, 47, 146, 107, 160, 10, 136, 199, 27, 190, 123, 38, 36, 84, 50, 152, 191, 67, 44, 6, 25, 187, 62, 108, 33, 148, 155, 57, 103, 122, 178, 119, 26, 54, 120, 151, 168, 177, 154, 23, 169, 157, 51, 86, 97, 167, 188, 130, 200, 158, 150, 53, 162, 52, 141, 95, 43, 17, 49, 70, 153, 82, 93, 13, 5, 102, 163]
#myListStatic = [4,2]
myList = myListStatic.copy()
def bubble():
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
                break
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
numofloops = 100
timefinal = 0
for x in range(numofloops):
    time1 = time.time()
    myList=myListStatic.copy()
    while orderChecker() == False:
        bubble()
    time2 = time.time()
    timefinal = timefinal + (time2-time1)
    print(myList)
    print("done in "+ str(time2-time1))
print("That Bubblesort took "+str(timefinal/numofloops)+" Seconds, on average")
