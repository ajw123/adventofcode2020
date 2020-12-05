def get_seatID(passID):
    seatRanges = {
                    "rows":[0,127],
                    "cols":[0,7]
                 }
    for bin in passID:
        if bin in ["B","F"]:
            id = "rows"
        else:
            id = "cols"
            
        if bin in ["B","R"]:
            lRow = ((seatRanges[id][1] + 1) - seatRanges[id][0])/2 + seatRanges[id][0]
            uRow = seatRanges[id][1]
            seatRanges[id] = [lRow, uRow]
        elif bin in ["F","L"]:
            lRow = seatRanges[id][0]
            uRow = ((((seatRanges[id][1] + 1) - seatRanges[id][0])/2) - 1) + seatRanges[id][0]
            seatRanges[id] = [lRow, uRow]
    seatID = seatRanges["rows"][0] * 8 + seatRanges["cols"][0]
    return seatID

seatIDArray = []

with open("input.txt", "r") as f:
    inputList = f.read()
    inputList = inputList.split("\n")

for bPass in inputList:
    seatIDArray.append(get_seatID(bPass))

#part 1    
print(max(seatIDArray))

#part 2
seatIDArray.sort()
prevSeat = min(seatIDArray)
print(prevSeat)
for seat in seatIDArray:
    if seat - prevSeat == 2:
        yourSeat = seat + 1
        break
    prevSeat = seat

print(yourSeat)
