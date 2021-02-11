
def askPath():
    pathOfFile = input("Enter the path of file: ")
    countWords(pathOfFile)

def countWords(pathOfFile):
    numOfWords = 0
    lineNumber = 0
    file = open(pathOfFile)
    readLines = file.readlines()
    for lines in readLines:
        lineNumber += 1
        
        words = lines.split()
        numOfWords = numOfWords + len(words)

        print("Words in line" + str(lineNumber))
        print(len(words))

    print("Number of total words in file: ", numOfWords)

askPath()
