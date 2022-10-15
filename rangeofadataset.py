#title: range of a data set
#developer: jenna wan
#purpose: state the difference between the maximum and minimum data entered

end = ""
min = "start"
max = "start"

while end != "y":
    num = float(input("Input: "))
    if min == "start" and max == "start":
        min = num
        max = num
    else:
        if num > max:
            max = num
        if num < min:
            min = num
    end = input("End? (y) ")

print("-")
print("Min: " + str(min) + ", Max: " + str(max))
print("Range: " + str(max - min))


