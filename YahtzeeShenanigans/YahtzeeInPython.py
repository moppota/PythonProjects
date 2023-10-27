import YahtzeeInPythonModule
import time

newGame = YahtzeeInPythonModule.functionsNeeded()
options = YahtzeeInPythonModule.listOfChoices
running = True # variables setup

print("Before we start, here are your choices (For what to do with your dice roll),\nand please enter them exactly as shown:")
print(options)
print("\n") # telling players this is how I want them to say where the score should go under

while running == True: # main loop
    input("Press enter to roll dice")
    diceRoll = newGame.rollDice()
    print("Here is your roll, Ordered numerically: ")
    diceRoll.sort()
    print(diceRoll)
    print("\n") # when enter is pressed, rolls dice and shows player
    while True:
        PlayerChoice = input("What would you like to do? (Please enter exactly as requested at the beginning)")
        if (PlayerChoice in options) == True:
            options.remove(PlayerChoice)
            print("Success, Added to your score. \n")
            newGame.refreshTotals()
            print(newGame.card)
            print("\n")
            break # if the option is valid, adds the score to that option and removes it from list since 
        else:
            print("Not a valid option. Try again.\n ")
    if len(options) == 0:
        print("Well done, you have completed the game. Here is your ScoreCard: \n")
        newGame.refreshTotals()
        print(newGame.card) # in Yahtzee, you can only use each option once 
        break
    else:
        print("Alright, Next turn:")
        





