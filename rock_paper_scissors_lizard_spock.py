#Rock, paper, scissors, lizzard & spock

import random 
print("--------------------------------------")
print("Rock, Paper, Scissors, Lizard & Spock.")
print("--------------------------------------")

print("\n1.👊(rock), 2.🖐️ (paper), 3.✌️ (scissors)")
print("4.🫳 (lizzard), 5.🖖(spock), 6. Quit")

player = 0
computer = 0

while player != 6:

  player = int(input("\nPlease enter input: "))
  computer = random.randint(1,5)

  if player == 6:
    break

  print("Computer's choice: " + str(computer))

  if player == computer:
    print("It's a draw")
    
  elif player == 1 and computer in [2,5]:
    print("Computer wins!")

  elif player == 2 and computer in [3,4]:
    print("Computer wins!")

  elif player == 3 and computer in [1,5]:
    print("Computer wins!")

  elif player == 4 and computer in [1,3]:
    print("Computer wins!")

  elif player == 5 and computer in [2,4]:
    print("Computer wins!")

  else:
    print("You Win!")

print("You have quit!")
