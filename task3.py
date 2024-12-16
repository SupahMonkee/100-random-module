'''
Rock Paper Scissors
Create the classic "Rock, Paper Scissors Game"
'''

import random

opp = random.randint(0,2)

if opp == 0:
    oppchoice = "Rock"
elif opp == 1:
    oppchoice = "Paper"
elif opp == 2:
    oppchoice = "Scissors"

me = (input('Rock, Paper, or Scissors? '))

if "Rock" in me:
    mechoice = "Rock"
elif "Paper" in me:
    mechoice = "Paper"
elif "Scissors" in me:
    mechoice = "Scissors"

if mechoice == "Rock" and oppchoice == "Rock":
    print(f'The computer picked {oppchoice}, you tied!')

if mechoice == "Rock" and oppchoice == "Paper":
    print(f'The computer picked {oppchoice}, you lost!')

if mechoice == "Rock" and oppchoice == "Scissors":
    print(f'The computer picked {oppchoice}, you won!')

if mechoice == "Paper" and oppchoice == "Rock":
    print(f'The computer picked {oppchoice}, you won!')

if mechoice == "Paper" and oppchoice == "Paper":
    print(f'The computer picked {oppchoice}, you tied!')

if mechoice == "Paper" and oppchoice == "Scissors":
    print(f'The computer picked {oppchoice}, you lost!')

if mechoice == "Scissors" and oppchoice == "Rock":
    print(f'The computer picked {oppchoice}, you lost!')

if mechoice == "Scissors" and oppchoice == "Paper":
    print(f'The computer picked {oppchoice}, you won!')

if mechoice == "Scissors" and oppchoice == "Scissors":
    print(f'The computer picked {oppchoice}, you tied!')

#done