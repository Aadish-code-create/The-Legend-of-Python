#Quiz Game 
import random

print("------------")
print("   Takken   ")
print("------------")

print("\nYou are King.")
print("Your opponent is Bryan Fury.")


print("\n1 = attack | 2 = block | 3 = heal | 4 = Quit ")

print("\nThe player with maximum HP will Win!")
print("Remember HP will decrease or ")
print("increase based on moves you play.")

king_hp = 100
bryan_hp = 100
king_move = 0
bryan_move = 0

print("\nTing-Ting-Ting")
print("Fight!")

while king_hp > 0 and bryan_hp > 0: #previously I used "while !=" for bryan, king and quit but then clude suggested that this wont help the loop end!

  king_move = int(input("\nEnter your move: "))
  bryan_move = random.randint(1,3)
  
  if king_move == 4:
    break
  
  if king_move == 1:
    print("You chose to Atack! 💥")
  elif king_move == 2:
    print("You chose to Block! 🛡️")
  elif king_move == 3:
    print("You chose to Heal! ❤️‍🩹")
  else: 
    print("Please input valid move.")

  if bryan_move == 1:
    print("Computer chose to Atack! 💥")
  elif bryan_move == 2:
    print("Computer chose to Block! 🛡️")
  else:
    print("Computer chose to Heal! ❤️‍🩹")

  if king_move == 1 and bryan_move == 1:
    king_hp = king_hp - 10
    bryan_hp = bryan_hp - 10 
  
  elif king_move == 1 and bryan_move in [2,3]:
    bryan_hp = bryan_hp - 10
  
  elif king_move == 2 and bryan_move == 1:
    king_hp = king_hp - 10
  
  elif king_move == 2 and bryan_move == 3:
    bryan_hp = bryan_hp - 10 
  
  elif king_move == 3 and bryan_move == 1:
    bryan_hp = bryan_hp - 10

  elif king_move == 3 and bryan_move == 2:
    king_hp = king_hp - 10

  elif king_move == 3 and bryan_move == 3:
    king_hp = king_hp + 10
    bryan_hp = bryan_hp + 10

  else:
    king_hp = king_hp 
    bryan_hp = bryan_hp

if king_move == 4:
  print("\nYou have quit!")
elif king_hp == 0:
  print("King Wins!")
else:
  print("Bryan Wins! Better Luck Next Time.")

