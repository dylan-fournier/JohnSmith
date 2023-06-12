import random
from printWithoutNewline import prnt
random.seed()
class Die:
    def __init__(self):
        self.number = 1
        self.hold = False
    def __str__(self):
        return f"{self.number}"
    def roll(self):
        self.number = random.randint(1,6)
class Player:
    def __init__(self):
        self.scoreCard = {
            "1": 0,
            "2":0,
            "3":0,
            "4":0,
            "5":0,
            "6":0,
            "fullHouse":0,
            "choice":0,
            "4ofKind":0,
            "smallStraight":0,
            "largeStraight":0,
            "yacht":0
        }
        self.topBonus = False
    def printScorecard(self):
        for i in self.scoreCard:
            print(i + ": " + str(self.scoreCard[i]))
        print()
    def __str__(self):
        return f"{self.scoreCard}"
A = Die()
B = Die()
C = Die()
D = Die()
E = Die()
human = Player()
dice = (A,B,C,D,E)

def playRound():
    for turn in range(3):
        holding = True
        for i in dice:
            if turn == 0:
                i.hold = False
            if i.hold == False:
                i.roll()
        if turn < 2:
            while holding == True:
                prnt("Values: ")
                for i in dice:
                    prnt(str(i)+" ")
                    
                print()
                print("Key:\t0 1 2 3 4")
                prnt("Hold:   ")
                for i in dice:
                    if i.hold == True:
                        prnt("* ")
                    else:
                        prnt("  ")
                print()
                x = input("Which do you want to hold? (int, \"roll\",\"card\")")
                if x == "roll":
                    break
                elif x == "Card":
                    human.printScorecard()
                else:
                    x = int(x)
                    dice[x].hold = not dice[x].hold
            



#for i in range(12):
playRound()