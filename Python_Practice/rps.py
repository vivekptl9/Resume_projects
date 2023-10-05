# Better way to write comments..!
# *
#!
#?
# TODO: 
 # * ------------------------------------------------------------------------ * #
import sys
import random
 
print("")
playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper, \n3 for Scissors: \n\n ")
player = int(playerchoice)
if player < 1 | player > 3:
    sys.exit("You must enter 1,2,or 3.")
computerchoice = random.choice("123")
computer = int(computerchoice)
print(" ")
print("You chose " + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print(" ")
