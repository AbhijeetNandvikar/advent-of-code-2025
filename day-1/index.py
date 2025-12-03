"""
Psuedo code puzzle 1
1. Read the file
2. Split text into string array with each item as a single instruction
3. Create a zero counter variable
4. Create a while loop with exit condition as len(instructions) > 0
5. Iterate over each instruction and find out the direction.
    - if direction left substract with boundary condition
        if steps > 99 find modulo steps % 100
        if position - steps < 0 
            new_position => 100 + (position - steps)
        else:
            position = position - steps

    - if direction right add with boundary conditions
        if steps > 99 find modulo steps % 100
        else if position + steps > 100
            new_position => (position + steps) - 100
        else:
            position = position + steps

    
    increase the zero counter everytime the we get position zero
6. Return the answer.

position = 1

steps == 80
steps = 99
steps = 100
"""

"""
Psuedo code puzzle 2
1. Read the file
2. Split text into string array with each item as a single instruction
3. Create a zero counter variable
4. Create a while loop with exit condition as len(instructions) > 0
5. Iterate over each instruction and find out the direction.
    - if direction left substract with boundary condition
        if steps > 99 find length of steps and divide it by 100. that will be the number of times we hit zero and then again find modulo of steps
        if position - steps < 0 
            new_position => 100 + (position - steps)
        else:
            position = position - steps

    - if direction right add with boundary conditions
        if steps > 99 divide it by 100 and add that number, and finally find modulo
        else if position + steps > 100
            new_position => (position + steps) - 100
        else:
            position = position + steps

    
    increase the zero counter everytime the we get position zero
6. Return the answer.

position = 1

steps == 80
steps = 99
steps = 100
"""

import os
import math

def puzzle1():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        data = f.read()

        instructions = data.split("\n")
        # instructions = instructions[0:20]
        position = 50
        zero_counter = 0

    while len(instructions) > 0:
        instruction = instructions.pop(0)
        direction = instruction[0]
        steps = int(instruction[1:])

        if direction == 'L':
            if steps > 99:
                steps = steps % 100
            if position - steps < 0:
                position = 100 + (position - steps)
            else:
                position = position - steps
        else:
            if steps > 99:
                steps = steps % 100
            if position + steps > 99:
                position = position + steps - 100
            else:
                position = position + steps


        if(position == 0):
            zero_counter+=1

    return zero_counter

def puzzle2():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as f:
        data = f.read()

        instructions = data.split("\n")
        position = 50
        zero_counter = 0

    while len(instructions) > 0:
        instruction = instructions.pop(0)
        direction = instruction[0]
        steps = int(instruction[1:])
        if direction == 'L':
            if steps > 99:
                number_of_times_zero_occur = math.floor(steps / 100)
                zero_counter+=number_of_times_zero_occur
                steps = steps % 100
            if (steps != 0) and (position - steps < 0):
                if(position != 0 ): zero_counter+=1
                position = 100 + (position - steps)
            else:
                position = position - steps
                if(position == 0):
                    zero_counter+=1
        else:
            if steps > 99:
                number_of_times_zero_occur = math.floor(steps / 100)
                zero_counter+=number_of_times_zero_occur
                steps = steps % 100
            if steps != 0  and (position + steps > 99):
                if(position != 0 ): zero_counter+=1
                position = position + steps - 100
            else:
                position = position + steps
                if(position == 0):
                    zero_counter+=1
        

    return zero_counter


def main():
    answer1 = puzzle1()
    answer2 = puzzle2()
    print(answer1, answer2)
            

if __name__ == "__main__":
    main()
