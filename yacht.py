import random
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
            "chance":0,
            "3ofKind":0,
            "4ofKind":0,
            "smallStraight":0,
            "largeStraight":0,
            "yacht":0
        }
        self.topBonus = False
    def __str__(self):
        return f"{self.scoreCard}"
A = Die()
B = Die()
C = Die()
D = Die()
E = Die()
human = Player()
print(human)
def playRound():
    pass



for i in range(12):
    pass