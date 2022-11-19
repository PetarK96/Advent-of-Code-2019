f = open("advent_2019_01_input.txt")
#f = open("test_input.txt")

lines = [int(line.strip()) for line in f.readlines()]

f.close()

fuel_acc = 0

for line in lines:
    fuel = 0
    val = line
    while val != 0:
        val = max(0, ((val // 3) - 2))
        fuel += val
    fuel_acc += fuel

print(fuel_acc)