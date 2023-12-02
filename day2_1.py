bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_game(game: list) -> bool:
    for set_i in game:
        colours = set_i.split(", ")
        for item in colours:
            num, colour = item.split(" ")
            if int(num) > bag[colour]:
                return False
    
        # print(colours)
    return True
    pass
def read_input(filename: str) -> list:
    out = ["-"]
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            out.append(line[line.find(":")+2:].strip().split("; "))
    return out

def main():
    games = read_input("input2.txt")
    total = 0
    for i in range(1, len(games)):
        if check_game(games[i]): total+=i
    print(total)
    pass

if __name__=="__main__":
    main()