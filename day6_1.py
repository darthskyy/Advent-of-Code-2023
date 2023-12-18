def read_input(filename: str) -> list:
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    times = lines[0][lines[0].find(":")+1:].strip().split()
    distances = lines[1][lines[1].find(":")+1:].strip().split()
    times = [int(t) for t in times]
    distances = [int(d) for d in distances]
    return times, distances


def get_beats(time: int, goal: int) -> int:
    beats = 0
    for hold in range(time):
        move = time - hold
        distance = hold * move
        if distance > goal:
            beats += 1

    return beats

times, distances = read_input("input6.txt")

product = 1
for i in range(len(times)):
    beats = get_beats(times[i], distances[i])
    print(f"Time: {times[i]}, Distance: {distances[i]}, Beats: {beats}")
    product *= beats

print(f"Product: {product}")
