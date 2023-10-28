import YahtzeeInPythonModule
import time

newGame = YahtzeeInPythonModule.functionsNeeded()
options = YahtzeeInPythonModule.listOfChoices
running = True # variables setup
diceRoll = [] # needs to be up here
diceToRoll = 5 # needs to be up here as well

print("Before we start, here are your choices (For what to do with your dice roll),\nand please enter them exactly as shown:")
print(options)
print("\n") # telling players this is how I want them to say where the score should go under

while running == True: # main loop
    diceToRoll = 5 # First roll is always 5, re rolls can change it so its reset up here
    diceRoll = [] # resetting list before each roll
    for i in range(2): # last stage is to add a way to choose which dice you want to re roll, will add soon
        input("Press enter to roll dice")
        diceRoll = diceRoll + newGame.rollDice(diceToRoll)

        print("Here is your roll, Ordered numerically: ")
        diceRoll.sort()
        print(diceRoll)
        print("\n") # when enter is pressed, rolls dice and shows player
        playerInput = input("Would you like to roll again? y/n.   Type r to reroll certain dice. ")
        if playerInput != "n":
            x = False
            if playerInput == "r": # if its a reroll of specific numbers, X is true so it initiates the re roll loop below
                x = True
            elif playerInput == "y": # if re roll is generic (all 5 dice), resets the list, X is false so loop below isnt triggered
                diceRoll = []
            n = 0
            while x:
                whichDice = input("Which dice in the list would you like to re roll? Please type numbers (e.g. 1, 5, 6) you want to reroll. type 'n' to stop rerolling") 
                if whichDice == "n": # breaks loop if they have re rolled all they want 
                    print(n)
                    diceToRoll = n
                    x = False
                else:
                    n += 1 # adds one to the amount of dice need to be re rolled
                    diceRoll.remove(int(whichDice)) # removes that list from our dice rolled list
        else:   
            break # if its n breaks the for i in range loop as they dont want any more rerolls
    isOptionValid = True
    while isOptionValid:
        PlayerChoice = input("What would you like to do? (Please enter exactly as requested at the beginning)") # asks for their option
        if (PlayerChoice in options) == True: # if its not in the list asks them to re roll it.
            checkIfTrue = newGame.checkIfPossibleAndGetValue(diceRoll, PlayerChoice) # calls the function to get a tuple of Bool, Int, Bool is whether what you chose is possible and Int is the score it gives
            if checkIfTrue[0] == True:
                options.remove(PlayerChoice) # each option can only be used once, removes it from the list so if they try to call again the in options check on line 47 returns a false
                newGame.addValues(PlayerChoice, checkIfTrue[1]) # calls the function to update the score 
                newGame.refreshTotals() # refreshes the Upper total, Lower total and Grand total
                print("Success, Added to your score. \n")
                print(newGame.card) # shows card
                print("\n")
                isOptionValid = False # if the option is valid, adds the score to that option and removes it from list since 
            else:
                PlayerChoice = input("That is not a valid option, Please enter again. \nWhat would you like to do? (Please enter exactly as requested at the beginning)")
    if len(options) == 0:
        print("Well done, you have completed the game. Here is your ScoreCard: \n")
        newGame.refreshTotals()
        print(newGame.card) # in Yahtzee, you can only use each option once 
        break
    else:
        print("Alright, Next turn:")
        





