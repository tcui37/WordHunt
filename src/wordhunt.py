from english_words import english_words_lower_alpha_set

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

# in:
# cord: i,j
# seen: set of cord
# curr_path: list of cord
# paths: list of paths
# out: returns all words from (i,j) with seen {}

def all_paths(cord,grid,seen=set(),curr_path=[],paths=[],limit=8):
    seen.add(cord)
    if len(curr_path) >= 3:
        paths.append(curr_path)
    for neighbor in get_neighbors(cord):
        # skip neighbor if its in our path
        if neighbor in seen:
            continue
        if len(curr_path) > 9:
            continue
        all_paths(neighbor,grid,seen.copy(),curr_path + [neighbor],paths)


# in: (i,j) cord
#returns set of 8 neighboring cords of cord (i,j)
def get_neighbors(cord):
    return_set = set()
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            new_cord = (min(3,(max(0,cord[0] + i))), min(3,(max(0,cord[1] + j))))
            return_set.add(new_cord)
    return return_set
    
# input: list of cords, 4x4 grid
# out: a string from corresponding cords
def path_to_word(path,grid):
    str = ""
    for row,col in path:
        str += grid[row][col]
    return str

# input 16 letter string wrapped for a 4x4 board
# out: list

def generate_words(str):
    grid = arr_to_grid(str)
    paths = []
    word_list = []
    for i in range(4):
        for j in range(4):
            all_paths((i,j),grid,set(),[],paths)
    for path in paths:
        str = path_to_word(path,grid)
        if str in english_words_lower_alpha_set:
            word_list.append(str)
    word_list = list(set(word_list))
    word_list.sort(reverse=True, key=len)
    return word_list



if __name__ == '__main__':
    str = "iogaygbrawrlahnn".lower()
    # grid = arr_to_grid(str)
    # paths = []
    # start = (0,0)
    # all_paths(start,grid,set(),[],paths)
    # path1 = paths[4]
    # print(path_to_word(path1,grid))
    # print("here" in english_words_lower_alpha_set)
    # print(generate_words(str))
    print(get_neighbors((2,0)))
    pass
