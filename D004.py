import re

attributesList = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
eyeList = ['amb','blu','brn','gry','grn','hzl','oth']
countValid = 0
countValid2 = 0

def get_SecurityCheck(attributes, whiteList, part):
    for test in attributesList:
        if test not in attributes.keys() and test not in whiteList:
            return 0
    if part == 2:
        return get_FieldCheck(attributes)
    return 1       

def get_FieldCheck(attributes):
    for key in attributes:
        value = attributes[key]
        if key == 'byr':
            if int(value) < 1920 or int(value) > 2002:
                return 0
        elif key == 'iyr':
            if int(value) < 2010 or int(value) > 2020:
                return 0
        elif key == 'eyr':
            if int(value) < 2020 or int(value) > 2030:
                return 0
        elif key == 'hgt':
            height = re.search(r"([-+]?\d*\.?\d+)([a-z]+)",value)
            if not height:
                return 0
            elif height[2] == "in" and (int(height[1]) < 59 or int(height[1]) > 76):
                return 0
            elif height[2] == "cm" and (int(height[1]) < 150 or int(height[1]) > 193):
                return 0
        elif key == 'hcl':
            if not re.search(r"^#[a-fA-F0-9]+$",value):
                return 0
        elif key == 'ecl':
            if value not in eyeList:
                return 0
        elif key == 'pid':
            if len(value) != 9:
                return 0
        elif key == 'cid':
            continue
    return 1
    
def get_PassportAttributes(passportRaw):
    passportList = []
    passportParse = passportRaw.split("\n\n")
    for passportItems in passportParse:
        attributes = dict(item.split(":") for item in re.split("\n| ",passportItems))
        passportList.append(attributes)
    return passportList

with open("input.txt", "r") as f:
    inputList = f.read()

passportList = get_PassportAttributes(inputList)

for passports in passportList:
    countValid += get_SecurityCheck(passports,['cid'],1)
    countValid2 += get_SecurityCheck(passports,['cid'],2)
    
print(countValid)
print(countValid2)
