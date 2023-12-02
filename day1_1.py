def extract_num(line: str) -> int:
    num = ""
    ind = 0
    while True:
        if ord(line[ind]) >= 48 and ord(line[ind]) <= 57:
            num += line[ind]
            break
        ind += 1
    
    ind = len(line) - 1
    while True:
        if ord(line[ind]) >= 48 and ord(line[ind]) <= 57:
            num += line[ind]
            break
        ind -= 1
    
    return int(num)

def extract_lines(filename: str) -> list:
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
    
    return lines
def main():
    lines = extract_lines("input1.txt")
    nums = [extract_num(line) for line in lines]
    print(sum(nums))

if __name__=="__main__":
    main()