############################
#       final_ToD.py       #
#     Conner Wilkinson     #
# The Trials of Daggervale #
############################
#imports
import pygame, sys, time, random, math, pickle
pygame.init()
#art credit to artstation and unsplash; various artists

#Sets game window size
gameDisplay=pygame.display.set_mode((500,400))
#ICON sets red star icon
icon = pygame.image.load('TDicon.png')
pygame.display.set_icon(icon)
#Sets caption of graphics window
pygame.display.set_caption("Trials of Daggervale")

#slowprints//invalidInputs defined
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1/200) # Final game-speed
    #time.sleep(1./1000) # Debug & test-speed
# ^ I chose (1./200) because it doesn't really slow the player down
def slowprint2(s2):
  for c in s2 + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1/10) # I chose (1./10) for all 'graphics'
def invalidInput():
    slowprint("<Your input is invalid>");
# ^ invalid user input function

#                                                                   PLAYER OBJ
class person:
    def __init__(self, name, caveLoc):
        self.name = "adventurer"
        self.caveLoc = "none"
        self.inventory = ["Pack", "Torch"]
        self.replay = False
class quests:
    def __init__(self, readyToPlay, doorCh):
        self.readyToPlay = False
        self.doorCh = False
        self.skeleKquest = False# These markers are turned true to allow
        self.caveWquest = False# the player to proceed through the game
        self.finalTquest = False
#                                                                  PLAYER OBJ
player = person("adventurer", "none",)# creation of the player as a person object
quests = quests("False", "False",)# creation of the quests object to hold quest markers
prompt = ">> "# prompt variable to accompany input sections so users know when to type
userDirChoice = False# setup variable for skeleton key section
#                                                                  >3 indep Variables
towerPuzzleDict = {1: {"name": "John", "age": "27", "sex": "male",},
                   2: {"name": "Marie", "age": "22", "sex": "female",},
                   3: {"name": "Al", "age": "39", "sex": "male",},
}

#################################################### PYGAME SECTION

def titleart():
  titleart = pygame.image.load("tdTITLE.png").convert()
  gameDisplay.blit(titleart, [0,0])#apply image to screen
  pygame.display.update()# paint screen one time
  pygame.event.wait()
def castleart():
  castleart = pygame.image.load("tdcastle.png").convert()
  gameDisplay.blit(castleart, [0,0])#apply image to screen
  pygame.display.update()# paint screen one time
  pygame.event.wait()
def forestart():
  # NORTH forest ART
  forestart = pygame.image.load("tdforest.png").convert()
  gameDisplay.blit(forestart, [0,0])#apply image to screen
  pygame.display.update()# paint screen one time
  pygame.event.wait()
def mtnart():
  # East mtn ART
  mtnart = pygame.image.load("tdmtn.png").convert()
  gameDisplay.blit(mtnart, [0,0])#apply image to screen
  pygame.display.update()# paint screen one time
  pygame.event.wait()
def caveart():
  # SOUTH cave ART
  caveart = pygame.image.load("tdcave.png").convert()
  gameDisplay.blit(caveart, [0,0])#apply image to screen
  pygame.display.update()# paint screen one time
  pygame.event.wait()
def riverart():
  # WEST river ART
  riverart = pygame.image.load("tdriver.png").convert()
  gameDisplay.blit(riverart, [0,0])#apply image to screen
  pygame.display.update()# paint screen one time
  pygame.event.wait()
def withgemart():
  #art for pedestal with skeletonkey
  withkeyart = pygame.image.load("tdsk.png").convert()
  gameDisplay.blit(withkeyart, [0,0])
  pygame.display.update()
  pygame.event.wait()
def alzhoon():
  tdalzhoonart = pygame.image.load("tdalzhoon.png").convert()
  gameDisplay.blit(tdalzhoonart, [0,0])#duringritual
  pygame.display.update()
  pygame.event.wait()
