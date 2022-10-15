#title: letter counter
#developer: jenna wan
#purpose: find most occuring letter

inpt = input("Input: ")
letters = {
}
maxLetter = ""
az = "abcdefghijklmnopqrstuvwxyz"

txt = inpt.lower()

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
