#Rock, paper & scissors.
import random 

print("Rock, paper & scissors!")
print("\n1 =✊(Rock), 2 =✋(Paper) & 3 =✌️ (Scissors).")
print("\nElse input 4 for exit.")

player = 0
computer = 0

while player != 4:

  computer = random.randint(1,3)
  player = int(input("\nPlayer's Choice = "))

  if player == 4:
    break #for 'break' I had to refer Claude because before this the loop was not exiting in desired manner

  print("computers choice: " + str(computer))
  
  if player == computer:
    print("It's a draw")

  elif player == 1 and computer == 2:
    print("\nComputer wins.")

  elif player == 2 and computer == 3:
    print("\nComputer wins.")

  elif player == 3 and computer == 1:
    print("\nComputer wins.")

  else:
    print("Player Wins!")

print("You have Quit!")

