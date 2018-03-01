import random
import pygame
import time
import pickle

clock = pygame.time.Clock()

class player:
    def __init__(self):
        self.hp = 100
        self.hpMax = 100
        self.defense = 10
        self.attack = 5
        self.guns = 0
        self.ammo = 0
        self.food = 0
        self.water = 0
    def hit(self, hp):
        self.hp -= hp
    def heal(self, hp):
        self.hp += hp
    def lvlUp(self, level):
        self.defense += level
        self.hpMax += 20
        

survivor = player()

items = ["Gun", "Ammo", "Food", "Water"]

def inventory(collectedItem):
    invent = []
    if collect == True:
        invent.extend(collectedItem)

    time.sleep(1)
    print(invent)

def timer():
    dt = datetime.datetime.now()
    dt_HM = (dt.hour, dt.minute)

    if dt_HM == (1, 0):
        print ("Yes")
    elif dt_HM == (2, 0):
        print ("Yes")
    elif dt_HM == (3, 0):
        print ("Yes")
    elif dt_HM == (4, 0):
        print ("Yes")
    elif dt_HM == (5, 0):
        print ("Yes")
    elif dt_HM == (6, 0):
        print ("Yes")
    elif dt_HM == (7, 0):
        print ("Yes")
    elif dt_HM == (8, 0):
        print ("Yes")
    elif dt_HM == (9, 0):
        print ("Yes")
    elif dt_HM == (10, 0):
        print ("Yes")
    elif dt_HM == (11, 0):
        print ("Yes")
    elif dt_HM == (12, 0):
        print ("Yes")
    elif dt_HM == (13, 0):
        print ("Yes")
    elif dt_HM == (14, 0):
        print ("Yes")
    elif dt_HM == (15, 0):
        print ("Yes")
    elif dt_HM == (16, 0):
        print ("Yes")
    elif dt_HM == (17, 0):
        print ("Yes")
    elif dt_HM == (18, 0):
        print ("Yes")
    elif dt_HM == (19, 0):
        print ("Yes")
    elif dt_HM == (20, 0):
        print ("Yes")
    elif dt_HM == (21, 0):
        print ("Yes")
    elif dt_HM == (22, 0):
        print ("Yes")
    elif dt_HM == (23, 0):
        print ("Yes")
    elif dt_HM == (24, 0):
        print ("Yes")
    else:
        print ("No")
    

def gameLoop():
    collectedItem = ""
    play = True

    while play == True:
        #Add the following to Survivalist as a function
        found = random.choice(items)

        if found == "Gun":
            survivor.guns += 1
        elif found == "Ammo":
            survivor.ammo += 1
        elif found == "Food":
            survivor.food += 1
        elif found == "Water":
            survivor.water += 1

        time.sleep(1)
        print("------------------------------------------------")
        print("You found 1 " + found + " in the wasteland.")
        print("------------------------------------------------")
        print("Inventory:")
        print("Guns =", survivor.guns)
        print("Ammo =", survivor.ammo)
        print("Food =", survivor.food)
        print("Water =", survivor.water)

        prompt = input("Would you like to search again? (Yes/No) ")

        if prompt == "Yes":
            play == True
        elif prompt == "No":
            play = False
            break
        
    #scavenge()

    pygame.quit()
    quit()

gameLoop()
