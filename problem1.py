'''
Advanced Dungeons and Dragons
optional rolling systems include:
a) roll 4 dice, discard the lowest
b) roll 3 dice, reroll 1's.
Add these as options to your D&D Character Statistics Generator
'''

import math, os, random, time

os.system('cls')
print('-------------------------------------------------------')
print('  Welcome to Dungeons and Dragons Character Generator')
print('-------------------------------------------------------')
charname = (input('Enter the name of your character: '))


x = 0

while x == 0:
    os.system('cls')
    print('Which rolling system would you like to use?')
    print('For original, type "1"') 
    print('For option a, type "2"') 
    print('For option b, type "3"') 
    try:
        choice = int(input())
        if choice > 0 and choice < 4:
            x = choice
        else:
            print('You didn\'t make a correct selection.')
            time.sleep(3)
    except:
        print('You didn\'t make a correct selection.')
        time.sleep(3)

while x == 1:
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
        print('Cause of Death: Falling Piano')
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

while x == 2:
    str1 = [random.randrange(1,20), random.randrange(1,20), random.randrange(1,20), random.randrange(1,20),]
    int1 = [random.randrange(1,20), random.randrange(1,20), random.randrange(1,20), random.randrange(1,20),]
    wis1 = [random.randrange(1,20), random.randrange(1,20), random.randrange(1,20), random.randrange(1,20),]
    dex1 = [random.randrange(1,20), random.randrange(1,20), random.randrange(1,20), random.randrange(1,20),]
    con1 = [random.randrange(1,20), random.randrange(1,20), random.randrange(1,20), random.randrange(1,20),]
    cha1 = [random.randrange(1,20), random.randrange(1,20), random.randrange(1,20), random.randrange(1,20),]
    age1 = [random.randrange(1,20), random.randrange(1,20), random.randrange(1,20), random.randrange(1,20),]
    list.sort(str1)
    del str1[0]
    str2 = sum(str1)
    list.sort(int1)
    del int1[0]
    int2 = sum(int1)
    list.sort(wis1)
    del wis1[0]
    wis2 = sum(wis1)
    list.sort(dex1)
    del dex1[0]
    dex2 = sum(dex1)
    list.sort(con1)
    del con1[0]
    con2 = sum(con1)
    list.sort(cha1)
    del cha1[0]
    cha2 = sum(cha1)
    list.sort(age1)
    del age1[0]
    age2 = sum(age1)

    os.system('cls')

    print(f"{charname}'s stats:")
    print("--------------------")
    print(f"Strength: {str2}")
    print(f"Intelligence: {int2}")
    print(f"Wisdom: {wis2}")
    print(f"Dexterity: {dex2}")
    print(f'Constitution: {con2}')
    print(f'Charisma: {cha2}')
    print(f'Age: {age2}')

    stillalive = random.randrange(0,101)

    if stillalive > 99:
        print('Status: Dead')
        print('Cause of Death: Falling Piano')
    elif stillalive < 100:
        stillalive = True


    if age2 > 49 and age2 < 69 and stillalive == True:
        status = random.randrange(1,5)
        if status < 5:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    if age2 >= 69 and age2 < 89 and stillalive == True:
        status = random.randrange(1,3)
        if status < 3:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    if age2 >= 89 and stillalive == True:
        status = random.randrange(1,3)
        if status < 2:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    print('')
    input('Press Enter to Reroll')

while x == 3:
    str1 = [random.randrange(2,21), random.randrange(2,21), random.randrange(2,21)]
    int1 = [random.randrange(2,21), random.randrange(2,21), random.randrange(2,21)]
    wis1 = [random.randrange(2,21), random.randrange(2,21), random.randrange(2,21)]
    dex1 = [random.randrange(2,21), random.randrange(2,21), random.randrange(2,21)]
    con1 = [random.randrange(2,21), random.randrange(2,21), random.randrange(2,21)]
    cha1 = [random.randrange(2,21), random.randrange(2,21), random.randrange(2,21)]
    age1 = [random.randrange(2,21), random.randrange(2,21), random.randrange(2,21)]
    str2 = sum(str1)
    int2 = sum(int1)
    wis2 = sum(wis1)
    dex2 = sum(dex1)
    con2 = sum(con1)
    cha2 = sum(cha1)
    age2 = sum(age1)
    os.system('cls')

    print(f"{charname}'s stats:")
    print("--------------------")
    print(f"Strength: {str2}")
    print(f"Intelligence: {int2}")
    print(f"Wisdom: {wis2}")
    print(f"Dexterity: {dex2}")
    print(f'Constitution: {con2}')
    print(f'Charisma: {cha2}')
    print(f'Age: {age2}')

    stillalive = random.randrange(0,101)

    if stillalive > 99:
        print('Status: Dead')
        print('Cause of Death: Falling Piano')
    elif stillalive < 100:
        stillalive = True


    if age2 > 49 and age2 < 69 and stillalive == True:
        status = random.randrange(1,5)
        if status < 5:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    if age2 >= 69 and age2 < 89 and stillalive == True:
        status = random.randrange(1,3)
        if status < 3:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    if age2 >= 89 and stillalive == True:
        status = random.randrange(1,3)
        if status < 2:
            print('Status: Alive')
        else:
            print('Status: Dead')
            print('Cause of Death: Old Age')

    print('')
    input('Press Enter to Reroll')

#done