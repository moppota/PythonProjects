import random
CardTemplate = {

    "Ones":0,
    "Twos":0,
    "Threes":0,
    "Fours":0,
    "Fives":0,
    "Sixes":0,

    "Total of Upper Section":0,

    "3 of a kind":0,
    "4 of a kind":0,
    "Full House":0,
    "Small Straight":0,
    "Large Straight":0,
    "Yahtzee":0,
    "Chance":0,

    "Total of Lower Section":0,

    "Grand Total":0
} # defining the score card of Yahtzee as a dictionary, and will show players what their score is

scoreOfCard = {
    "Ones":1,
    "Twos":2,
    "Threes":3,
    "Fours":4,
    "Fives":5,
    "Sixes":6,

    "Full House": 25,
    "Small Straight": 30,
    "Large Straight": 40,
    "Yahtzee": 50,
} # These options have a set amount of points, so I will just call them from here anmd it allows me to loop stuff

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

    def rollDice(self, number): # rolls dice and returns as a list. 
        dice = []
        for i in range(number):
            dice.append(random.randint(1,6))
        return dice
    
    def checkIfPossibleAndGetValue(self, dice, score): # checking if the option given is legal with the dice roll and gives the value
        x = 0
        if score not in listOfChoices: # if its not in list of choices just return false, function shouldnt be called if its not in their anyway
            return False, 0
        else:
            for v in scoreOfCard: # checking the ones, twos, threes etc. 
                x+=1
                if v == score and x < 7 and dice.count(scoreOfCard[score]) != 1: # loops through the score dictionary until option is reached, check if the roll has any numbers of the specified one in it 
                    returnValue = dice.count(scoreOfCard[score]) * scoreOfCard[score]
                    return True, returnValue
                if x > 7: # above 7 we just stop the loop since this was not one of the chosen options
                    break
            match score:
                case "3 of a kind": # checks if any number in the roll is repeated 3 or more times
                    for i in range(6):
                        if dice.count(i+1) >= 3:
                            return True, sum(dice)
                        else:
                            if i == 5:
                                return False, 0
                case "4 of a kind": # checks if any number in the roll is repeated 4 or more times
                    for i in range(6):
                        if dice.count(i+1) >= 4:
                            return True, sum(dice)
                        else:
                            if i == 5:
                                return False, 0
                case "Full House":
                    isThreeofakind = False # if both of these end up being true, its a full house
                    isPair = False
                    for i in range(6):
                        if dice.count(i+1) == 3:
                            isThreeofakind = True
                            break
                    for i in range(6):
                        if dice.count(i+1) == 2:
                            isPair = True
                            break
                    if isThreeofakind and isPair:
                        return True, scoreOfCard[score]
                    else:
                        return False, 0
                case "Small Straight": # loops through list and sees how many are in a row, if 4 or more, its valid
                    sortedDice = dice.sort()
                    amountInARow = 0
                    for i in range(6):
                        if i == 0:
                            pass
                        else:
                            if (dice[i] - 1) == dice[i-1]:
                                amountInARow += 1
                            else:
                                amountInARow = 0
                    if amountInARow >= 4:
                        return True, scoreOfCard[score]
                    else:
                        return False, 0
                case "Large Straight": # same as above but it needs 5 in a row
                    sortedDice = dice.sort()
                    amountInARow = 0
                    for i in range(6):
                        if i == 0:
                            pass
                        else:
                            if (dice[i] - 1) == dice[i-1]:
                                amountInARow += 1
                            else:
                                amountInARow = 0
                    if amountInARow >= 5:
                        return True, scoreOfCard[score]
                    else:
                        return False, 0
                case "Yahtzee": # Since its sorted and at least 5 need to match, the second option in the list would always be the one thats yahtzee. Just check if the count of that is higher than 5
                    newList = dice.sort()
                    if newList.count(newList[1]) == 5:
                        return True, scoreOfCard[score]
                    else:
                        return False, 0
                case "Chance": #its always possible (only once along with everything else), just return value of everything
                    return True, sum(dice)




                    
                    
                        


        


    

        



