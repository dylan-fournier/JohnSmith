import random
random.seed()
global suitsList
suitsList = ["Spades", "Clubs", "Diamonds", "Hearts"]
class Card:
    def __init__(self,suit,number):
        self.cardsuit=suit
        self.num=number
    def __str__(self):
        return f"{self.cardsuit},{self.num}"
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
        random.shuffle(self.cardsList)

    def draw(self):
        return self.cardsList.pop(0)


blackjackDeck = Deck()
print(blackjackDeck)