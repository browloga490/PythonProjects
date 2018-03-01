import random

items = ['Sword', 'Shield', 'Magic Wand', 'Gold', 'Nothing']
empty = []
numbers = [1, 9, 17, 22, 33, 105, 99, 1, 12]

def shuffle(items):
    # Pulls a random item out by shuffling the entire list.
    if len(items) > 0:
        random.shuffle(items)
        win = items.pop()
        print("You recieve as a reward: %s" % win)
    else:
        print("There is nothing left to receive.")

def same_order(items):
    # Pulls a random item out, but keeps the original order of the list.
    if len(items) > 0:
        num = len(items) - 1
        index = random.randint(0, num)
        win = items.pop(index)
        print("You recieve as a reward: %s" % win)
    else:
        print("There is nothing left to receive.")
