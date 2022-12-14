# DATA POPULATION
input_file = "puzzle_input/day3.txt"

with open(input_file) as file:
    data = [line.strip() for line in file]

# COMMON
def get_priority(letter: str) -> int:
    if letter.islower(): 
        return ord(letter) - ord('a') + 1
    else: 
        return ord(letter) - ord('A') + 27

def chunks(input: int, to_skip: int) -> None:
    for i in range(0, len(input), to_skip):
        yield input[i:i+to_skip]

# PART 1
p1_sum = 0
for block in data:
    m = len(block) // 2
    first_half, second_half = set(block[:m]), set(block[m:])

    dupe = first_half.intersection(second_half)
    p1_sum += get_priority(list(dupe)[0]) # assumes good data
print("Part 1: ", p1_sum)


# PART 2
p2_sum = 0
for b1, b2, b3 in chunks(data, 3):
    badge = set.intersection(set(b1), set(b2), set(b3))
    p2_sum += get_priority(list(badge)[0]) # assumes good data
print("Part 2: ", p2_sum)