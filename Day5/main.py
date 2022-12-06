import re
input = open("key.txt").read()
myList = []
ListFold = []
stop: bool = False
iteruj: int = 0

zadani, prikazy = input.split('\n\n')
zadani = zadani.split('\n')
prikazy = prikazy.strip().split('\n')
print(len(zadani)-1)
print(len(zadani[0]))
print(zadani[0])
for a in range(len(zadani)):
    myList.append([])
    for index in range(8):
        if zadani[index][1+iteruj] != ' ':
            myList[a].append(zadani[index][1+iteruj])
    iteruj += 4
_move: int = 0
_from: int = 0
_to: int = 0
listonos = []
for index,prikaz in enumerate(prikazy):
    listonos.append(re.findall(r'\d+', prikaz))
    _move = int(listonos[0][0])
    _from = int(listonos[0][1])-1
    _to = int(listonos[0][2])-1
    for i in range(_move):
        myList[_to].insert(i, myList[_from][0])
        myList[_from].pop(0)

    listonos.clear()

for node in myList:
    print(node[0])

