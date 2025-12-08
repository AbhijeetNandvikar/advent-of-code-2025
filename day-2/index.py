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

def checkInvalid1(num):
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
            is_invalid = checkInvalid1(value)
            if is_invalid:
                answer+=value
    
    print("Answer: ", answer)
    

"""

1258903
1111111
1212121212
123123123

"""


def checkInvalid2(num):
    # print("NUM",num)
    num_str = str(num)
    max_window_size = math.floor(len(num_str)/2)

    
    for str_len in range(1,max_window_size + 1):
        # print("max_window_size",max_window_size, str_len)
        initial_window = num_str[0:str_len]
        window_break = False    
        max_multiple = math.ceil(len(num_str) / (str_len))
        # print("initial_window",initial_window,len(num_str))

        # print("max_multiple",max_multiple)
        for multiple in range(1, max_multiple):
            new_start = str_len * multiple 
            new_end = str_len * (multiple + 1) 
            
            new_window = num_str[new_start:new_end]

            # print("initial_window compare", initial_window,new_window)

            if(new_window != initial_window):
                window_break = True
                break
        
        if window_break == False:
            print("all check complete",num) 
            return True
    
    return False



def puzzle2():
   answer = []
   content = ''

   filePath = os.path.join(os.path.dirname(__file__),"input.txt")
   with open(filePath,"r") as f:
    content = f.read()

    content_arr = content.split(",")

    for item in content_arr:
        item_arr = item.split("-")
        start = int(item_arr[0])
        end = int(item_arr[1])

        for step in range(start,end+1):
            isInvalid = checkInvalid2(step)
            if isInvalid:
                answer.append(step)
    return sum(answer)
   

ans = puzzle2()
print("answer puzzle 2",ans)
