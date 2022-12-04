input = open("key.txt")
fE = []
sE = []
lookfor: bool = True
index: int = 0
contains: int = 0
overlaps: int = 0

for lines in input.read().splitlines():
    first, second = lines.split(',')
    fE.append(first.split('-'))
    sE.append(second.split('-'))
while index < len(fE):
    lookfor = True
    rngS = range(int(sE[index][0]), int(sE[index][1])+1)
    rngF = range(int(fE[index][0]), int(fE[index][1])+1)
    if int(fE[index][0]) in rngS or int(fE[index][1]) in rngS or int(sE[index][0]) in rngF or int(sE[index][1]) in rngF:
        overlaps+=1
    if int(fE[index][0]) >= int(sE[index][0]) and int(fE[index][1]) <= int(sE[index][1]) or int(sE[index][0]) >= int(fE[index][0]) and int(sE[index][1]) <= int(fE[index][1]):
        contains += 1
    index += 1

print(fE)
print(sE)
print(contains)
print(overlaps)
