#title: find and replace
#developer: jenna wan
#purpose: find item in a list and replace it with another item

list = []
list2 = []

length = int(input("Length of the list: "))

for i in range(length):
    num = input("Item " + str(i+1) + ": ")
    list.append(num)

find = input("Find: ")
rep = input("Replace: ")

def find_replace(list):
    for x in list:
        if x == find:
            list2.append(rep)
        else:
            list2.append(x)

find_replace(list)

print(list2)
