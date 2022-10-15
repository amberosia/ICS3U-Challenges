#title: roulette 
#developer: jenna wan
#purpose: simuates roulette wheel except its scuffed 

import random
money = 10
result = ""

while money > 0:

    bet = input("Bet:(green/black/red) ")
    spin = random.randint(1,38)

    if bet == "red" or bet == "black" or bet == "green":

        if spin >= 1 and spin <= 2:
            result = "green"
            if bet == result:
                money = money + 18
            else:
                money = money - 1

        elif spin >= 3 and spin <= 20:
            result = "black"
            if bet == result:
                money = money + 1
            else:
                money = money - 1

        else:
            result = "red"
            if bet == result:
                money = money + 1
            else:
                money = money - 1

        print("Bet:",bet, ", Result:",result, ", Total $ Remaining:",str(money))
        end = input("End? (y) ")

        if end == "y":
            break

    else:
        print("Invalid bet")