def alzhooncancel():
  tdcancel = pygame.image.load("tdcancel.png").convert()
  gameDisplay.blit(tdcancel, [0,0])#surpriseface
  pygame.display.update()
  pygame.event.wait()
def endingart():
  tdendingart = pygame.image.load("tdending.png").convert()
  gameDisplay.blit(tdendingart, [0,0])#endingthroneroom
  pygame.display.update()
  pygame.event.wait()
def cow0art():
  cow0art = pygame.image.load("tdcow0.png").convert()
  gameDisplay.blit(cow0art, [0,0])#mainCOWroom
  pygame.display.update()
  pygame.event.wait()
def cow1art():
  cow1art = pygame.image.load("tdcow1.png").convert()
  gameDisplay.blit(cow1art, [0,0])#fallroom
  pygame.display.update()
  pygame.event.wait()
def cow2art():
  cow2art = pygame.image.load("tdcow2.png").convert()
  gameDisplay.blit(cow2art, [0,0])#swordroom
  pygame.display.update()
  pygame.event.wait()
def cow3art():
  cow3art = pygame.image.load("tdcow3.png").convert()
  gameDisplay.blit(cow3art, [0,0])#redkeyroom
  pygame.display.update()
  pygame.event.wait()
def cow4art():
  cow4art = pygame.image.load("tdcow4.png").convert()
  gameDisplay.blit(cow4art, [0,0])#emptyroom
  pygame.display.update()
  pygame.event.wait()
def cow5art1():
  cow5art1 = pygame.image.load("tdcow51.png").convert()
  gameDisplay.blit(cow5art1, [0,0])#spiderssword
  pygame.display.update()
  pygame.event.wait()
def cow5art2():
  cow5art2 = pygame.image.load("tdcow52.png").convert()
  gameDisplay.blit(cow5art2, [0,0])#spidersnosword
  pygame.display.update()
  pygame.event.wait()
def cow6art():
  cow6art = pygame.image.load("tdgem.png").convert()
  gameDisplay.blit(cow6art, [0,0])#gemroom
  pygame.display.update()
  pygame.event.wait()
def towerart():
  towerart = pygame.image.load("tdtower.png").convert()
  gameDisplay.blit(towerart, [0,0])#towerexterior
  pygame.display.update()
  pygame.event.wait()

#####################################################################

#This is a dict used for flavor in the final zone of the game
#playerNameFunction for user name input
def playerNameFunc():
    slowprint("What is your name?")
    player.name = input(prompt)
    slowprint("Your name is " + player.name + "? Are you sure?")
    playerNameConfirm = input(prompt).lower()
    while playerNameConfirm != "yes":
        if playerNameConfirm == "no" or playerNameConfirm == "n":
            slowprint("What is your name, really?")
            player.name = input(prompt)
            slowprint("Your name is " + player.name + "? Are you sure?")
            playerNameConfirm = input(prompt).lower()
        else:
            invalidInput()
            slowprint("Your name is " + player.name + "? Are you sure?")
            playerNameConfirm = input(prompt).lower()
    slowprint("It is nice to meet you " + player.name + "!")
    choiceToPlay=0;
#playerReadyFunction to let the user choose when to begin the game
def playerReadyFunc():
    while quests.readyToPlay == False:
        slowprint("Are you ready to play, " + player.name + "? yes/no");
        choiceToPlay=input(prompt);
        if choiceToPlay.lower() == "yes" or choiceToPlay.lower() == "y":
                slowprint("Fantastic! Let us begin...");
                quests.readyToPlay = True
        elif choiceToPlay.lower() == "no" or choiceToPlay.lower() == "n":
                slowprint("Very well, the adventure can wait until you are ready, then.");
        else:
                invalidInput()
#replay y/n functions
def replayYes():
    player.name = "adventurer"
    player.caveLoc = "9"
    player.inventory = ["Pack", "Torch"]
    player.replay = False
    quests.readyToPlay = False
    quests.doorCh = False
    quests.skeleKquest = False
    quests.caveWquest = False
    quests.finalTquest = False
