proper = "0123456789."
nums = proper[:-1]
def read_input(filename: str) -> list:
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def make_grid(lines: list):
    out = []
    for line in lines:
        temp = []
        for char in line:
            temp.append(char)
        out.append(temp[:])
    
    return out

def check_cell(grid, i: int, j: int):
    try:
        if grid[i-1][j-1] not in proper:
            return True
    except:
        pass
    try:
        if grid[i-1][j] not in proper:
            return True
    except:
        pass
    try:
        if grid[i-1][j+1] not in proper:
            return True
    except:
        pass
    try:
        if grid[i][j-1] not in proper:
            return True
    except:
        pass
    try:
        if grid[i][j+1] not in proper:
            return True
    except:
        pass
    try:
        if grid[i+1][j-1] not in proper:
            return True
    except:
        pass
    try:
        if grid[i+1][j] not in proper:
            return True
    except:
        pass
    try:
        if grid[i+1][j+1] not in proper:
            return True
    except:
        pass
    return False

def get_nums(grid: list) -> list:
    out = []
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            k = 1
            if grid[i][j] in nums:
                valid = False
                num = grid[i][j]
                if check_cell(grid, i, j):
                    valid = True
                while j+k < len(grid[i]) and grid[i][j+k] in nums:
                    num += grid[i][j+k]
                    if check_cell(grid, i, j+k): valid = True
                    k += 1
                
                if valid: out.append(int(num))
            
            j += k
    return out
def main():
    grid = read_input('input3_demo.txt')
    grid = make_grid(grid)
    x = get_nums(grid)
    print(sum(x))

if __name__=="__main__":
    main()