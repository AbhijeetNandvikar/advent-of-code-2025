"""

Puzzle 1

def checkInvalid(num):
    num_str = num.toString()
    len_num_str = len(num_str)
    half = math.floor(len_num_str)
    num_str_arr =[ num_str[0:half],num_str[half:]]
    
    return num_str_arr[0] == num_str_arr[1]

Psuedo code
1. read the text file
2. answer = 0
2. split the string by ","
3. loop over the each item
    a. split each item by "-" and parse it to get start and end
    b. iterate for start to end.
        i. isInvalid =  checkInvalid
        ii. if isInvalid 
            answer+=num


# Puzzle 2



"""

import math
import os

def checkInvalid(num):
    num_str = str(num)
    len_num_str = len(num_str)
    if len_num_str % 2 != 0:
        return False
    
    half = math.floor(len_num_str/2)
    num_str_arr =[ num_str[0:half],num_str[half:]]

    # print("num_str",num_str_arr)
    
    return num_str_arr[0] == num_str_arr[1]


def main():
    filePath = os.path.join(os.path.dirname(__file__),"input.txt")
    content = ''
    answer = 0

    with open(filePath,"r") as f:
        content = f.read()

    content_arr = content.split(",")
    # content_arr = content_arr[0:1]


    for range_str in content_arr:
        range_arr = range_str.split("-")
        start = int(range_arr[0])
        end = int(range_arr[1])

        for value in range(start,end+1):
            is_invalid = checkInvalid(value)
            if is_invalid:
                answer+=value
    
    print("Answer: ", answer)
    
main()



