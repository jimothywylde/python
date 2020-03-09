import math
import sys
import time
import random

prompt = ">> "
playerDict = {
    "name" : "name",
    "class" : "wizard",
    "inventory": [],
}

def outputFunction(x):
    for c in x:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0001)


def invalidInput():
    print("invalid input")


outputFunction("Welcome to \'In The Castle Of The King!\'\n")
outputFunction("\nWhat is your name, young adventurer?")
name = input(prompt)
outputFunction("\nIt is nice to meet you, " + name +"\n")
outputFunction("\nAre you ready to play?")
playerReady = False
while playerReady == False:
    playerResponse = input(prompt).lower()
    if playerResponse == "yes":
        playerReady = True
    elif playerResponse == "no":
        outputFunction("Okay. I'll wait here")
    else:
        invalidInput()

locations = ["north", "south", "east", "west"]
newGame = True
while newGame == True:
    kingsLocation = random.choice(locations).lower()
    outputFunction(kingsLocation)
    outputFunction("")
    outputFunction("\nYou have been summoned by the King. He is behind one of the doors in this room and you must locate him\n")
    outputFunction("\nWhich door would you like to try? (North/South/East/West)")
    playerChoice = input(prompt).lower() 
    validInput = False
    while validInput == False:
        if playerChoice == "north":
            outputFunction("\nYou went North\n")
            if playerChoice == kingsLocation:
                outputFunction("You found the King!\n")
                validInput = True
            else:
                outputFunction("\nWhich door would you like to try? (North/South/East/West)")
                playerChoice = input(prompt).lower()
        elif playerChoice == "south":
            outputFunction("\nYou went South\n")
            if playerChoice == kingsLocation:
                outputFunction("You found the King!\n")
                validInput = True
            else:
                outputFunction("\nWhich door would you like to try? (North/South/East/West)")
                playerChoice = input(prompt).lower()
        elif playerChoice == "east":
            outputFunction("\nYou went East\n")
            if playerChoice == kingsLocation:
                outputFunction("You found the King!\n")
                validInput = True
            else:
                outputFunction("\nWhich door would you like to try? (North/South/East/West)")
                playerChoice = input(prompt).lower()
        elif playerChoice == "west":
            outputFunction("\nYou went West\n")
            if playerChoice == kingsLocation:
                outputFunction("You found the King!\n")
                validInput = True
            else:
                outputFunction("\nWhich door would you like to try? (North/South/East/West)")
                playerChoice = input(prompt).lower()
        else:
            invalidInput()
            playerChoice = input(prompt).lower()
    outputFunction("\nWould you like to play again?")
    playerResponse = input(prompt).lower()
    if playerResponse == "yes":
        outputFunction("Fantastic!\n")
    elif playerResponse == "no":
        outputFunction("\nWhat a shame. See you next time!")
        newGame = False
    else:
        outputFunction("Invalid Input")
        playerResponse = input(prompt).lower()




