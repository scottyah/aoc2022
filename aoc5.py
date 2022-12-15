from collections import defaultdict
from collections import deque

# DATA IMPORT
input_file = "puzzle_input/day5.txt"
# data = "test_puzzle_input/d5_p1.txt"


# COMMON
def chunks(input: str, chunk_size: int) -> None:
    for i in range(0, len(input), chunk_size):
        yield input[i:i+chunk_size]

# for Part 1
def crateMover9000(num: int, src: str, dst: str, piles: defaultdict):
    for _ in range(num):
        piles[dst].append(piles[src].pop())

# for part 2
def crateMover9001(num: int, src: str, dst: str, piles: defaultdict):
    buff = []
    for _ in range(num):
        buff.append(piles[src].pop())
    piles[dst].extend(reversed(buff))

def main_fcn(cratemover) -> str:
    piles = defaultdict(deque)

    with open(input_file) as file:
        for line in file:
            # skip the empty space
            if line[0] == '\n':  pass
            # skip the numbering of the stacks
            elif line[1].isdigit(): pass

            # move operation
            elif line[:4] == 'move':
                _, num, _, src, _, dst = line.strip().split(' ') # 5 items
                num = int(num)
                cratemover(num, src, dst, piles)
                # print("moving %d from %s to %s" % (num, src, dst))

            # build the dictionary
            else: 
                for i, chunk in enumerate(chunks(list(line), 4)):
                    if len(chunk) >= 1 and chunk[1] != ' ':
                        piles[str(i+1)].appendleft(chunk[1])

    # make sure the last letters are in order and formatted as a string
    rtn = [0] * len(piles)
    for k,v in piles.items():
        rtn[int(k)-1] = v[-1]
    return ''.join(rtn)

print("Part 1: ", main_fcn(crateMover9000))
print("Part 2: ", main_fcn(crateMover9001))