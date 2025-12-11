"""
Docstring for day-3.index

Psuedo code
1. Read the input file and store it in string.
2. Split the input into string array, with line break as a seperator.
3. convert string into number.
4. find out the max number that you can make using their digits.
5. Add those numbers

def get_max_voltage_puzzle_1():
1. declare and initialize 3 variables max_num and second_max_num, max_num_index
2. start iterating over the array.
3. check a number if it is greater than max_num place it in max_num. We will check max num till len(value) - 2 position
4. check a number if it is greater than second_max_num and if it's index is greater then max_num_index place it.

Puzzle 2:
1. def get_max_voltage_puzzle_1():
2. have a loop for setting 12 numbers one by one
3. for each index the range over which we iterate will change

"""

import os

def get_max_joltage_puzzle_1(value):
    max_num = -1
    max_num_index = -1
    second_max_num = -1
    num_count = len(value)
    for index in range(len(value)):
        current_num = int(value[index])

        if current_num > max_num and index <= num_count - 2:
            max_num = current_num
            max_num_index = index
            second_max_num = -1
        if current_num > second_max_num and index > max_num_index:
            second_max_num = current_num

    return int(f"{max_num}{second_max_num}")


# answer1 = get_max_joltage("987654321111111")
# answer2 = get_max_joltage("811111111111119")
# answer3 = get_max_joltage("234234234234278")
# answer4 = get_max_joltage("818181911112111")
# print(answer1,answer2,answer3,answer4)
# print(answer1+answer2+answer3+answer4)


def puzzle1():
    content = ''
    answer = 0

    file_path = os.path.join(os.path.dirname(__file__),"input.txt")

    with open(file_path,'r') as f:
        content = f.read()  
    
    content_arr = content.split("\n")
    # content_arr = content_arr[0:1]


    for item in content_arr:
        result = get_max_joltage_puzzle_1(item)
        print("result", result)
        answer+= result


    return answer

# answer = puzzle1()
# print("Answer",answer)

TOTAL_DIGITS = 12

def get_max_joltage_puzzle_2(value):
    value_len = len(value)
    # print(value_len)
    result = "000000000000"
    positions = [0]*12
    for loop in range(0,TOTAL_DIGITS):
        # print("\n loop index",loop, "range", loop , value_len + 1- (TOTAL_DIGITS - loop))
        for index in range(loop,value_len + 1  - (TOTAL_DIGITS - loop)):
            # print( "numvalue",index, value[index], end=" ")
            if(int(result[loop]) < int(value[index])):
                if loop == 0:
                    result_arr = list(result)
                    result_arr[loop] = value[index]
                    positions[loop] = index
                    result = "".join(result_arr)
                elif index > positions[loop - 1]:
                    result_arr = list(result)
                    result_arr[loop] = value[index]
                    positions[loop] = index
                    result = "".join(result_arr)
                # if loop == 0: 
                #     positions[loop] = index
                #     result_arr = list(result)
                #     result_arr[loop] = value[index]
                #     result = "".join(result_arr)
                # elif index > positions[loop]:
                #     positions[loop] = index
                #     result_arr = list(result)
                #     for reset_index in range(loop+1,TOTAL_DIGITS):
                #         result_arr[reset_index] = "0"
                #     result_arr[loop] = value[index]
                #     result = "".join(result_arr)
               
    return int(result)


def puzzle2():
    content = ''
    answer = 0

    file_path = os.path.join(os.path.dirname(__file__),"input.txt")

    with open(file_path,'r') as f:
        content = f.read()  
    
    content_arr = content.split("\n")
    # content_arr = content_arr[0:1]


    for item in content_arr:
        result = get_max_joltage_puzzle_2(item)
        print("result", result)
        answer+= result


    return answer

answer = puzzle2()
print("Answer",answer)
print(len("811111111111119"),"len")
