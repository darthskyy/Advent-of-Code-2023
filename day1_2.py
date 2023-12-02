from day1_1 import extract_lines, extract_num

nums = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
search_dict = {
    "z": ["zero"],
    "o": ["one"],
    "t": ["two", "three"],
    "f": ["four", "five"],
    "s": ["six", "seven"],
    "e": ["eight"],
    "n": ["nine"]
}
def digitize_line(line: str) -> str:
    ind = 0
    out = ""
    while ind < len(line):
        if line[ind] == "z" and line[ind:ind+4] == "zero":
            out += "0"
        elif line[ind] == "o" and line[ind:ind+3] == "one":
            out += "1"
        elif line[ind] == "t" and line[ind:ind+3] == "two":
            out += "2"
        elif line[ind] == "t" and line[ind:ind+5] == "three":
            out += "3"
        elif line[ind] == "f" and line[ind:ind+4] == "four":
            out += "4"
        elif line[ind] == "f" and line[ind:ind+4] == "five":
            out += "5"
        elif line[ind] == "s" and line[ind:ind+3] == "six":
            out += "6"
        elif line[ind] == "s" and line[ind:ind+5] == "seven":
            out += "7"
        elif line[ind] == "e" and line[ind:ind+5] == "eight":
            out += "8"
        elif line[ind] == "n" and line[ind:ind+4] == "nine":
            out += "9"
        else:
            out += line[ind]
        ind += 1
    return out

def main():
    lines = extract_lines("input1.txt")
    for i in range(len(lines)):
        lines[i] = digitize_line(lines[i])
    nums = [extract_num(line) for line in lines]
    for i in range(len(lines)):
        print(f"{lines[i]:40s}\t{nums[i]}")
    print(sum(nums))

if __name__=="__main__":
    main()
    # print(digitize_line("five5six6"))