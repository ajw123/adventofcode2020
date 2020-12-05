def get_seatID(passID):
    rows = int(passID[:7].replace("B","1").replace("F","0"),base=2)
    cols = int(passID[7:].replace("R","1").replace("L","0"),base=2)
    seatID = rows * 8 + cols
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

for seat in seatIDArray:
    if seat - prevSeat == 2:
        yourSeat = seat + 1
        break
    prevSeat = seat
print(yourSeat)
