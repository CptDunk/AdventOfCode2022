file = open("key.txt")

stop: bool = False
packet = []

for index, char, in enumerate(file.read()):
    if (len(packet)) == 14:
        if len(set(packet)) == 14 and stop == False:
            print(index,packet)
            stop = True
        packet.pop(0)

    packet.append(char)
