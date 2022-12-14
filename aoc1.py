# DATA POPULATION
input_file = "puzzle_input/day1.txt"
data, buff = [], []

with open(input_file) as file:
    for line in file:
        line = line.strip()
        # New line signifies new elf inventory
        if line == "":
            data.append(buff)
            buff = []
        # Add new snack to buffer
        else:
            buff.append(int(line))

# COMMON 
groups = [sum(batch) for batch in data]

# PART 1
print("Part 1: ", max(groups))

# PART 2
print("Part 2: ", sum(sorted(groups, reverse=True)[:3]))