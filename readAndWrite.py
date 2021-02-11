f = open("readANDwrite.txt")
#f.read()

fileLines = f.readlines()
for line in fileLines:
    print(line)

