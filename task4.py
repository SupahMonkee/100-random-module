'''
Dungeons and Dragons Character Generator
In Dungeons and Dragons, players roll 3 dice to generate statistics for their characters.  The statistics recorded are:
strength
intelligence
wisdom
dexterity
constitution
charisma
Create a character generator that generates a character's statistics
'''

import math, os, random

os.system('cls')
print('-------------------------------------------------------')
print('  Welcome to Dungeons and Dragons Character Generator')
print('-------------------------------------------------------')
charname = (input('Enter the name of your character: '))

x = 0

while x == 0:
    strength = (random.randrange(3,61))
    intelligence = (random.randrange(3,61))
    wisdom = (random.randrange(3,61))
    dexterity = (random.randrange(3,61))
    constitution = (random.randrange(3,61))
    charisma = (random.randrange(3,61))
    age = (random.randrange(0,101))

    os.system('cls')

    print(f"{charname}'s stats:")
    print("--------------------")
    print(f"Strength: {strength}")
    print(f"Intelligence: {intelligence}")
    print(f"Wisdom: {wisdom}")
    print(f"Dexterity: {dexterity}")
    print(f'Constitution: {constitution}')
    print(f'Charisma: {charisma}')
    print(f'Age: {age}')

    stillalive = random.randrange(0,101)

    if stillalive > 99:
        print('Status: Dead')
        print('Cause of Death: Simon')
    elif stillalive < 100:
        stillalive = True


    if age > 49 and age < 69 and stillalive == True:
        status = random.randrange(1,5)
        if status < 5:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    if age >= 69 and age < 89 and stillalive == True:
        status = random.randrange(1,3)
        if status < 3:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    if age >= 89 and stillalive == True:
        status = random.randrange(1,3)
        if status < 2:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    print('')
    input('Press Enter to Reroll')