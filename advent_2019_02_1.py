f = open("advent_2019_02_input.txt")
#f = open("test_input.txt")

values = [int(v) for v in f.readline().strip().split(",")]

f.close()

values[1] = 12
values[2] = 2

val_dict = {}

for index, val in enumerate(values):
    val_dict[index] = val

pos = 0
while True:
    opcode = values[pos]
    if opcode == 99:
        break
    if opcode == 1:
        val_dict[values[pos + 3]] = val_dict[values[pos + 1]] + val_dict[values[pos + 2]]
    elif opcode == 2:
        val_dict[values[pos + 3]] = val_dict[values[pos + 1]] * val_dict[values[pos + 2]]
    pos += 4

print(val_dict[0])