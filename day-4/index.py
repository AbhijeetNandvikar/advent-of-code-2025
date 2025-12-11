"""
Docstring for day-4.index

PSUEDO CODE:

1. Read the input.
2. Convert it into 2d array with each line as a row.
3. Iterate through the array and check each item.
4. create a checking function.
5. Add the number of rolls that can be accessed. 
6. return the answer.

def check_roll_access():
    1. check 3 items above current row
    2. check 3 items below current row
    3. check left item, check right item
    4. increase the count every time we encounter a roll
    5. return true if adjcent_roll_count is < 4

"""

import os,copy

def check_roll_access(row_index,col_index, roll_grid):
    row_len = len(roll_grid[0])
    col_len = len(roll_grid)

    adjcent_roll_count = 0

    # check above
    if row_index > 0 and roll_grid[row_index - 1][col_index] == "@":
        adjcent_roll_count += 1

    # check below
    if row_index < row_len-1 and roll_grid[row_index + 1][col_index] == "@":
        adjcent_roll_count += 1

    # check left 
    if col_index > 0 and roll_grid[row_index][col_index - 1] == "@":
        adjcent_roll_count += 1

    # check right 
    if col_index < col_len - 1 and roll_grid[row_index][col_index + 1] == "@":
        adjcent_roll_count += 1

    # check top left
    if col_index > 0 and row_index > 0 and  roll_grid[row_index - 1][col_index - 1] == "@":
        adjcent_roll_count += 1

    # check top right 
    if col_index < col_len - 1 and row_index > 0  and  roll_grid[row_index - 1][col_index + 1] == "@":
        adjcent_roll_count += 1

    # check bottom left
    if col_index > 0 and row_index < row_len -1  and  roll_grid[row_index + 1][col_index - 1] == "@":
        adjcent_roll_count += 1

    # check bottom right
    if col_index < col_len -1 and row_index < row_len -1  and  roll_grid[row_index + 1][col_index + 1] == "@":
        adjcent_roll_count += 1

    return adjcent_roll_count < 4

def puzzle1():
    content = ""

    file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(file_path,'r') as f:
        content = f.read()  
    
    content_arr = content.split("\n")

    roll_grid = []
    answer = 0

    for item in content_arr:
        roll_grid.append(list(item))

    row_len = len(roll_grid[0])
    col_len = len(roll_grid)
    

    for row_index in range(0,row_len):
        for col_index in range(0,col_len):
            if roll_grid[row_index][col_index] == '@':
                has_role_access = check_roll_access(row_index,col_index,roll_grid)
                if has_role_access:
                    answer+=1
    
    return answer

answer = puzzle1()
print("Puzzle 1 answer:", answer)