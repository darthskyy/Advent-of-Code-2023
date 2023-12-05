def read_input(filename: str) -> list:
    out = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()[line.find(":") + 2:].split(" | ")
            winning, mine = line
            winning = winning.strip().split(" ")
            mine = mine.strip().split(" ")
            winning = [int(i) for i in winning if i != ""]
            mine = [int(i) for i in mine if i != ""]
            out.append([winning, mine])
    
    return out

def get_matches(line: list) -> int:
    winning, mine = line
    return len([num for num in mine if num in winning])

def line_result(line: list) -> int:
    x = get_matches(line)
    return 2**(x-1) if x > 0 else 0

def main():
    x = read_input('input4.txt')
    total = 0
    for i in x:
        total += line_result(i)
    
    print(total)

if __name__=="__main__":
    main()