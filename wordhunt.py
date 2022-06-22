# Input: array of characters of length 16
# output: a 4x4 array
def arr_to_grid(str):
    if len(str) != 16:
        raise Exception("list of string must be = 16")
    grid = [[""]*4, [""]*4, [""]*4, [""]*4 ]

    for i,c in enumerate(str):
        row = i // 4
        col = i % 4 
        grid[row][col] = c
    return grid


if __name__ == '__main__':
    str = "VMFWCUWLREHAREEG"
    print(arr_to_grid(str))