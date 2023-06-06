import random
import time
from printWithoutNewline import prnt
import csv
random.seed()
global suitsList, cardIndicatorList, cardIndicatorListLong, chips
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
        if num == 1:
            return f"Ace of {self.cardsuit}"
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
        self.hasBlackjack = False

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
    def score(self):
        score = 0
        self.have11Ace = False
        aceCounter = 0
        for i in self.hand:
            if i.num > 10:
                score += 10
            elif i.num==1:
                aceCounter+=1
            else:
                score += i.num
        for i in range(aceCounter):
            if score + 11 < 21 and self.have11Ace == False:
                score += 11
                self.have11Ace = True
            else:
                score+=1
        if len(self.hand) == 2 and score == 21:
            self.hasBlackjack = True
        else:
            self.hadBlackjack = False
        return score

blackjackDeck = Deck()
blackjackDeck.shuffle()
human = BlackjackPlayer("Human")
dealer = BlackjackPlayer("Dealer")
try:
    with open('chips.csv', 'r') as file:
        reader = csv.reader(file)
        for column in reader:
            chips = int(column[0])
        file.close()
except:
    chips = 100

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
        for i in range(2):
            human.hand.append(blackjackDeck.draw())
            dealer.hand.append(blackjackDeck.draw())
        hit = True
        while hit == True:
            print("Dealer's Cards: "+ dealer.handStr() + " Score: " + str(dealer.score()))
            print()
            print("Your Cards: "+ human.handStr() + " Score: " + str(human.score()))
            print()
            if human.score() > 21:
                print("You Bust!")
                hit = False
            else:
                x = 1
                while x == 1:
                    try:
                        askHit = input("Hit or Stand? ")
                        if askHit != "Hit" and askHit != "Stand":
                            raise TypeError("Error")
                        if askHit == "Hit":
                            human.hand.append(blackjackDeck.draw())
                            hit=True
                        else:
                            hit=False
                        x = 0
                    except:
                        print("Must Be \"Hit\" or \"Stand\"")
        if dealer.score() > 21:
            print("\nDealer Stands")
            dealerHit = False
        else:
            dealerHit = True
        while dealerHit == True:
            print("Dealer's Cards: "+ dealer.handStr() + " Score: " + str(dealer.score()))
            print()
            print("Your Cards: "+ human.handStr() + " Score: " + str(human.score()))
            print()
            time.sleep(1)
            if dealer.score() > 21:
                print("Dealer Bust!")
                dealerHit=False
            else:
                if dealer.score() == 17 and dealer.has11Ace:
                    print("Dealer Hits")
                    print()
                    dealer.hand.append(blackjackDeck.draw())
                    dealerHit = True
                elif dealer.score() < 17:
                    print("Dealer Hits")
                    print()
                    dealer.hand.append(blackjackDeck.draw())
                    dealerHit = True
                else:
                    print("dealer Stands")
                    dealerHit = False
        #final score check
        if dealer.score() > 21 and human.score() > 21:
            print("Tie!")
            chips = chips + bet
        elif human.score() > 21:
            print("House Wins")
        elif dealer.score() >21:
            print("You WIn!")
            chips = chips + (bet*2)
        elif dealer.score() == human.score() and human.hasBlackjack == True and dealer.hasBlackjack == True:
            print("Tie!")
            chips = chips + bet
        elif dealer.score() == human.score() and human.hasBlackjack == True:
            print("you win")
            chips = chips + (bet*2)
        elif dealer.score() == human.score() and dealer.hasBlackjack == True:
            print("House Wins")
        elif dealer.score() > human.score():
            print("House Wins")
        elif human.score() > dealer.score():
            print("You Win")
            chips = chips + (bet*2)
        elif human.score()== dealer.score():
            print("Tie")
            chips = chips + bet
        for i in range(len(human.hand)):
            discardPile.append(human.hand.pop(0))
        for i in range(len(dealer.hand)):
            discardPile.append(dealer.hand.pop(0))
        print("You have "+str(chips)+" chips")
        print("Want to play again? (1/0)")
        try:
            playAgain = int(input())
        except:
            playAgain = 0
    except IndexError:
        for i in range(len(human.hand)):
            discardPile.append(human.hand.pop(0))
        for i in range(len(dealer.hand)):
            discardPile.append(dealer.hand.pop(0))
        print("Out of cards, Shuffling...\nDeck has been reset.\n")
        blackjackDeck.shuffle()

with open('chips.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([chips])
    file.close()