def replayNo():
    playerReplayInput="0";
    player.replay=True
    slowprint("Thank you, " + player.name + ", for playing 'The Trials of Daggervale!'")
#_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\
# vvv Cave functions LOCATIONS ERRATA vvv 3.2.5.6
    #READY TO PLAY
def SkeletonkeyFunc():
    withgemart()
    slowprint("You have obtained the Skeletonkey!")
    quests.skeleKquest = True
    player.inventory.append("Skeletonkey")
    player.caveLoc = "0"
    slowprint("Your inventory now contains:")
    print(player.inventory)
def noSkeletonkeyFunc():
    slowprint("The ritual dias is empty;");
    slowprint("The Skeletonkey is not here...");
    slowprint("You must continue searching, " + player.name + "!")

def SkeletonkeyHunt():
    while "Skeletonkey" not in player.inventory:
        slowprint(player.name + ", you have been summoned by the King Himself!");
        slowprint("He bids you come to the castle for a dangerous quest, the details he dare not share in a letter.")
        slowprint("You approach the King's Castle, after many days of travelling across the kingdom.")
        #Retry/Replay while loop begins
        playerReplayInput=0;
        slowprint("You are ushered into the castle, through the grand halls,")
        slowprint("...through the throne room, and into the campaign room beyond.")
        slowprint("The King stands regal and stoic, looking over a map of the small country with the castle at its center.")
        while quests.skeleKquest == False:
        #player empty inventory at beginning of the game
            # Skeletonkey's location randomly set each replay
            # N.EVER E.AT S.EA W.EED == N>E>S>W
            worldLocations = ["north", "east", "south", "west"]
            SkeletonkeyLoc = random.choice(worldLocations)
            print(SkeletonkeyLoc) #COMMENT THIS LINE OUT IN FINAL DRAFT
        # TELL THE PLAYER ABOUT THE Skeletonkey QUEST
            slowprint("The King pulls you aside:");
            slowprint("'The Court Wizard Alzhoon has betrayed us,' he whispers.")
            slowprint("In hushed tones he says, 'The fabled Skeletonkey, which opens the door to the hidden Cave of Wonders, has been stolen by Alzhoon and has been transported somewhere randomly within the kingdom.'");
            slowprint("'He has a barrier protecting the key when we first discovered it on the old swamp's ritual dias.'")
            slowprint("'You shall have to go into the kingdom and find where it has been moved to, and use this spell to break the barrier:'")
        # array // direction choice 1-4
            dirOptions=["North; into the Forest,", "East; into the Mountains,", "South; into the Caves,", "West; toward the Rivers."]
            for abcd in dirOptions:
                    slowprint(abcd);
        # direction choice and consequences // dir is my shorthand for direction
            choiceOfDir=0;
            userDirChoice=0;
            userDirChoice = False;
            while userDirChoice == False: #this loop keeps player in zone until they find the right key location
                    slowprint("When you have chosen a direction to go from here, " + player.name + ", type it and press the enter key.");
                    choiceOfDir=input(prompt);
                    if choiceOfDir.lower() == "north":
                        forestart()
                        userDirChoice = True
                        slowprint("You follow the well-trodden path which winds this way and that into the Kingswood.");
                        slowprint("For hours you course through the dense trees, dodging the dangerous flora and fauna.");
                        slowprint("At last you see the great central clearing, at its center a tall, white ritual dias...");
                        if choiceOfDir == SkeletonkeyLoc:
                            SkeletonkeyFunc()
                            quests.skeleKquest = True
                        if choiceOfDir != SkeletonkeyLoc:
                            noSkeletonkeyFunc()
                            userDirChoice = False
                    elif choiceOfDir.lower() == "east":
                        mtnart()
                        userDirChoice = True
                        slowprint("You climb, up and up,");
                        slowprint("...and up,");
                        slowprint("...and up...");
                        slowprint("Until the harsh winds and bright white frost leave you snowblind.")
                        slowprint("Finally, on the mountain's peak you see the distant ritual dias, a perfect tower built into the jagged horn.")
                        slowprint("You inch toward it along the ridge line and...")
                        if choiceOfDir == SkeletonkeyLoc:
                            SkeletonkeyFunc()
                            replayOption = True
                        if choiceOfDir != SkeletonkeyLoc:
                            noSkeletonkeyFunc()
                            userDirChoice = False
                    elif choiceOfDir.lower() == "south":
                        caveart()
                        userDirChoice = True
                        slowprint("The caves to the south are a terrible sight after many hours on the road.");
                        slowprint("The black maw screaming as wind gushes from its mouth, an awful scar in the hillside.");
                        slowprint("As you enter, your feet stick with mud, every step a battle, a trudge, an exhaustive march.");
                        slowprint("The tunnels snake through the earth and torchlight is only somewhat reliable, as you fight the unnatural winds...")
                        slowprint("...until...")
                        slowprint("You enter the great cavern at the center of this labyrinth. The black central room illuminated by burning braziers...")
                        slowprint("...at the room's heart, a lone white ritual dias stands like a singular broken tooth...")
                        if choiceOfDir == SkeletonkeyLoc:
                            SkeletonkeyFunc()
                        if choiceOfDir != SkeletonkeyLoc:
                            noSkeletonkeyFunc()
                            userDirChoice = False
                    elif choiceOfDir.lower() == "west":
                        userDirChoice = True
                        riverart()
                        slowprint("You follow the small stream from the castle toward the King's River.");
                        slowprint("The tributary leads you to the grand King's Bridge, and as you cross, you can see downriver...");
                        slowprint("The needle-thin island at the river's center, with the bone-white fang of the ritual dias at its center.");
                        slowprint("You jump into the water, and ride its current to the lone, long island to more closely inspect the dias...")
                        if choiceOfDir == SkeletonkeyLoc:
                            SkeletonkeyFunc()
                        if choiceOfDir != SkeletonkeyLoc:
                            noSkeletonkeyFunc()
                            userDirChoice = False
            #5b VVV waiting until player chooses a direction VVV
                    else:
                        invalidInput()
