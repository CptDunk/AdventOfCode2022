import math
# pDict = {'X': {'A': 4, 'B': 1, 'C': 7}, 'Y': {'A': 8, 'B': 5, 'C': 2}, 'Z': {'A': 3, 'B': 9, 'C': 6}}
sDict = {'A': {'X': 3, 'Y': 4, 'Z': 8}, 'B': {'X': 1, 'Y': 5, 'Z': 9}, 'C': {'X': 2, 'Y': 6, 'Z': 7}}
myList = []
enemyList = []
playerList = []
fullList = []
i = 0
file = open("key.txt")
for line in file.read().splitlines():
    myList.append((line.split(" ")))
file.close()
for a in myList:
    enemyList.append(a[0])
    playerList.append(a[1])
# print(enemyList)
# print(playerList)
for index,a in enumerate(enemyList):
    fullList.append(sDict[enemyList[index]][playerList[index]])
#    print(eDict[enemyList[index]][playerList[index]])
print(sum(fullList))