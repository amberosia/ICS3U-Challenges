#title: caesar cypher
#developer: jenna wan
#purpose: decrypts an encrypted message

inpt = open("C:/Downloads/school/caesarEncrypted.txt", "r")
outp = open("C:/Downloads/school/caesarDecrypted.txt", "w")
az = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = int(inpt.readline())%27

for line in inpt:
    txt = line.upper()

    for i in txt:
        if i in az:
            value = az.find(i)
            decrypt = az[value - key]
            outp.write(decrypt)
        else:
            outp.write(i)
    
inpt.close()
outp.close()
