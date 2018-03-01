import time
from random import randint

def RNG():
    rng = True
    while rng == True:
        first = input("From: ")
        last = input("To: ")
        randNumber = str(randint(int(first),int(last)))

        print("Your random number is:",randNumber)
        choice = input("Would you like to continue? ")

        if choice == "no" or "No" or "NO" or "N":
            break
        

RNG()
