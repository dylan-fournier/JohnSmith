import pickle
global temptotal
temptotal = 0
def checkout():
    scanLoop = True
    while scanLoop:
        barcodeIn = input("? ")
        if barcodeIn == str(0):
            scanLoop = False
        else:
            try:
                temptotal = temptotal + database[barcodeIn].price
            except:
                print("item does not exist")
        print("Total Price: $"+str(temptotal))

class item():
    def __init__(self,name,price):
        self.name = name
        self.price = float(price)
    def __str__(self):
        key = [k for k, v in database.items() if v == self][0]
        return f"name:{self.name} | code: {key} | Price:{self.price} "
try:
    with open('database of barcodes.pkl', 'rb') as f:
        database = pickle.load(f)
except:
    database = {

    }  

mainLoop = True

while mainLoop:
    print("0. Exit \n1. Add Code \n2. Print List of Codes\n3. Checkout \n4. Remove Code")
    firstIn = int(input("? "))
    if firstIn == 0:
        mainLoop = False
    elif firstIn == 1:
        tempbarcode = input("Scan the Barcode now\n? ")
        print("Name of this item?")
        tempname = input("? ")
        print("price of this item")
        tempprice = float(input("? "))
        try:
            database[tempbarcode]
            print("this code already exists, overwrite?")
            x = input("y/n ? ")
            if x == "y":
                database[tempbarcode] = item(tempname,tempprice)
            else:
                pass
        except:
            database[tempbarcode] = item(tempname,tempprice)
    elif firstIn == 2:
        print()
        for i in database:
            print(database[i])
        print()
    elif firstIn == 3:
        temptotal = 0
        checkout()
    elif firstIn == 4:
        x = input("Barcode? ")
        try:
            print(database[x].name + " Removed")
            database.pop(x)
        except:
            print("Not in database yet")
    else:
        temptotal = 0
        barcodeIn = firstIn
        try:
            temptotal = temptotal + database[barcodeIn].price
        except:
            print("item does not exist")
        print("Total Price: $"+str(temptotal))
        checkout()
with open('database of barcodes.pkl', 'wb') as f:
    pickle.dump(database, f)