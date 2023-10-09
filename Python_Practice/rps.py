# Better way to write comments..!
# *
#!
#?
# TODO: 
 # * ------------------------------------------------------------------------ * #
# TODO: A basic program to make a Rock, Paper Scissor Game using python

#? Importing the libraries required for this program
import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    #playagain = True

    #while playagain:
        
    print (RPS(2)) #! Different ways to call class objects
    print (RPS.ROCK)
    print (RPS["ROCK"])
    print (RPS.ROCK.value)
    # sys.exit()

    print("")
    #? Variable defining the choice made by the player
    #?--------------------------------------------------------------------------------------
    playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, \n3 for Scissors: \n\n ")
    
    if playerchoice not in ["1","2","3"]:
        print ("You must enter 1, 2, or 3.")
        return play_rps()
    
    player = int(playerchoice)
    
    #? Variable defining the choice made by the computer
    #?-----------------------------------------------------------------------------------
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    
    #-------------------------------------------------------------------------------
    print("\nYou chose " + playerchoice + ".")
    print("Python chose " + computerchoice + ".\n")

    if player == 1 and computer ==3:
        print("🙌 You Win..🎉🎊")
    elif player == 2 and computer ==1:
        print("🙌 You Win..🎉🎊")
    elif player == 3 and computer ==2:
        print("🙌 You Win..🎉🎊")
    elif player == computer:
        print("😒 It's a Tie Game..!")
    else:
        print("🐍 Python Wins..🎉🎊")
    
    print("\nPlay again?")
    while True:
        playagain = input("\n Y for Yes or \n Q to quit\n\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()    
    else:
        print("\n Thank you for playing!")
        sys.exit("Bye  .! 🙋‍♂️")
play_rps()