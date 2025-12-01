"""
Psuedo code
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


import os


def main():
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
        print(direction,steps)
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

        print(position)

        if(position == 0):
            zero_counter+=1

    return zero_counter
            

if __name__ == "__main__":
    ans  = main()
    print(ans)
