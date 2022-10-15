#title: baby steps
#developer: jenna wan
#purpose: determines which parent gets custody of their child

import random

steps = 0

while steps < 5 and steps > -1:
    chance = random.randint(1,10)
    if chance >= 1 and chance <= 7:
        steps += 1
        print("The baby steps forward and has taken " + str(steps) + " step(s).")

    else:
        steps -= 1
        print("The baby steps backward and has taken " + str(steps) + " step(s).")

if steps == 5:
    print("The baby ended up with their father.")

if steps == -1:
    print("The baby ended up with their mother.")
