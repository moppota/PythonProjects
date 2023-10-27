import random
CardTemplate = {

    "Ones":1,
    "Twos":2,
    "Threes":3,
    "Fours":4,
    "Fives":5,
    "Sixes":6,

    "Total of Upper Section":0,

    "3 of a kind":1,
    "4 of a kind":1,
    "Full House":1,
    "Small Straight":1,
    "Large Straight":1,
    "Yahtzee":1,
    "Chance":1,

    "Total of Lower Section":0,

    "Grand Total":0
} # defining the score card of Yahtzee as a dictionary, and will show players what their score is

listOfChoices = []

for v in CardTemplate:
    listOfChoices.append(v) #literally cant be assed to type out every option so I spent the same amount of time automating it. At least I can add stuff to the template if needed

class functionsNeeded:
    def __init__(self):
        self.card = CardTemplate #adding some self. variables

    def refreshTotals(self):
        i = 0
        upperTotalTemp,lowerTotalTemp,grandTotalTemp = 0,0,0
        for v in self.card.values(): # loops through every value in the dictionary, if its in the upper or lower section adds it to those totals and gives a grand total. 
            i += 1
            if i == 16:
                grandTotalTemp = upperTotalTemp+lowerTotalTemp
            if i == 15:
                continue
            if i < 7:
                upperTotalTemp += v
            elif  i > 7:
                lowerTotalTemp += v
            self.card["Total of Lower Section"] = lowerTotalTemp
            self.card["Total of Upper Section"] = upperTotalTemp
            self.card["Grand Total"] = grandTotalTemp
    def addValues(self, Type, Score):
        self.card[Type] = Score # updates the score of a specific value 

    def rollDice(self): # rolls dice and returns as a list. 
        dice = []
        for i in range(5):
            dice.append(random.randint(1,6))
        return dice
    
    def checkIfPossible(self, dice, score):
        if score not in listOfChoices:
            return False
        


    

        



