

word1 = input("First word: ")
word2 = input("Second word: ")




len1 = len(word1)
len2 = len(word2)

if len1 > len2:
    for x in range(len2):
        if word1[x] > word2[x]:
            print ("Order: " + word2 + ", " + word1 )
            break
        elif word1[x] < word2[x]:
            print ("Order: " + word1 + ", " + word2)
            break
    else:
        print ("Order: " + word2 + ", " + word1 )
elif len1 < len2:
    for x in range(len1):
        if word1[x] > word2[x]:
            print ("Order: " + word2 + ", " + word1 )
            break
        elif word1[x] < word2[x]:
            print ("Order: " + word1 + ", " + word2)
            break
    else:
        print ("Order: " + word1 + ", " + word2 )
else:
    for x in range(len1):
        if word1[x] > word2[x]:
            print ("Order: " + word2 + ", " + word1 )
            break
        elif word1[x] < word2[x]:
            print ("Order: " + word1 + ", " + word2)
            break
    else:
        print ("Order: " + word1 + ", " + word2 )
