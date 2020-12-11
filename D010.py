
def get_IntValue(e):
    return int(e)

def get_Possibilities(count):
    sumList = [1,2,4]
    totalAmount = 0

    if count <= 3:
        return sumList[count-1]
    
    for i in range(0,count):
        if i <= 3:
            a = 0
        else:
            a = i - 3
        totalAmount = sum(sumList[a:i])
        if i > 3:
            sumList.append(totalAmount)
    if totalAmount == 0:
        totalAmout = 1
    return(totalAmount)
    

with open("input.txt", "r") as f:
    inputList = list(f.read().split("\n"))

one = 1
three = 1
old = 0
add = 0
total = 0
groupCount = 0
permGroup = []
#part 1 - sort list for count
inputList.sort(key = get_IntValue)
for i in range (0,len(inputList)-1):
    new = int(inputList[i])
    
    if (new - old) == 1:
        #Part 1 count of one jump
        one += 1
        add += 1

        #Part 2 count of permutation group
        groupCount += 1
        
    elif (new - old) == 3:
        #Part 1 count of a three jump
        three += 1
        add = 0

        #Part 2 add permutation group count
        permGroup.append(groupCount)
        groupCount = 0
        
    old = new
    total += add - 1

amount.append(groupCount + 1)
print (one," x ",three, "=", one * three)

countPerm = 1
for i in range(0,len(amount)):
    if amount[i] != 0:
        countPerm = countPerm * get_Possibilities(amount[i])


print(countPerm)
