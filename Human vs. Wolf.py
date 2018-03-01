import pygame
import time
import random
import pickle

class player:
    def __init__(self):
        self.hp = 100
        self.hpMax = 100
        self.defense = 10
        self.attack = 5
    def hit(self, hp):
        self.hp -= hp
    def heal(self, hp):
        self.hp += hp
    def lvlUp(self, level):
        self.defense += level
        self.hpMax += 20

human = player()
wolf = player()

def Human():
    human.heal(5)
    if wolf.hp >= 0:
        human.hit(15)
    print("Human HP: ", human.hp)

def Wolf():
    wolf.heal(10)
    if human.hp >= 0:
        wolf.hit(16)
    print("Wolf HP: ", wolf.hp)

game = True

def run():
    while game == True:
        Human()
        Wolf()
        if human.hp == 0:
            break
        elif wolf.hp == 0:
            break
        time.sleep(1)
run()

##outFile = open('HvW.txt', 'wb')
##pickle.dump(wolf.hp, outFile)
##outFile.close()

inFile = open('HvW.txt', 'rb')
newList = pickle.load(inFile)
print(newList)
