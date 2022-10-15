#title: digit reps
#developer: jenna wan
#purpose: returns the number of occurrences of a digit in an integer

def digitReps(posInt, digit):
    posInt, digit = str(posInt), str(digit)

    if digit not in posInt:
        return 0

    else:
        digitIndex = posInt.index(digit)
        return 1 + digitReps(posInt[digitIndex + 1:], digit)

def main():
    posInt = input("Integer: ")
    digit = input("Digit: ")
    print("Occurrences:", digitReps(posInt, digit))

main()
