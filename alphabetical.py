#title: alphabetical
#developer: jenna wan
#purpose: put two words in alphabetical order

word1 = input("First word: ")
word2 = input("Second word: ")


if len(word1) > 3 or len(word2) > 3:
    print("Word exceeds 3 characters.")

#when any word is 1 character
elif len(word1) == 1 or len(word2) == 1:

    if word1[0] < word2[0]:
        print ("Order: " + word1 + ", " + word2)

    if word1[0] > word2[0]:
        print ("Order: " + word2 + ", " + word1)

    else:
              
        if len(word1) < len(word2):
            print("Order: " + word1 + ", " + word2)
            
        if len(word1) > len(word2):
            print("Order: " + word2 + ", " + word1)
            
        if len(word1) == len(word2):
            print ("Order: " + word2 + ", " + word1)

#when any word is 2 characters
elif len(word1) == 2 or len(word2) == 2:
    
    for x in range(2):
        if word1[x] < word2[x]:
            print ("Order: " + word1 + ", " + word2)
            break

        elif word1[x] > word2[x]:
            print ("Order: " + word2 + ", " + word1)
            break

    else:
              
        if len(word1) < len(word2):
                print("Order: " + word1 + ", " + word2)
            
        if len(word1) > len(word2):
                print("Order: " + word2 + ", " + word1)
            
        if len(word1) == len(word2):
                print ("Order: " + word2 + ", " + word1)    

#when both words are 3 characters          
else:

    for x in range(3):
        if word1[x] < word2[x]:
            print ("Order: " + word1 + ", " + word2)
            break

        elif word1[x] > word2[x]:
            print ("Order: " + word2 + ", " + word1)
            break

    else:
        print ("Order: " + word2 + ", " + word1)
