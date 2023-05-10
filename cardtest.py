import random
import time
cardIndicatorList = ("J","Q","K")
random.seed()
chips = 100
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

#init deck
blackjackDeck = Deck()
blackjackDeck.shuffle()
"""
bet = input("How much do you want to bet (Current Amount: "+ str(chips)+")? ")
"""
#init players
#init human
humanHand=[] 

for i in range(2):
    humanHand.append(blackjackDeck.draw())
#init dealer
dealerHand = []
for i in range(2):
    dealerHand.append(blackjackDeck.draw())
hit = True
dealerScore = 0
humanScore = 0
for i in dealerHand:
    if i.num > 10:
        dealerScore = dealerScore + 10
    else:
        dealerScore = dealerScore + i.num
if dealerScore == 21:
    perfectDealer = True
for i in humanHand:
    if i.num > 10:
        humanScore = humanScore + 10
    else:
        humanScore = humanScore + i.num
if humanScore == 21:
    perfectHuman = True
while hit == True:
    dealerStr = ""
    humanStr = ""
    dealerScore = 0
    humanScore = 0
    for i in dealerHand:
        if i.num > 10:
            dealerStr = dealerStr + str(cardIndicatorList[i.num-11]) + " "
            dealerScore = dealerScore + 10
        else:
            dealerStr = dealerStr + str(i.num) + " "
            dealerScore = dealerScore + i.num
    for i in humanHand:
        if i.num > 10:
            humanStr = humanStr + str(cardIndicatorList[i.num-11]) + " "
            humanScore = humanScore + 10
        else:
            humanStr = humanStr + str(i.num) + " "
            humanScore = humanScore + i.num
    
    print("Dealers cards: " + dealerStr+ " Score: " + str(dealerScore))
    print()
    print("Your Cards: "+ humanStr+" Score: " + str(humanScore))
    print()
    if humanScore > 21:
        print("You Bust!")
        hit = False
    else:
        askHit = input("Hit or Stand? ")
        if askHit == "Hit":
            humanHand.append(blackjackDeck.draw())
            hit=True
        else:
            hit=False
if dealerScore > 21:
    print("\nDealer Stands")
    dealerHit = False
else:
    dealerHit = True
while dealerHit == True:
    dealerStr = ""
    humanStr = ""
    dealerScore = 0
    humanScore = 0
    for i in dealerHand:
        if i.num > 10:
            dealerStr = dealerStr + str(cardIndicatorList[i.num-11]) + " "
            dealerScore = dealerScore + 10
        else:
            dealerStr = dealerStr + str(i.num) + " "
            dealerScore = dealerScore + i.num
    for i in humanHand:
        if i.num > 10:
            humanStr = humanStr + str(cardIndicatorList[i.num-11]) + " "
            humanScore = humanScore + 10
        else:
            humanStr = humanStr + str(i.num) + " "
            humanScore = humanScore + i.num
    
    print("Dealers cards: " + dealerStr+ " Score: " + str(dealerScore))
    print()
    print("Your Cards: "+ humanStr+" Score: " + str(humanScore))
    print()
    time.sleep(1)
    if dealerScore > 21:
        print("Dealer Bust!")
        dealerHit=False
    else:
        if dealerScore < 17:
            print("Dealer Hits")
            print()
            dealerHand.append(blackjackDeck.draw())
            dealerHit = True
        else:
            print("dealer Stands")
            dealerHit = False

#final score check
if dealerScore > 21 and humanScore > 21:
    print("Tie!")
elif humanScore > 21:
    print("House Wins")
elif dealerScore >21:
    print("You WIn!")
elif dealerScore == humanScore and perfectHuman == True:
    print("you win")
elif dealerScore == humanScore and perfectDealer == True:
    print("House Wins")
elif dealerScore > humanScore:
    print("House Wins")
elif humanScore > dealerScore:
    print("You Win")
