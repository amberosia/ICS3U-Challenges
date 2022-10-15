#title: find and replace
#developer: jenna wan
#purpose: find item in a list and replace it with another item

def find_replace(lst, find, rep):
    lst2 = []
    for x in lst:
        if x == find:
            lst2.append(rep)
        else:
            lst2.append(x)
    print(lst2)
