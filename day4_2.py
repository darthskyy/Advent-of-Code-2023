from day4_1 import read_input, line_result, get_matches

def sort_days(days: list) -> dict:
    out = {}
    for i in range(len(days)):
        out[i] = 1
    
    return out

def main():
    x = read_input('input4.txt')
    counts = sort_days(x)
    for i in range(len(x)):
        for copy in range(counts[i]):
            matches = get_matches(x[i])
            for j in range(matches):
                try:
                    counts[i+j+1] = counts[i+j+1] + 1
                except:
                    pass
    
    num_cards = 0

    for day in counts:
        num_cards += counts[day]
    
    print(num_cards)


if __name__=="__main__":
    main()