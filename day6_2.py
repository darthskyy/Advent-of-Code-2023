def read_input(filename: str) -> list:
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    times = lines[0][lines[0].find(":")+1:].strip().replace(" ", "")
    distances = lines[1][lines[1].find(":")+1:].strip().replace(" ", "")
    return int(times), int(distances)

def get_low_beats(time: int, goal: int) -> int:

    curr_hold = -1
    while True:
        curr_hold += 1
        curr_move = time - curr_hold
        curr_distance = curr_hold * curr_move
        if curr_distance > goal:
            return curr_hold

    return curr_hold

def get_high_beats(time: int, goal: int) -> int:
    curr_hold = time
    while True:
        curr_move = time - curr_hold
        curr_distance = curr_hold * curr_move
        if curr_distance > goal:
            return curr_hold

        curr_hold -= 1

    return curr_hold


time, distance = read_input("input6.txt")
low_beats = get_low_beats(time, distance)
high_beats = get_high_beats(time, distance)
print(f"Low Beats: {low_beats}, High Beats: {high_beats}")
print(f"Ways to get to {distance} in {time} seconds: {high_beats - low_beats + 1}")