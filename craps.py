#title: craps
#developer: jenna wan
#purpose: simulate one round of craps aaaaaa

import random
money = 50
win = ""

bet = int(input("Bet($): "))

if bet <= 0 or bet > money:
    print("Invalid Bet :(")

else:
    go = input("Type 'r' to roll: ")

    if go == "r" or go == "R":

        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        add = die1 + die2

        print("Result:", add)

        if add == 7 or add == 11:
            win == "t"
            print("You win $" + str(bet*2) + "! Your total is now $" + str(money + bet) + "!")

        else:
            target = add
            while win == "":
                go = input("Type 'r' to roll: ")

                die1 = random.randint(1,6)
                die2 = random.randint(1,6)
                add = die1 + die2

                print("Result:", add)

                if add == target:
                    win = "t"
                    print("You win $" + str(bet*2) + "! Your total is now $" + str(money + bet) + "!")
                elif add == 7 or add == 11:
                    win = "f"
                    print("You lost $" + str(bet) + "! Your total is now $" + str(money - bet) + "!")
                else:
                    win == ""
    else:
        print("bruh why didn't you type r :(")
