#Programming Assignment 7 'Cave of Objects'
#Conner Wilkinson
#exotic imports section
import sys
import time
import random
import math
#slowprint/slowprint2 defined
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    #time.sleep(1/75) # Final game-speed
    time.sleep(1./1000) # Debug & test-speed
# ^ I chose (1./75) because it doesn't really slow the player down
def slowprint2(s2):
  for c in s2 + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1/1000) # I chose (1./1000) for all 'graphics'
# v invalid input fucntion
def invalidInput():
    print("I'm sorry, I didn't quite understand that. <Your input is invalid>");
prompt = ">> "
#Task number 1 vvv player is an OBJECT, constructed from a PERSON class
class person:
    def __init__(self, name, location):
        self.name = "adventurer"
        self.location = "0"
        self.inventory = ["Backpack", "Torch"] #arrays still do not print from Objects
        self.replay = False
        self.ready = False
        self.doorCh = False
player = person("adventurer", "0",)

#_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\
# vvv Cave functions LOCATIONS ERRATA vvv 3.2.5.6
#Task 3; 6+1 rooms:
#Task 8 throughout code:
#Task 9; all rooms use functions
def room0():
    #starting room
    player.location = "0"
    choiceOfDoor=0;
    player.doorCh==False; #player.doorCh = False == player alive when exiting room
    while player.doorCh == False:
        print("Within the main cavern you find 6 doors cut into the rock;")
        doorOptions=["1: an oily wooden door", "2: a heavy iron door", "3: a wooden door", "4: a broken wooden door", "5: a cold iron door", "6: a heavy, intricate metal door"]
        for a in doorOptions:
            print(a)
        print("When you have chosen a door, " + player.name + ", type the number.")
        choiceOfDoor=input(prompt);
        if choiceOfDoor.lower() == "1":
            player.doorCh = True
            if player.inventory.__contains__("Red Key"): #task 7
                print("You unlock the door with the Red Key.")
                room1()
            else:
                print("This door is locked with a Red Skull painted on the door.")
                player.doorCh = False
        elif choiceOfDoor.lower() == "2":
            player.doorCh = True
            room2()
            player.doorCh = False
        elif choiceOfDoor.lower() == "3":
            player.doorCh = True
            room3()
            player.doorCh = False
        elif choiceOfDoor.lower() == "4":
            player.doorCh = True
            room4()
            player.doorCh = False
        elif choiceOfDoor.lower() == "5":
            player.doorCh = True
            room5()
            if player.inventory.__contains__("Sword"):
                player.doorCh = False
            else:
                player.doorCh = True
        elif choiceOfDoor.lower() == "6":
            player.doorCh = True
            room6()
        else:
            invalidInput()

def room1():
    #trapped room - ends game
    #Task 5 ends game outright, no matter what gear player has
    player.location = "1"
    print("The door is unlocked, and you enter, torch held high.")
    print("You walk through a long corridor, which winds this way and that...")
    print("*VOOSH!*")
    print("--The floor gives from beneath you, and you--")
    print("   f")
    print("    a")
    print("     l")
    print("      l")
    print("_________")
    print("<<< GAME OVER >>>")

def room2():
    #sword location, requires key1red  #task number 7
    player.location = "2"
    print("This room appears to have been an armory for the mercenaries that used to hide here.");
    print("The walls bear empty armor and weapon racks.")
    if "Sword" not in player.inventory:
        print("Though there is one thing of note left in here...")
        swordPickupFunc()
    else:
        print("There is little else to discover in here.")
        print("You exit the armory.");

#task 6 sword / Task 8
def swordPickupFunc():
    print("In a rack on the wall,       /| ________________")
    print("   you see a gleaming, O|===|* >________________>")
    print("     untarnished sword.      \|")
    print("The rack is locked with a small lock painted red...")
    while "Sword" not in player.inventory and "Red Key" in player.inventory:
        print("Would you like to pick up the sword? yes/no");
        playerSwordPickupCh=input(prompt);
        if playerSwordPickupCh.lower() == "yes" or playerSwordPickupCh.lower() == "y":
            player.inventory.append("Sword")
            print("Your inventory now contains:")
            print(player.inventory);
            print("You exit the room with your new blade!")
            print("Any monsters should be no problem now...")
            player.doorCh = False
        elif playerSwordPickupCh.lower() == "no" or playerSwordPickupCh.lower() == "n":
            print("Very well, you exit the room.");
            print("There is little else to discover in there.")
            player.doorCh = False
        else:
            invalidInput()
    if "Sword" not in player.inventory and "Red Key" not in player.inventory:
        print("'I should find that key,' you think to yourself.")
        print("There is little else to discover in here, you exit to the main cavern.")
        player.doorCh = False


