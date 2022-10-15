#title: reverse
#developer: jenna wan
#purpose: reverses a list

list2 = []

def rev(lst):
    for x in lst:
        list2.insert(0, x)
    print(list2)
    list2.clear()
