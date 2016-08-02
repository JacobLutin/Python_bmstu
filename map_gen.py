from random import randrange

def setRoom(minLen, maxLen):

    height = randrange(minLen, maxLen);
    width = randrange(minLen, maxLen);

    room = [[" " for j in range(width)] for i in range(height)]

    for i in range(height):
        for j in range(width):
            if (i == 0 or i == height - 1 or j == 0 or j == width - 1):
                room[i][j] = "#"

    return room

def printRoom(room):
    for i in room:
        for j in i:
            print(j)#, end=" ")
        print()

def setMap(mapLen, minLen, maxLen):

    map = [["*" for j in range(mapLen)] for i in range(mapLen)]

    xPos = 0
    yPos = 0

    for yPos in range(mapLen):
        for xPos in range(mapLen):
            if map[yPos][xPos] == "*":
                height = yPos + randrange(minLen, maxLen);
                width = xPos + randrange(minLen, maxLen);

                canBuild = True

                for yRoom in range(yPos, height):
                    for xRoom in range(xPos, width):
                        if xRoom >= mapLen or yRoom >= mapLen:
                            canBuild = False
                            break
                        if map[yRoom][xRoom] == "#" or map[yRoom][xRoom] == " ":
                            canBuild = False
                            break

                if canBuild:
                    for yRoom in range(yPos, height):
                        for xRoom in range(xPos, width):
                            map[yRoom][xRoom] = " "
                            if (xRoom == xPos or xRoom == width - 1 or
                                yRoom == yPos or yRoom == height - 1):
                                map[yRoom][xRoom] = "#"

    return map

def printMap(map):
    for row in map:
        line = ""
        for x in row:
            line += x
            line += ' '
        print(line)

rooms = []
mapLen = 35
maxLen = 12
minLen = 4
numOfRooms = 5

map = setMap(mapLen, minLen, maxLen)

printMap(map)

playerInput = ""

while playerInput != "exit":

    playerInput = input()

    if playerInput == "up":
        playerYpos -= 1
    if playerInput == "down":
        playerYpos += 1
    if playerInput == "left":
        playerXpos -= 1
    if playerInput == "right":
        playerXpos += 1

    map[playerYpos][playerXpos] = "@"
    printMap(map)
