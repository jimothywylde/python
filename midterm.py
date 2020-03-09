#__ midterm.py Conner Wilkinson
#imports
import sys
import time
import random
import math
#slowprints//invalidInputs defined
def slowprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    #time.sleep(1/200) # Final game-speed
    time.sleep(1./1000) # Debug & test-speed
# ^ I chose (1./200) because it doesn't really slow the player down
def slowprint2(s2):
  for c in s2 + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1/1000) # I chose (1./1000) for all 'graphics'
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
        self.readyToPlay = False
        self.doorCh = False
        self.skeleKquest = False
        self.caveWquest = False
        self.finalTquest = False
#                                                                  PLAYER OBJ
player = person("adventurer", "none",) #creation of the player as a person object
prompt = ">> "        #prompt variable to accompany input sections so users know when to type
userDirChoice = False #setup variable for skeleton key section

#                                                                  >3 indep Variables
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
    while player.readyToPlay == False:
        slowprint("Are you ready to play, " + player.name + "? yes/no");
        choiceToPlay=input(prompt);
        if choiceToPlay.lower() == "yes" or choiceToPlay.lower() == "y":
                slowprint("Fantastic! Let us begin...");
                player.readyToPlay = True
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
    player.readyToPlay = False
    player.doorCh = False
    player.skeleKquest = False
    player.caveWquest = False
    player.finalTquest = False
def replayNo():
    playerReplayInput="0";
    player.replay=True
    slowprint("Thank you, " + player.name + ", for playing 'The Trials of Daggervale!'")
#_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\
# vvv Cave functions LOCATIONS ERRATA vvv 3.2.5.6
    #READY TO PLAY
def SkeletonkeyFunc():
    slowprint2("  {F}  ")
    slowprint2(" _{b}_     ")
    slowprint2("  |||     ")
    slowprint2(" /|||\      ")
    slowprint("It floats within the protective barrier, and you are unable to pick it up.")
    slowprint("You retrieve the spellbook and recite the incantation:")
    slowprint2("   F   ")
    slowprint2(" _ b _ ")
    slowprint2("  |||  ")
    slowprint2(" /|||\ ")
    slowprint("You have obtained the Skeletonkey!")
    player.skeleKquest = True
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
        #ASCII CASTLE ART
        print("                                  |>>>")
        print("                                  |")
        print("                    |>>>      _  _|_  _         |>>>")
        print("                    |        |;| |;| |;|        |")
        print("                _  _|_  _    \\.    .  /    _  _|")
        print("               |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|")
        print("               \\..      /    ||;   . |    \\.    .  /")
        print("                \\.  ,  /     ||:  .  |     \\:  .  /")
        print("                 ||:   |_   _ ||_ . _ | _   _||:   |")
        print("                 ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |")
        print("                 ||:   ||.    .     .      . ||:  .|")
        print("                 ||: . || .     . .   .  ,   ||:   |       \,/")
        print("                 ||:   ||:  ,  _______   .   ||: , |            /`|")
        print("                 ||:   || .   /+++++++\    . ||:   |")
        print("                 ||:   ||.    |+++++++| .    ||: . |")
        print("              __ ||: . ||: ,  |+++++++|.  . _||_   |")
        print("     ____--`~    '--~~__|.    |+++++__|----~    ~`---,              ___")
        print("-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~~")
        #Retry/Replay while loop begins
        playerReplayInput=0;
        slowprint("You are ushered into the castle, through the grand halls,")
        slowprint("...through the throne room, and into the campaign room beyond.")
        slowprint("The King stands regal and stoic, looking over a map of the small country with the castle at its center.")
        while player.skeleKquest == False:
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
            while userDirChoice == False:
                    slowprint("When you have chosen a direction to go from here, " + player.name + ", type it and press the enter key.");
                    choiceOfDir=input(prompt);
                    if choiceOfDir.lower() == "north":
        #North; into the Forest,
                        userDirChoice = True
                        slowprint("You follow the well-trodden path which winds this way and that into the Kingswood.");
                        slowprint("For hours you course through the dense trees, dodging the dangerous flora and fauna.");
                        slowprint("At last you see the great central clearing, at its center a tall, white ritual dias...");
                        if choiceOfDir == SkeletonkeyLoc:
                            SkeletonkeyFunc()
                            player.skeleKquest = True
                        if choiceOfDir != SkeletonkeyLoc:
                            noSkeletonkeyFunc()
                            userDirChoice = False
                    elif choiceOfDir.lower() == "east":
        #East; into the Mountains
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
        #SOUTH = CAVES
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
        #WEST = rivers
                        userDirChoice = True
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
    #starting room
    player.caveLoc = "0"
    choiceOfDoor=0;
	caveReplay = False;
	while caveReplay == False and "Power Gem" not in player.inventory:
		while player.doorCh == False:
			slowprint("Within the main cavern you find 6 doors cut into the rock;")
			doorOptions=["1: an oily wooden door", "2: a heavy iron door", "3: a wooden door", "4: a broken wooden door", "5: a cold iron door", "6: a heavy, intricate metal door"]
			for a in doorOptions:
				slowprint(a)
			slowprint("When you have chosen a door, " + player.name + ", type the number.")
			choiceOfDoor=input(prompt);
			if choiceOfDoor.lower() == "1":
				player.doorCh = True
				if player.inventory.__contains__("Red Key"): #task 7
					slowprint("You unlock the door with the Red Key.")
					room1()
				else:
					slowprint("This door is locked with a Red Skull painted on the door.")
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
		slowprint("Would you like to try the Cave quest again?")
		playerCaveReplayInput=input(prompt);
		if playerCaveReplayInput.lower() == "yes" or playerCaveReplayInput.lower() == "y":#                        pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
			cavereplay()
		elif playerCaveReplayInput.lower() == "no" or playerCaveReplayInput.lower() == "n":
			cavereplayNo()
		else:
			invalidInput()
