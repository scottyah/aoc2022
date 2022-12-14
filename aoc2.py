# DATA POPULATION
input_file = "puzzle_input/day2.txt"
data = []

with open(input_file) as file:
    for line in file:
        line = line.strip()
        data.append(line[0] + line[2])

# COMMON
# hand map for ease of logging
h = {'A':'RCK','X': 'RCK', 'B':'PPR', 'Y':'PPR', 'C': 'SZR', 'Z': 'SZR'}

# play map for ease of logging
tlr = {'X': 'LOSE', 'Y': 'TIE ', 'Z': 'WIN '}


# PART 1
play_points = '_XYZ' # index is point value
winning_plays = ('AY','BZ', 'CX')
draw_plays = ('AX','BY','CZ')

p1_pts = 0
for i in data:
    # points for move played
    play_score= play_points.index(i[1])
    p1_pts += play_score

    # points for winning / losing / draw
    if i in winning_plays: 
        comp_score = 6
    elif i in draw_plays: 
        comp_score = 3
    else: 
        comp_score = 0
    p1_pts += comp_score

    print("played %s: %dpts | %s v %s: %dpts | round = %dpts | total = %dpts" % (i[1], play_score, h[i[0]], h[i[1]], comp_score, comp_score+play_score, p1_pts))


# PART 2
play_points = '_ABC' # index is point value
play_map = {
'AX': 'C',
'AY': 'A',
'AZ': 'B',
'BX': 'A',
'BY': 'B',
'BZ': 'C',
'CX': 'B',
'CY': 'C',
'CZ': 'A'
}
p2_pts = 0
for i in data:
    # points for move played
    play_score = play_points.index(play_map[i])
    p2_pts += play_score

    # points for winning / losing / draw
    if i[1] == 'Z': 
        comp_score = 6
    elif i[1] == 'Y': 
        comp_score = 3
    else: 
        comp_score = 0
    p2_pts += comp_score

    round_score = play_score + comp_score

    print("To %s against %s: play %s (%d points) | %d points for %s | round = %d | total = %d" % (tlr[i[1]], h[i[0]], h[play_map[i]], play_score, comp_score, tlr[i[1]], round_score, p2_pts))


print("Part 1: ", p1_pts)
print("Part 2: ", p2_pts)