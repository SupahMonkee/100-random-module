'''
Create a list that contains a deck of cards.
Shuffle and deal 5 card hands to 2 different players.  You may want to make use of the list commands we have previously explored to remove cards when they have been dealt to players.
'''
import math, os, random

deck = ["AS", "AD", "AC", "AH", "2S", "2D", "2C", "2H", "3S", "3D", "3C", "3H", "4S", "4D", "4C", "4H", "5S", "5D", "5C", "5H", "6S", "6D", "6C", "6H", "7S", "7D", "7C", "7H", "8S", "8D", "8C", "8H", "9S", "9D", "9C", "9H", "10S", "10D", "10C", "10H", "JS", "JD", "JC", "JH", "QS", "QD", "QC", "QH", "KS", "KD", "KC", "KH"]

x = 0
p1 = []
p2 = []
random.shuffle(deck)
for i in range(5):
    p1.append(deck[0])
    del deck[0]
for i in range(5):
    p2.append(deck[0])
    del deck[0]
    
print(p1)
print(p2)
print(deck)

#done