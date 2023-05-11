import random
import time
discardPile = []
global have11AceDealer, have11AceHuman
cardIndicatorList = ("J","Q","K")
have11AceHuman = False
have11AceDealer = False
random.seed()
chips = 100
global suitsList
suitsList = ("Spades", "Clubs", "Diamonds", "Hearts")
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
        for i in range(len(discardPile)):
            self.cardsList.append(discardPile[i])
        random.shuffle(self.cardsList)

    def draw(self):
        return self.cardsList.pop(0)

#init deck
blackjackDeck = Deck()
blackjackDeck.shuffle()
#init players
#init human
playAgain = 1
while playAgain == 1:
    try:
        x = 1
        while x == 1:
            try:
                bet = int(input("How much do you want to bet (Current Amount: "+ str(chips)+")? "))
                x = 0
            except:
                print("Must be number")
        chips = chips - bet
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
            elif i.num == 1:
                if dealerScore + 11 > 21:
                    dealerScore = dealerScore + 1
                else:
                    dealerScore = dealerScore + 11
            else:
                dealerScore = dealerScore + i.num
        if dealerScore == 21:
            perfectDealer = True
        else:
            perfectDealer= False
        for i in humanHand:
            if i.num > 10:
                humanScore = humanScore + 10
            elif i.num == 1:
                if humanScore +11 > 21:
                    humanScore = humanScore + 1
                else:
                    humanScore = humanScore + 11
            else:
                humanScore = humanScore + i.num
        if humanScore == 21:
            perfectHuman = True
        else:
            perfectHuman = False
        while hit == True:
            dealerStr = ""
            humanStr = ""
            dealerScore = 0
            humanScore = 0
            for i in dealerHand:
                if i.num > 10:
                    dealerStr = dealerStr + str(cardIndicatorList[i.num-11]) + " "
                    dealerScore = dealerScore + 10
                elif i.num == 1:
                    dealerStr=dealerStr + "A "
                    if dealerScore + 11 > 21:
                        dealerScore = dealerScore + 1
                    else:
                        have11AceDealer = True
                        dealerScore = dealerScore + 11 
                else:
                    dealerStr = dealerStr + str(i.num) + " "
                    dealerScore = dealerScore + i.num
            if dealerScore > 21 and have11AceDealer:
                dealerScore = dealerScore - 10
                have11AceDealer = False
            for i in humanHand:
                if i.num > 10:
                    humanStr = humanStr + str(cardIndicatorList[i.num-11]) + " "
                    humanScore = humanScore + 10
                elif i.num == 1:
                    humanStr = humanStr + "A "
                    if humanScore + 11 > 21:
                        humanScore = humanScore + 1
                    else:
                        have11AceHuman = True
                        humanScore = humanScore + 11
                else:
                    humanStr = humanStr + str(i.num) + " "
                    humanScore = humanScore + i.num
            
            print("Dealers cards: " + dealerStr+ " Score: " + str(dealerScore))
            print()
            if have11AceHuman == True and humanScore == 21:
                print("Your Cards: "+ humanStr + " Score: " + "BlackJack!")
            elif have11AceHuman == False:
                print("Your Cards: "+ humanStr + " Score: " + str(humanScore))
            else:
                print("Your Cards: "+ humanStr + " Score: Soft " + str(humanScore))
            print()
            if humanScore > 21 and have11AceHuman:
                humanScore = humanScore - 11
                have11AceHuman = False
            elif humanScore > 21:
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
                elif i.num == 1:
                    dealerStr=dealerStr + "A "
                    if dealerScore +11 > 21:
                        dealerScore = dealerScore + 1
                    else:
                        dealerScore = dealerScore + 11 
                else:
                    dealerStr = dealerStr + str(i.num) + " "
                    dealerScore = dealerScore + i.num
            if dealerScore > 21 and have11AceDealer:
                dealerScore = dealerScore - 10
                have11AceDealer = False
            for i in humanHand:
                if i.num > 10:
                    humanStr = humanStr + str(cardIndicatorList[i.num-11]) + " "
                    humanScore = humanScore + 10
                elif i.num == 1:
                    humanStr = humanStr + "A "
                    if humanScore +11 > 21:
                        humanScore = humanScore + 1
                    else:
                        have11AceHuman = True
                        humanScore = humanScore + 11
                else:
                    humanStr = humanStr + str(i.num) + " "
                    humanScore = humanScore + i.num
            if humanScore > 21 and have11AceHuman:
                humanScore = humanScore - 10
                have11AceHuman = False
            print("Dealers cards: " + dealerStr + " Score: " + str(dealerScore))
            print()
            if have11AceHuman == True and humanScore == 21:
                print("Your Cards: "+ humanStr + " Score: " + "BlackJack!")
            elif have11AceHuman == False:
                print("Your Cards: "+ humanStr + " Score: " + str(humanScore))
            else:
                print("Your Cards: "+ humanStr + " Score: Soft " + str(humanScore))
            print()
            time.sleep(1)
            if dealerScore > 21:
                print("Dealer Bust!")
                dealerHit=False
            else:
                if dealerScore == 17 and have11AceDealer:
                    print("Dealer Hits")
                    print()
                    dealerHand.append(blackjackDeck.draw())
                    dealerHit = True
                elif dealerScore <= 17:
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
            chips = chips + bet
        elif humanScore > 21:
            print("House Wins")
        elif dealerScore >21:
            print("You WIn!")
            chips = chips + (bet*2)
        elif dealerScore == humanScore and perfectHuman == True and perfectDealer == True:
            print("Tie!")
            chips = chips + bet
        elif dealerScore == humanScore and perfectHuman == True:
            print("you win")
            chips = chips + (bet*2)
        elif dealerScore == humanScore and perfectDealer == True:
            print("House Wins")
        elif dealerScore > humanScore:
            print("House Wins")
        elif humanScore > dealerScore:
            print("You Win")
            chips = chips + (bet*2)
        elif humanScore== dealerScore:
            print("Tie")
            chips = chips + bet
        for i in range(len(humanHand)):
            discardPile.append(humanHand.pop(0))
        for i in range(len(dealerHand)):
            discardPile.append(dealerHand.pop(0))
        print("You have "+str(chips)+" chips")
        print("Want to play again? (1/0)")
        try:
            playAgain = int(input())
        except:
            playAgain = 0
    except IndexError:
        for i in range(len(humanHand)):
            discardPile.append(humanHand.pop(0))
        for i in range(len(dealerHand)):
            discardPile.append(dealerHand.pop(0))
        print("Out of cards, Shuffling...")
        blackjackDeck.shuffle()
"""
    u should write a nice message here 
    taht way your ai will be kind :) 
    ex include:
    you lost, have a nice day 
    you are a loser but thats ok 
"""