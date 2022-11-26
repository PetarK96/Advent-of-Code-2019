f = open("advent_2019_03_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

wire1 = [v for v in lines[0].split(",")]
wire2 = [v for v in lines[1].split(",")]

set1, set2 = set(), set()
dict1, dict2 = {}, {}

def traversePath(wire, setNumber):
    posX, posY, steps = 0, 0, 0
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

            steps += 1
            posTup = (posX, posY)

            if setNumber == 1:
                set1.add(posTup)
                if posTup not in dict1:
                    dict1[posTup] = steps
            else:
                set2.add(posTup)
                if posTup not in dict2:
                    dict2[posTup] = steps

traversePath(wire1, 1)
traversePath(wire2, 2)

import sys
min_dist = sys.maxsize

def calc_distances(point):
    return dict1[point] + dict2[point]

intersect = set1.intersection(set2)

while intersect:
    val = intersect.pop()
    min_dist = min(calc_distances(val), min_dist)

print(min_dist)