def room0():
    #starting room of cave
    player.caveLoc = "0"
    choiceOfDoor=0;
    caveReplay = False
    while caveReplay == False and quests.caveWquest == False:
        while quests.doorCh == False:
            cow0art()
            slowprint("Within the main cavern you find 6 doors cut into the rock;")
            doorOptions=["1: an oily wooden door", "2: a heavy iron door", "3: a wooden door", "4: a broken wooden door", "5: a cold iron door", "6: a heavy, intricate metal door"]
            for a in doorOptions:
                slowprint(a)
            slowprint("When you have chosen a door, " + player.name + ", type the number.")
            choiceOfDoor=input(prompt);
            if choiceOfDoor.lower() == "1":
                quests.doorCh = True
                if player.inventory.__contains__("Red Key"): #task 7
                    slowprint("You unlock the door with the Red Key.")
                    room1()
                else:
                    slowprint("This door is locked with a Red Skull painted on the door.")
                    quests.doorCh = False
            elif choiceOfDoor.lower() == "2":
                quests.doorCh = True
                room2()
                quests.doorCh = False
            elif choiceOfDoor.lower() == "3":
                quests.doorCh = True
                room3()
                quests.doorCh = False
            elif choiceOfDoor.lower() == "4":
                quests.doorCh = True
                room4()
                quests.doorCh = False
            elif choiceOfDoor.lower() == "5":
                quests.doorCh = True
                room5()
                if player.inventory.__contains__("Sword"):
                    quests.doorCh = False
                else:
                    quests.doorCh = True
            elif choiceOfDoor.lower() == "6":
                quests.doorCh = True
                room6()
            else:
                invalidInput()
        slowprint("Would you like to try the Cave quest again?") #simple replay loop to catch dead players
        playerCaveReplayInput=input(prompt);
        if playerCaveReplayInput.lower() == "yes" or playerCaveReplayInput.lower() == "y":#                        pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
            cavereplayYes()
        elif playerCaveReplayInput.lower() == "no" or playerCaveReplayInput.lower() == "n":
            if quests.caveWquest == True:
                slowprint("Very well, you continue on your quest and begin making your way to Alzhoon's Tower!")
                caveReplay = True
                quests.caveWquest = True
            elif quests.caveWquest == False:
                slowprint(player.name + ", you must gather the Power Gem to stop Alzhoon's plan!")
        else:
            invalidInput()
