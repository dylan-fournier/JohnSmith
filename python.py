print("hello world")
from datetime import datetime
def doInputs():
    global x
    global y
    try:
        x = int(input("how old are you? "))
        y = input("did you have your birthday yet this year? ")
    except ValueError:
       print("age must be integer")
z = int(datetime.now().year)
doInputs()
y = y.lower()
#print("debug "+ str(z))
if y == "y" or y == "yes":
    y = True
else:
    y = False
if y==True:
    a = z-x
else:
    a = z-x-1
print("your birthyear is "+ str(a))