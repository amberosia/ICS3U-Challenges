#title: school store
#developer: jenna wan
#purpose: management of a school store

data = []
itemsLst = []
action = ""

#format
read = open("C:/Downloads/school/storeInventory.txt", "r")
x = read.readlines()

for i in x:
    frmt = i.lower().strip("\n").split(", ")
    data.append(frmt)

for i in range(len(data)):
    itemsLst.append(data[i][0])

read.close()


def search(item):
    if item.lower() in itemsLst:
        itemNum = itemsLst.index(item.lower())
        print("Name: " + data[itemNum][0] + ", Stock: " + str(data[itemNum][1]) + ", Cost: $" + str(data[itemNum][2]),"\n")
    else:
        print("Invalid Item.\n")

def purchase(item, qty):
    if item.lower() not in itemsLst:
        print("Invalid Item.\n")

    else:
        itemNum = itemsLst.index(item.lower())
            
        if qty < 0 or qty > int(data[itemNum][1]):
            print("Invalid Quantity.\n")
        else:
            write = open("C:/Downloads/school/storeInventory.txt", "w")

            total = float(data[itemNum][2]) * qty
            print("Total: $" + str(total), "\n")

            stock = int(data[itemNum][1])
            data[itemNum][1] = stock - qty

            for i in range(len(data)):
                write.write(data[i][0] + ", " + str(data[i][1]) + ", " + str(data[i][2]) + "\n")

            write.close()

def main(action):
    while action.lower() != "exit":

        print("What would you like to do? (Search/Purchase/Exit)")
        action = input("Input: ")

        if action.lower() == "search":
            item = input("Item: ")
            search(item)

        elif action.lower() == "purchase":
            item = input("Item: ")
            qty = int(input("Quantity: "))
            purchase(item, qty)
            
        elif action.lower() == "exit":
            print("\nThank you for visiting! :)") 

        else:
            print("Invaid action.\n")
            
main(action)