def cavereplayYes():
    player.caveLoc = "0"
    player.inventory = ["Pack", "Torch"]
    player.replay = False
    player.readyToPlay = False
    player.doorCh = False
    player.skeleKquest = True
    player.caveWquest = False
    player.finalTquest = False
def cavereplayNo():
    if "Power Gem" in player.inventory == True:
		slowprint("Very well, you continue on your quest and begin making your way to Alzhoon's Tower!")
	elif player.caveWquest == False:
		slowprint(player.name + ", you must gather the Power Gem to stop Alzhoon's plan!")
		
def room1():
    #trapped room - ends game
    #Task 5 ends game outright, no matter what gear player has
    player.caveLoc = "1"
    slowprint("The door is unlocked, and you enter, torch held high.")
    slowprint("You walk through a long corridor, which winds this way and that...")
    slowprint("*VOOSH!*")
    slowprint("--The floor gives from beneath you, and you--")
    slowprint2(" \ |      f")
    slowprint2("  \|       a")
    slowprint2(" /\|_       l")
    slowprint2("   0 \       l")
    slowprint2("|/\/\/\/\/\/\|")
    slowprint("<<< GAME OVER >>>")
def room2():
    #sword location, requires key1red  #task number 7
    player.caveLoc = "2"
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
    slowprint2("In a rack on the wall,       /| ________________")
    slowprint2("   you see a gleaming, O|===|* >________________>")
    slowprint2("     untarnished sword.      \|")
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
            player.doorCh = False
        elif playerSwordPickupCh.lower() == "no" or playerSwordPickupCh.lower() == "n":
            slowprint("Very well, you exit the room.");
            slowprint("There is little else to discover in there.")
            player.doorCh = False
        else:
            invalidInput()
    if "Sword" not in player.inventory and "Red Key" not in player.inventory:
        slowprint("'I should find that key,' you think to yourself.")
        slowprint("There is little else to discover in here, you exit to the main cavern.")
        player.doorCh = False
def room3():
    #key1 location
    player.caveLoc = "3"
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
    slowprint("This ransacked room was emptied long ago.")
    slowprint("It may have been a larder of some kind, the supplies taken when the caves were abandoned.")
    slowprint("You find nothing left of any use here...")
def room5():
    #key2 location, requires sword -- else ends game -giant spiders
    #Task 4/5/6/7
    player.caveLoc = "5"
    if player.inventory.__contains__("Sword"):
        spiders()
        slowprint("You fend off the Dire Spiders just barely, thanks to your blade and torch!")
        silverKeyPickupFunc()
    else:
        spiders()
        slowprint("You swing your torch desperately, trying to keep them at bay!")
        slowprint("The Dire Spiders descend quickly upon you, surrounding you until one of them lands a bite!")
        slowprint("The poison acts quickly, and you stumble and begin fading......")
        slowprint("...into the dark...")
        slowprint("<<< GAME OVER >>>")