def room3():
    #key1 location
    player.location = "3"
    print("This room was some sort of barracks, long abandoned.")
    print("Old cots and emptied trunks line the walls...")
    redKeyPickupFunc()

#task 6 red key
def redKeyPickupFunc():
    playerKey1Pickup = False
    while playerKey1Pickup == False and "Red Key" not in player.inventory:
        print("The only thing of note is a Red Key, hanging from a hook on the wall.")
        print("Would you like to take the Red Key? yes/no");
        playerKey1PickupCh=input(prompt);
        if playerKey1PickupCh.lower() == "yes" or playerKey1PickupCh.lower() == "y":
            player.inventory.append("Red Key")
            print("Your inventory now contains:")
            print(player.inventory);
            print("This should come in handy. You exit the room.")
            playerKey1Pickup = True
        elif playerKey1PickupCh.lower() == "no" or playerKey1PickupCh.lower() == "n":
            print("Very well, you exit the room.");
            playerKey1Pickup = True
        else:
            invalidInput()


def room4():
    player.location = "4"
    print("This ransacked room was emptied long ago.")
    print("It may have been a larder of some kind, the supplies taken when the caves were abandoned.")
    print("You find nothing left of any use here...")

def room5():
    #key2 location, requires sword -- else ends game -giant spiders
    #Task 4/5/6/7
    player.location = "5"
    if player.inventory.__contains__("Sword"):
        spiders()
        print("You fend off the Dire Spiders just barely, thanks to your blade and torch!")
        silverKeyPickupFunc()
    else:
        spiders()
        print("You swing your torch desperately, trying to keep them at bay!")
        print("The Dire Spiders descend quickly upon you, surrounding you until one of them lands a bite!")
        print("The poison acts quickly, and you stumble and begin fading......")
        print("...into the dark...")
        print("<<< GAME OVER >>>")

def spiders():
    print("Countless pinpoints of light begin reflecting back from the dark above...")
    print("The skittering above draws louder, and closer!")
    print("They are   ____                      ,")
    print("         /---.'.__             ____//")
    print("    EYES!      '--.\      |    /.---'")
    print("          _______  \\         //")
    print("        /.------.\  \|      .'/  ______")
    print("       //  ___  \ \ ||/|\  //  _/_----.\__")
    print("      |/  /.-.\  \ \:|< >|// _/.'..\   '--'")
    print("   |     //   \'. | \'.|.'/ /_/ /  \\")
    print("        //     \ \_\/~ ' ~\-'.-'    \\")
    print("       //   |   '-._| :H: |'-.__  |  \\")
    print("      //           (/'==='\)'-._\     ||")
    print("   |  ||                        \\    \|")
    print("      ||                |        \\    '")
    print("      |/                          \\")
    print("                     |             ||")
    print("  It's a swarm of                   \\")
    print("         Dire Spiders!               '")
    print("Countless eyes and wiry, hairy legs climbing down from the dark!")


#task 6 silver key
def silverKeyPickupFunc():
    playerKey2Pickup = False
    while playerKey2Pickup == False and "Silver Key" not in player.inventory:
        print("Around the neck of a poor lost soul wrapped in web, is a small Silver Key on a necklace.")
        print("Would you like to pick up the Silver Key? yes/no");
        playerKey2PickupCh=input(prompt);
        if playerKey2PickupCh.lower() == "yes" or playerKey2PickupCh.lower() == "y":
            player.inventory.append("Silver Key")
            print("Your inventory now contains:")
            print(player.inventory);
            print("This key should come in handy!")
            print("Finding nothing else of note, you exit.")
            playerKey2Pickup = True
        elif playerKey2PickupCh.lower() == "no" or playerKey2PickupCh.lower() == "n":
            print("Very well, you exit the room.");
            playerKey2Pickup = True
        else:
            invalidInput()

