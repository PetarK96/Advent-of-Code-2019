f = open("advent_2019_02_input.txt")
#f = open("test_input.txt")

values = [int(v) for v in f.readline().strip().split(",")]

f.close()

found = False

for noun in range(100):
    for verb in range(100):
        new_values = values[:]
        new_values[1] = noun
        new_values[2] = verb

        val_dict = {}

        for index, val in enumerate(new_values):
            val_dict[index] = val

        pos = 0
        while True:
            opcode = new_values[pos]
            if opcode == 99:
                break
            if opcode == 1:
                val_dict[new_values[pos + 3]] = val_dict[new_values[pos + 1]] + val_dict[new_values[pos + 2]]
            elif opcode == 2:
                val_dict[new_values[pos + 3]] = val_dict[new_values[pos + 1]] * val_dict[new_values[pos + 2]]
            pos += 4

        if val_dict[0] == 19690720:
            print(100 * noun + verb)
            found = True
            break

    if found:
        break