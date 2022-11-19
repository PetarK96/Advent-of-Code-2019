f = open("advent_2019_01_input.txt")
#f = open("test_input.txt")

lines = [int(line.strip()) for line in f.readlines()]

f.close()

fuel_acc = 0

for line in lines:
    fuel_acc += ((line // 3) - 2)

print(fuel_acc)