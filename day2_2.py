from day2_1 import read_input
def get_power(game: list) -> int:
    max_colours = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for set_i in game:
        colours = set_i.split(", ")
        for item in colours:
            num, colour = item.split(" ")
            max_colours[colour] = max(int(num), max_colours[colour])
    
    return max_colours["red"] * max_colours["green"] * max_colours["blue"]
    pass

def main():
    games = read_input("input2.txt")
    total = 0
    for game in games[1:]:
        game_total = get_power(game)
        total += game_total
    
    print(total)
    pass

if __name__=="__main__":
    main()