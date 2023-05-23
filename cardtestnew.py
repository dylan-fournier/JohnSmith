import random
from printWithoutNewline import prnt
random.seed()
global suitsList, cardIndicatorList
suitsList = ("Spades", "Clubs", "Diamonds", "Hearts")
cardIndicatorList = ("J","Q","K")
cardIndicatorListLong = ("Jack","Queen","King")

discardPile = []

class Card:
    def __init__(self,suit,number):
        self.cardsuit=suit
        self.num=number
    def __str__(self):
        num = self.num
        if num > 10:
            num = num - 11
            return f"{cardIndicatorListLong[num]} of {self.cardsuit}"
        return f"{self.num} of {self.cardsuit}"
class Deck:
    def __init__(self):
        self.cardsList = []
        for i in range(4):
            suit = suitsList[i]
            for j in range(13):
                self.cardsList.append(Card(suit,j+1))
    def __str__(self):
        templist = []
        for i in self.cardsList:
            templist.append(f"{i}")
        return str(templist)
    def shuffle(self):
        for i in range(len(discardPile)):
            self.cardsList.append(discardPile[i])
        random.shuffle(self.cardsList)
    def draw(self):
        return self.cardsList.pop(0)

class BlackjackPlayer:
    def __init__(self,name="Player"):
        self.name = name
        self.hand = []
        self.has11Ace = False
        self.Perfect = False

    def __str__(self):
        templist = []
        for i in self.hand:
            templist.append(f"{i}")
        return self.name +" has: "+ str(templist)
    def handStr(self):
        strtemp = ""
        for i in self.hand:
            if i.num == 1:
                temp = "A"
            elif i.num >10:
                temp = cardIndicatorList[i.num-11]
            else:
                temp = str(i.num)
            
            strtemp = strtemp + temp + " "
        return strtemp

cards = Deck()
cards.shuffle()
human = BlackjackPlayer("Human")
dealer = BlackjackPlayer("Dealer")
for i in range(2):
    human.hand.append(cards.draw())
    dealer.hand.append(cards.draw())
print(dealer)
print(human)