def cavereplayYes():
    player.caveLoc = "0"
    player.inventory = ["Pack", "Torch"]
    player.replay = False
    quests.readyToPlay = False
    quests.doorCh = False
    quests.skeleKquest = True
    quests.caveWquest = False
    quests.finalTquest = False
def room1():
    #trapped room - ends game
    #Task 5 ends game outright, no matter what gear player has
    player.caveLoc = "1"
    cow1art()
    slowprint("The door is unlocked, and you enter, torch held high.")
    slowprint("You walk through a long corridor, which winds this way and that...")
    slowprint("*VOOSH!*")
    slowprint("--The floor gives from beneath you, and you--")
    slowprint("<<< GAME OVER >>>")
def room2():
    #sword location, requires key1red  #task number 7
    player.caveLoc = "2"
    cow2art()
    slowprint("This room appears to have been an armory for the mercenaries that used to hide here.");
    slowprint("The walls bear empty armor and weapon racks.")
    if "Sword" not in player.inventory:
        slowprint("Though there is one thing of note left in here...")
        swordPickupFunc()
    else:
        slowprint("There is little else to discover in here.")
        slowprint("You exit the armory.");
# sword pickup functions
def swordPickupFunc():
    slowprint("In a rack on the wall,       /| ________________")
    slowprint("   you see a gleaming, O|===|* >________________>")
    slowprint("     untarnished sword.      \|")
    slowprint("The rack is locked with a small lock painted red...")
    while "Sword" not in player.inventory and "Red Key" in player.inventory:
        slowprint("Would you like to pick up the sword? yes/no");
        playerSwordPickupCh=input(prompt);
        if playerSwordPickupCh.lower() == "yes" or playerSwordPickupCh.lower() == "y":
            player.inventory.append("Sword")
            slowprint("Your inventory now contains:")
            print(player.inventory);
            slowprint("You exit the room with your new blade!")
            slowprint("Any monsters should be no problem now...")
            quests.doorCh = False
        elif playerSwordPickupCh.lower() == "no" or playerSwordPickupCh.lower() == "n":
            slowprint("Very well, you exit the room.");
            slowprint("There is little else to discover in there.")
            quests.doorCh = False
        else:
            invalidInput()
    if "Sword" not in player.inventory and "Red Key" not in player.inventory:
        slowprint("'I should find that key,' you think to yourself.")
        slowprint("There is little else to discover in here, you exit to the main cavern.")
        quests.doorCh = False
def room3():
    #key1 location
    player.caveLoc = "3"
    cow3art()
    slowprint("This room was some sort of barracks, long abandoned.")
    slowprint("Old cots and emptied trunks line the walls...")
    redKeyPickupFunc()
# red key pickup function
def redKeyPickupFunc():
    playerKey1Pickup = False
    while playerKey1Pickup == False and "Red Key" not in player.inventory:
        slowprint("The only thing of note is a Red Key, hanging from a hook on the wall.")
        slowprint("Would you like to take the Red Key? yes/no");
        playerKey1PickupCh=input(prompt);
        if playerKey1PickupCh.lower() == "yes" or playerKey1PickupCh.lower() == "y":
            player.inventory.append("Red Key")
            slowprint("Your inventory now contains:")
            print(player.inventory);
            slowprint("This should come in handy. You exit the room.")
            playerKey1Pickup = True
        elif playerKey1PickupCh.lower() == "no" or playerKey1PickupCh.lower() == "n":
            slowprint("Very well, you exit the room.");
            playerKey1Pickup = True
        else:
            invalidInput()
