#title: letter counter
#developer: jenna wan
#purpose: find most occuring letter in each line of file

openInpt = open("C:/Downloads/school/letterCount.txt", "r")
az = "abcdefghijklmnopqrstuvwxyz"

#each line
for x in openInpt:
    letters = {
    }
    maxLetter = ""
    txt = x.lower()

    #each letter in line
    for i in txt:
        if i in az:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

    num = max(letters.values())

    for x,y in letters.items():
        if y == num:
            maxLetter = maxLetter + x + " "

    print(maxLetter + "occurs " + str(num) + " time(s).")

openInpt.close()
