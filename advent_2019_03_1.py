f = open("advent_2019_03_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

wire1 = [v for v in lines[0].split(",")]
wire2 = [v for v in lines[1].split(",")]

set1, set2 = set(), set()

def traversePath(wire, setNumber):
    posX, posY = 0, 0
    for v in wire:
        dir = v[0]
        dist = int(v[1:])
        for i in range(dist):
            if dir == 'U':
                posY += 1
            elif dir == 'R':
                posX += 1
            elif dir == 'D':
                posY -= 1
            elif dir == 'L':
                posX -= 1

            if setNumber == 1:
                set1.add((posX, posY))
            else:
                set2.add((posX, posY))

traversePath(wire1, 1)
traversePath(wire2, 2)

import sys
min_dist = sys.maxsize

intersect = set1.intersection(set2)

while intersect:
    val = intersect.pop()
    min_dist = min((abs(val[0]) + abs(val[1])), min_dist)

print(min_dist)