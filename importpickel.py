#Testfile tuples formatting strigns

import pickle

# Get Name
#name = input("What is your name?: ")

#Dump name
#pickle.pump(name, open( "save.sav", "wb") )

#Load file and print name
name = pickle.load(  open( "save.sav", "rb" ) )
print(name)