def room4():
    player.caveLoc = "4"
    cow4art()
    slowprint("This ransacked room was emptied long ago.")
    rectangleArea()
    slowprint("It may have been a larder of some kind, the supplies taken when the caves were abandoned.")
    slowprint("You find nothing left of any use here...")
def rectangleArea():
    length = float(input("Enter the length of the room: "))
    width = float(input("Enter the width of the room: "))
    rectArea = length * width
    print("The area of this room is: " + str(rectArea))
def room5():
    #key2 location, requires sword -- else ends game -giant spiders
    #Task 4/5/6/7
    player.caveLoc = "5"
    if player.inventory.__contains__("Sword"):
        cow5art1()
        slowprint("You fend off the Dire Spiders just barely, thanks to your blade and torch!")
        silverKeyPickupFunc()
    else:
        cow5art2()
        slowprint("You swing your torch desperately, trying to keep them at bay!")
        slowprint("The Dire Spiders descend quickly upon you, surrounding you until one of them lands a bite!")
        slowprint("The poison acts quickly, and you stumble and begin fading......")
        slowprint("...into the dark...")
        slowprint("<<< GAME OVER >>>")
# silver key
def silverKeyPickupFunc():
    playerKey2Pickup = False
    while playerKey2Pickup == False and "Silver Key" not in player.inventory:
        slowprint("Around the neck of a poor lost soul wrapped in web, is a small Silver Key on a necklace.")
        slowprint("Would you like to pick up the Silver Key? yes/no");
        playerKey2PickupCh=input(prompt);
        if playerKey2PickupCh.lower() == "yes" or playerKey2PickupCh.lower() == "y":
            player.inventory.append("Silver Key")
            slowprint("Your inventory now contains:")
            print(player.inventory);
            slowprint("This key should come in handy!")
            slowprint("Finding nothing else of note, you exit.")
            playerKey2Pickup = True
        elif playerKey2PickupCh.lower() == "no" or playerKey2PickupCh.lower() == "n":
            slowprint("Very well, you exit the room.");
            playerKey2Pickup = True
        else:
            invalidInput()
def room6():
    #power gems room, but requires key1 and key2
    #task number 3 if player has keys  #task number 5
    player.caveLoc = "6"
    slowprint("This door is locked with two keyholes; one large and painted red, the other small and shiny.")
    if player.inventory.__contains__("Red Key") and player.inventory.__contains__("Silver Key") :
        cow6art()
        slowprint("You open the door and have found the treasure room!")
        slowprint("You have discovered the secret horde of the Cave of Wonders!")
        slowprint("You now have the Gems of Power the King can use to protect the Kingdom!")
        quests.caveWquest = True
        player.inventory.append("Power Gem")
    else:
        slowprint("You cannot open this door without both the keys.")
        player.caveLoc = "0"
        quests.doorCh = False
def caveBeginArt():
    slowprint("You have heard of a great fortune also trapped within the Cave of Wonders;")
    slowprint("Once a hideout for travelling mercenaries, it has long been forgotten.")
    slowprint("It is night when you find the entrance to the cave, nestled deep in the mountains.")
    slowprint("You place the Skeletonkey into the great copper lock on the doorway, and as you turn it, the key is drawn into the door itself as it opens.")
# tower section, final zone in game
def towerStart():
    towerart()
    slowprint("You have entered the base of the evil wizard's tower:")
    slowprint("This appears to have been a cell block, but the cells are empty except for blood...")
    for a, b in towerPuzzleDict.items():
        print(a, b)
    slowprint("There is a large door magically sealed with a riddle, blocking your passage to the higher floors.")
    towerRiddle1 = False;
    while towerRiddle1 == False:
        slowprint("What walks on four legs in the morning, two at noon, and three at night?")
        riddle1response = input(prompt)
        if riddle1response.lower() == "man" or riddle1response.lower() == "human":
            towerRiddle1 = True
            slowprint("The door opens...")
        else:
            slowprint("The door does not move.")
