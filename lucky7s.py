#title: lucky 7s
#developer: jenna wan
#purpose: rolls of a pair of dice and count times a sum of 7 is rolled

import random

seven = 0

rolls = int(input("Rolls: "))

for x in range(rolls):
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    add = die1 + die2
    print("(" + str(die1) + ", " + str(die2) + "); sum: " + str(add))
    if add == 7:
        seven += 1

print("Sevens: " + str(seven))