def room6():
    #Wins the game, but requires key1 and key2
    #task number 3 if player has keys  #task number 5
    player.location = "6"
    print("This door is locked with two keyholes; one large and painted red, the other small and shiny.")
    if player.inventory.__contains__("Red Key") and player.inventory.__contains__("Silver Key") :
        print("You open the door and have found the treasure room!")
        print("You have discovered the secret horde of the Cave of Wonders!")
        print("   .    '    .")
        print(" .  _________  .")
        print(" _ /_|_____|_\ _")
        print("   '. \   / .'")
        print("     '.\ /.'")
        print("       '.'")
        print("<<< YOU WIN! >>>")
    else:
        print("You cannot open this door without both the keys.")
        player.location = "0"
        player.doorCh = False


# ^^^ Cave functions LOCATIONS ERRATA ^^^ 3.2.5.6
#_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\
def replayYes():
    player.inventory = ["Backpack", "Torch"]
    player.location = "0"
    player.replay = False
    player.doorCh = False

def replayNo():
    playerReplayInput="0";
    player.replay=True
    print("Thank you, " + player.name + ", for playing 'Cave of Wonders!'")

def playerReadyFunc():
    while player.ready == False:
        print("Are you ready to enter the Cave? yes/no");
        choiceToPlay=input(prompt);
        if choiceToPlay.lower() == "yes" or choiceToPlay.lower() == "y":
                print("Fantastic! Let us begin...");
                player.ready = True
        elif choiceToPlay.lower() == "no" or choiceToPlay.lower() == "n":
                print("Very well, the Cave can wait until you are ready, then.");
        else:
                invalidInput()

def playerNameFunc():
    print("What is your name?")
    player.name = input(prompt)
    print("Your name is " + player.name + "? Are you sure?")
    playerNameConfirm = input(prompt).lower()
    while playerNameConfirm != "yes":
        if playerNameConfirm == "no" or playerNameConfirm == "n":
            print("What is your name, really?")
            player.name = input(prompt)
            print("Your name is " + player.name + "? Are you sure?")
            playerNameConfirm = input(prompt).lower()
        else:
            invalidInput()
            print("Your name is " + player.name + "? Are you sure?")
            playerNameConfirm = input(prompt).lower()
    print("It is nice to meet you " + player.name + "!")
    choiceToPlay=0;
#ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def game():
    print("Welcome, " + player.name + ", to 'Cave of Wonders!'")
    print("           .          .           .     .                .       .")
    print("  .      .      *           .       .          .                       .")
    print("                 .       .   . *                      . ")
    print("  .       ____     .      . .            .                          .  ")
    print("         >>         .        .               .                             .")
    print(" .   .  /WWWI; \  .       .    .  ____               .         .     .         ")
    print("  *    /WWWWII; \=====;    .     /WI; \   *    .        /\_             .")
    print("  .   /WWWWWII;..      \_  . ___/WI;:. \     .        _/M; \    .   .         .")
    print("     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .")
    print(" . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .")
    print("  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .")
    print(" /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *")
    print("WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :   \   ")
    print("WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWW(_)WWIIII;::; :::::::::.....::   \\")
    #section for modifying playernames
    playerNameFunc()
    playerReadyFunc()
    # WHILE LOOP until the player states they are ready to init game
    while player.replay == False:
        while player.location == "0":
            #---- TASK 7 --- Game runs on function
            print("You have heard of a great fortune trapped within the Cave of Wonders;")
            print("Once a hideout for travelling mercenaries, it has long been forgotten.")
            print("It is night when you find the entrance to the cave, nestled deep in the mountains.")
            print(player.name + ", you check your supplies once more before entering:")
            print(player.inventory)
            print("You enter the cave's main cavern after some few minutes of walking the tunnel to the outside.")
            room0()
    #/-\_/-\_/-\_/-\_/-\_/-\_GAME OCCURRING_/-\_/-\_/-\_/-\_/-\_/-\
        print("Would you like to play again?")
        playerReplayInput=input(prompt);
        if playerReplayInput.lower() == "yes" or playerReplayInput.lower() == "y":
            replayYes()
        elif playerReplayInput.lower() == "no" or playerReplayInput.lower() == "n":
            replayNo()
        else:
            invalidInput()

#Master start fucntion, task 7:
game()
