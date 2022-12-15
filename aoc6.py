
# DATA IMPORT
input_file = "puzzle_input/day6.txt"

datastream = ""
with open(input_file) as file:
    for line in file:
        datastream = line.strip() # We know it's only one string

# COMMON
def first_marker(datastream_buffer: str, marker_length: int) -> int:
    for i in range(len(datastream_buffer)):
        splice = datastream_buffer[i:i+marker_length]
        if len(splice) == len(set(splice)):
            return(i+marker_length)
    return 0 

# PART 1
print("Part 1: ", first_marker(datastream, 4))

# PART 2
print("Part 2: ", first_marker(datastream, 14))


# TESTS
test1_data = [   
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
            ]
test1_answers = [5, 6, 10, 11]

test2_data = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
]
test2_answers = [19, 23, 23, 29, 26]

def day6_tests(function, params, data, answers):
    for test_case, answer in zip(data, answers):
        assert(answer == function(test_case, params))

# PART 1
day6_tests(first_marker, 4, test1_data, test1_answers)

# PART 2
day6_tests(first_marker, 14, test2_data, test2_answers)



