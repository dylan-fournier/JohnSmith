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
            "1":[0, False],
            "2":[0, False],
            "3":[0, False],
            "4":[0, False],
            "5":[0, False],
            "6":[0, False],
            "fullHouse":[0, False],
            "choice":[0, False],
            "4ofKind":[0, False],
            "smallStraight":[0, False],
            "largeStraight":[0, False],
            "yacht":[0, False]
        }
        self.topBonus = False
    def printScorecard(self):
        for i in self.scoreCard:
            prnt(i + ": " + str(self.scoreCard[i][0]))
            if str(self.scoreCard[i][1]) == True:
                prnt(" *")
            print()
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
def score(category):
    if category == 

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
        else:
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
            human.printScorecard()
            x = input("In which category do you want to place? ")
            score(x)
            



#for i in range(12):
playRound()