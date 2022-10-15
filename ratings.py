#title: ratings
#developer: jenna wan
#purpose: sort ratings of people's names

data = []

#format text file
read = open("shinobiNames.txt")
readLst = read.readlines()
read.close()

for line in readLst:
    dict = {}
    fName, lName, rating = line.strip("\n").split(", ")
    dict["name"] = fName + ", " + lName
    dict["rating"] = int(rating)
    data.append(dict)

#sort
def sort(rating):
    return rating["rating"]

data.sort(reverse = True, key = sort)

#write
write = open("shinobiNames.txt", "w")

for i in range(len(data)):
    write.write(data[i]["name"] + ", " + str(data[i]["rating"]) + "\n")

write.close()
