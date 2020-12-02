import re

##define count
valid = 0
valid2 = 0

##Open inputs and parse
with open("input.txt", "r") as f:
	   inputList = f.read()
	   inputList = inputList.split("\n")

for line in inputList:
    findInLine = re.search("^(\d+)-(\d+) ([A-Za-z_]): (.*)",line)
    minCount = int(findInLine[1])
    maxCount = int(findInLine[2])
    character = findInLine[3]
    password = findInLine[4]

    ##part 1 check
    #Count the number of characters in the password
    charPassword = password.count(character)
    if charPassword >= minCount and charPassword <= maxCount:
        valid += 1
        
    ##part 2 check
    #get the character in the location described in the string
    lChar = password[(minCount-1):minCount]
    uChar = password[(maxCount-1):maxCount ]
    if (lChar == character or uChar == character) and (lChar != uChar) :
        valid2 += 1

print ("Part 1:",valid)
print ("Part 2:",valid2)    

