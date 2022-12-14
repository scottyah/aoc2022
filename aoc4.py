
# DATA IMPORT
input_file = "puzzle_input/d4_p1.txt"
# data = "test_puzzle_input/d4_p1.txt"

data = [] # Each line will be a list, each range will be a tuple
with open(input_file) as file:
    for line in file:
        sections = line.split(',')
        converted_line = []
        for section in sections:
            vals = section.split('-')
            converted_line.append((int(vals[0]), int(vals[1])))
        data.append(converted_line)


# PART 1
p1_rtn = 0
for elf1, elf2 in data:

    # elf2 covers all of elf1
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        p1_rtn += 1 
    # elf1 covers all of elf2
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        
        p1_rtn += 1  
print("Part 1: ", p1_rtn)


# PART 2
p2_rtn = 0
for elf1, elf2 in data:
    # elf1's largest value is less than elf2's smallest
    if elf1[1] < elf2[0]:
        pass 
    # elf1's smallest value is greater than elf2's greatest
    elif elf1[0] > elf2[1]:
        pass 
    else:
        p2_rtn += 1
print("Part 2: ", p2_rtn)