def spiders():
    slowprint("Countless pinpoints of light begin reflecting back from the dark above...")
    slowprint("The skittering above draws louder, and closer!")
    slowprint2("They are   ____                      ,")
    slowprint2("         /---.'.__             ____//")
    slowprint2("    EYES!      '--.\      |    /.---'")
    slowprint2("          _______  \\         //")
    slowprint2("        /.------.\  \|      .'/  ______")
    slowprint2("       //  ___  \ \ ||/|\  //  _/_----.\__")
    slowprint2("      |/  /.-.\  \ \:|< >|// _/.'..\   '--'")
    slowprint2("   |     //   \'. | \'.|.'/ /_/ /  \\")
    slowprint2("        //     \ \_\/~ ' ~\-'.-'    \\")
    slowprint2("       //   |   '-._| :H: |'-.__  |  \\")
    slowprint2("      //           (/'==='\)'-._\     ||")
    slowprint2("   |  ||                        \\    \|")
    slowprint2("      ||                |        \\    '")
    slowprint2("      |/                          \\")
    slowprint2("                     |             ||")
    slowprint2("  It's a swarm of                   \\")
    slowprint2("         Dire Spiders!               '")
    slowprint("Countless eyes and wiry, hairy legs climbing down from the dark!")
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
    #Wins the game, but requires key1 and key2
    #task number 3 if player has keys  #task number 5
    player.caveLoc = "6"
    slowprint("This door is locked with two keyholes; one large and painted red, the other small and shiny.")
    if player.inventory.__contains__("Red Key") and player.inventory.__contains__("Silver Key") :
        slowprint("You open the door and have found the treasure room!")
        slowprint("You have discovered the secret horde of the Cave of Wonders!")
        slowprint2("   .    '    .")
        slowprint2(" .  _________  .")
        slowprint2(" _ /_|_____|_\ _")
        slowprint2("   '. \   / .'")
        slowprint2("     '.\ /.'")
        slowprint2("       '.'")
        slowprint("You now have the Gems of Power the King can use to protect the Kingdom!")
        player.caveWquest = True
    else:
        slowprint("You cannot open this door without both the keys.")
        player.caveLoc = "0"
        player.doorCh = False
def caveBeginArt():
    print("           .          .           .     .                .               .")
    print("  .      .      *           .       .          .                   .")
    print("                 .       .   . *     >>>>>>>               . ")
    print("  .       ____     .      . .    > >>>>>   .                  >>>>   .")
    print("         >>         .        .               .           >>>>>>> >>       .")
    print(" .   .  /WWWI; \  .       .    .  ____               .         .     .")
    print("  * >>>>>WWWII; \=====;    .     /WI; \   *    .        /\_             .")
    print("  .   /WWWWWII;..      >>>>. ___/WI;:. \     .        _/M; \    .   .")
    print("     /WWWWWIIIIi;..      \__/WWWIIII:.. \____ .   .  /MMI:  \   * .")
    print(" . _/WWWWWIIIi;;;:...:   ;\WWWWWWIIIII;.     \     /MMWII;   \    .  .     .")
    print("  /WWWWWIWIiii;;;.:.. :   ;\WWWWWIII;;;::     \___/MMWIIII;   \              .")
    print(" /WWWWWIIIIiii;;::.... :   ;|WWWWWWII;;::.:      :;IMWIIIII;:   \___     *")
    print("WWWWWWWWWIIIIIIIIIii;;::.;..;\WWWWWWWWIIIII;;..  :;IMIII;:::     :   \ ")
    print("WWWWWWWWWWWWWIIIIIIii;;::..;..;\WWWWWW[H]WWWIIII;::; :::::::::....:: \\ ")
    slowprint("You have heard of a great fortune also trapped within the Cave of Wonders;")
    slowprint("Once a hideout for travelling mercenaries, it has long been forgotten.")
    slowprint("It is night when you find the entrance to the cave, nestled deep in the mountains.")
    slowprint("You place the Skeletonkey into the great copper lock on the doorway, and as you turn it, the key is drawn into the door itself as it opens.")
def towerStart():
    print("")
def towerFloor2():
    print("")
def towerFloor3():
    print("")
def towerRoof():
    print("")
    player.finalTquest = True
def FinalTowerQuest():
    towerStart()
    towerFloor2()
    towerFloor3()
    towerRoof()
# ^^^ Cave functions LOCATIONS ERRATA ^^^ 3.2.5.6
#_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\_/-\
def gameStart():
    #section for modifying playernames
    playerNameFunc()
    playerReadyFunc()
    while player.replay == False:#may need to re-arrange the order of the 'while-loop quests'
        while player.skeleKquest == False:
            SkeletonkeyHunt()
            while player.caveWquest == False:
                caveBeginArt()
                player.inventory.remove("Skeletonkey")
                slowprint(player.name + ", you check your supplies once more before entering:")
                print(player.inventory)
                slowprint("You enter the cave's main cavern after some few minutes of walking the tunnel to the outside.")
                room0()
                while player.finalTquest == False
                    FinalTowerQuest()
    #/-\_/-\_/-\_/-\_/-\_/-\_GAME OCCURRING_/-\_/-\_/-\_/-\_/-\_/-\
    # vvv Replay options vvv
        slowprint("Would you like to play again?")
        playerReplayInput=input(prompt);
        if playerReplayInput.lower() == "yes" or playerReplayInput.lower() == "y":
            replayYes()
        elif playerReplayInput.lower() == "no" or playerReplayInput.lower() == "n":
            replayNo()
        else:
            invalidInput()
#Master start fucntion:
gameStart()
