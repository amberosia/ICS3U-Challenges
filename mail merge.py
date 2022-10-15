#title: mail merge
#developer: jenna wan
#purpose: replaces $Name in message.txt with a name from name.txt and writes it in comments.txt

#names
readName = open("names.txt")
name = readName.readlines()
readName.close()

#message
readMess = open("message.txt")
mess = readMess.readlines()
readMess.close()

#replace
write = open("comments.txt", "w")

for name in name:
    name = name.strip("\n")

    for line in mess:
        namedMess = line.replace("$Name", name)
        write.write(namedMess)

    write.write("\n\n")

write.close()
