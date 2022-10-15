#title: bracket logic
#developer: jenna wan
#purpose: state if a bracket sequence is logical or not

count = 0

brac = str(input("Sequence of brackets: "))

for x in range(len(brac)):
    if brac[x] == "(":
        count += 1
    else:
        count -= 1
    if count < 0:
        break

if count == 0:
    print("The sequence is logically ordered.")

else:
    print("The sequence is not logically ordered.")