# entire tower is cut up into these riddle loops^V^V^V
def towerFloor2():
    slowprint("You have entered the second floor of the tower:")
    slowprint("There is a large door magically sealed with a riddle, blocking your passage to the higher floors.")
    towerRiddle2 = False;
    while towerRiddle2 == False:
        slowprint("What belongs to you, but other people use it more than you?")
        riddle2response = input(prompt)
        if riddle2response.lower() == "name" or riddle2response.lower() == "your name":
            towerRiddle2 = True
            slowprint("The door opens...")
        else:
            slowprint("The door does not move.")
def towerFloor3():
    slowprint("You have entered the third floor of the tower:")
    slowprint("There is a large door magically sealed with a riddle, blocking your passage to the roof.")
    towerRiddle3 = False;
    while towerRiddle3 == False:
        slowprint("The more you take, the more you leave behind. What am I?")
        riddle3response = input(prompt)
        if riddle3response.lower() == "steps" or riddle3response.lower() == "footsteps":
            towerRiddle3 = True
            slowprint("The door opens...")
        else:
            slowprint("The door does not move.")
def towerRoof():
        slowprint("You ascend to the tower's roof, the site of Alzhoon's ritual!")
        alzhoon()
        alzhoonalive = False
        while alzhoonalive == False:
            slowprint("Will you activate the Power Gem?")
            killAlzhoon = input(prompt)
            if killAlzhoon.lower() == "yes" or killAlzhoon.lower() == "y":
                alzhooncancel()
                slowprint2("The Power Gem begins glowing brightly, the energies from Alzhoon's wicked spell are drawn into it!")
                slowprint2("   *     *     *     *   ")
                slowprint2("  * *   * *   * *   * *  ")
                slowprint2(" *   * *   * *   * *   * ")
                slowprint2("*     *     *     *     *")
                alzhoonalive = True
            else:
                slowprint("His wicked ritual continues! Daggervale is in danger!")
        quests.finalTquest = True
def FinalTowerQuest():
    towerStart()
    towerFloor2()
    towerFloor3()
    towerRoof()

# ^^^  functions LOCATIONS ERRATA ^^^ 3.2.5.6
#_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\

#Game framework is here: taking player theough the 3 stages of the game
def gameStart():
    global background
    #section for modifying playernames
        # load the previous score if it exists
    try:
        with open('score.dat', 'rb') as file:
            score = pickle.load(file)
    except:
        score = 0

    print("High score: %d" %score)
    titleart()
    playerNameFunc()
    playerReadyFunc()
    pygame.display.update()
    while player.replay == False:# may need to re-arrange the order of the 'while-loop quests'
        castleart()
        while quests.skeleKquest == False:
            SkeletonkeyHunt()# stage 1
            while quests.caveWquest == False:
                caveBeginArt()# stage 2
                cow0art()
                player.inventory.remove("Skeletonkey")
                slowprint(player.name + ", you check your supplies once more before entering:")
                print(player.inventory)
                slowprint("You enter the cave's main cavern after some few minutes of walking the tunnel to the outside.")
                room0()
                while quests.finalTquest == False:
                    FinalTowerQuest()# stage 3
    #/-\_/-\_/-\_/-\_/-\_/-\_GAME OCCURRING_/-\_/-\_/-\_/-\_/-\_/-\
    # vvv Replay options vvv
        endingart()
        slowprint("You have defeated the terrible Alzhoon and rescued Daggervale!")
        print("<<< YOU WIN >>>")
        slowprint("Would you like to play again?")
        playerReplayInput=input(prompt);
        if playerReplayInput.lower() == "yes" or playerReplayInput.lower() == "y":
            replayYes()
        elif playerReplayInput.lower() == "no" or playerReplayInput.lower() == "n":
            replayNo()
        else:
            invalidInput()

#Master start function:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            gameStart()
            score = 10;

# save the score
with open('score.dat', 'wb') as file:
    pickle.dump(score, file)