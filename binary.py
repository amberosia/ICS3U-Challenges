#title: binary
#developer: jenna wan
#purpose: convert binary to decimal

column = ""
number = 0

bi = input("Binary: ")
digits = len(bi)

for x in range(digits):
    column = bi[digits-x-1]
    if column == "1":
        number = number + 2**x
    if column == "0":
        number = number + 0

print("Decimal: " + number)
