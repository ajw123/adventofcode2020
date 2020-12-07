def get_UniqueCount(response):
    return len(set(response.replace(" ","").replace("\n","")))
    
def get_Intersect(response):
    form = response.split("\n")
    intersect = form[0]
    for individual in form:
        intersect = set(intersect).intersection(set(individual))
    return len(intersect)

with open("input.txt", "r") as f:
    inputList = f.read()
    inputList = inputList.split("\n\n")

#part 1
countSum = 0
countSum2 = 0
for response in inputList:
    countSum += get_UniqueCount(response)
    countSum2 += get_Intersect(response)

print (countSum)
print (countSum2)
