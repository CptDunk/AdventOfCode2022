keyList = []
first = []
second = []
token = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
found: bool = False
lookfor: bool = True
soucet: int = 0
indexI: int = 0
x: int = 0
file = open("key.txt")

for line in file.read().splitlines():
    keyList.append(line)
for index, getLine in enumerate(keyList):
    first.append(keyList[index][:len(keyList[index])//2])
    second.append(keyList[index][len(keyList[index])//2:])
for index, lines in enumerate(first):
    found = False
    lookfor = True
    for i in lines:
        if i in second[index] and lookfor:
            if i.islower():
                soucet += ord(i) - 96
                found = True
            if i.isupper():
                soucet += ord(i) - 38
                found = True
            if found:
                lookfor = False
for i in range(len(keyList)//3):
    lookfor = True

    for a in token:
        print(a)
        if lookfor:
            if a in keyList[indexI+0] and a in keyList[indexI+1] and a in keyList[indexI+2]:
                if a.isupper():
                    print(a, ord(a)-38)
                    x += ord(a) - 38
                    lookfor = False

                if a.islower():
                    print(a, ord(a)-96)
                    x += ord(a) -96
                    lookfor = False
    indexI += 3
print(soucet)
print(x)