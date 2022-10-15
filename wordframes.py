#title: word frames
#developer: jenna wan
#purpose: print a word in a frame

word = input("Word: ")
letters = len(word)
reverseWord = ""

print("*" + word + "*")

for x in range(letters):
    sideLetter1 = word[letters-x-1]
    sideLetter2 = word[x]
    print(sideLetter1 + "*" * letters + sideLetter2)

for x in range(letters):
    reverseWord = word[x] + reverseWord

print("*" + reverseWord + "*")
