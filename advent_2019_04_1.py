f = open("advent_2019_04_input.txt")
#f = open("test_input.txt")

lines = [line.strip() for line in f.readlines()]

f.close()

ranges = lines[0].split("-")
min_range = int(ranges[0])
max_range = int(ranges[1])

validCount = 0

for i in range (min_range, max_range + 1):
    remLast = i % 10
    new_i = i // 10
    adjFound = False
    valid = True
    for j in range(5):
        rem = new_i % 10
        new_i //= 10
        if not adjFound and rem == remLast:
            adjFound = True
        if remLast < rem:
            valid = False
            break
        remLast = rem
    if valid and adjFound:
        validCount += 1

print(validCount)