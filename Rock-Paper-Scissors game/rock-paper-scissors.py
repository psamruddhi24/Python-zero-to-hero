import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pictures = [rock,paper,scissors]

me = int(input("What do you choose? rock is 0,paper is 1 and scissors is 2 \n"))
if me == 0 or me == 1 or me == 2:
  print(pictures[me])
  
  computer = random.randint(0,2)
  print(pictures[computer])

  if me == computer:
    print("Its a draw")
  elif me == 0 and computer == 1:
    print("You lose")
  elif me == 0 and computer == 2:
    print("You win")
  elif me == 1 and computer == 0:
    print("You win")
  elif me == 1 and computer == 2:
    print("You lose")
  elif me == 2 and computer == 0:
    print("You lose")
  elif me == 2 and computer == 1:
    print("You win")
else:
  print("Invalid input, You lose!")
