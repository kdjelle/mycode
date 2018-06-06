#!/usr/bin/env python3

#importing functions from cheatdice
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

#assigning functions to cheater objects
cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

#running those cheater objects as ordinary players
cheater1.roll()
cheater2.roll()

#the cheating part
cheater1.cheat()
cheater2.cheat()

#displaying the results the results
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

#declaring the winner
if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")

else:
  print("Cheater 2 wins!")

