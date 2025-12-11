"""
Docstring for day-5.index

PSUEDO CODE

1. read the input file
2. split the input text in 2 parts
3. first part contains all the ranges
4. second part contains all the ids that we need to check.
5. iterate over the list.
6. check if item is fresh and increase the fresh count.
7. return the count

def check_fresh(fresh_ranges,value)
    for current_range in fresh_ranges:
        start = current_range[0]
        end = current_range[1]

        if start - value <=0 and value - end <=0
            return True
        
        return False

"""

import os

def check_fresh(fresh_ranges,value):
    for current_range in fresh_ranges:
        start = int(current_range[0])
        end = int(current_range[1])

        if value >= start and value <= end:
            print("fresh")
            return True
        
    return False

def puzzle1():
    content = ""

    file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(file_path,'r') as f:
        content = f.read()  
    
    content_arr = content.split("\nMID\n")

    ranges = content_arr[0].split("\n")
    ranges_arr = []

    for item in ranges:
        item_arr = item.split('-')
        ranges_arr.append(item_arr)

    product_ids = content_arr[1].split("\n")

    fresh_product_count = 0

    # print("RANGES",ranges_arr)
    # print("PRODUCTS", product_ids)

    for item in product_ids:
        # print("item",item)
        id = int(item)
        result = check_fresh(ranges_arr,id)

        if result:
            fresh_product_count+=1

    return fresh_product_count

answer1 = puzzle1()
print("Answer puzzle 1: ", answer1)

def puzzle2():
    content = """3-5
10-14
16-20
12-18"""

    # file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    # with open(file_path,'r') as f:
    #     content = f.read()  
    
    # content_arr = content.split("\nMID\n")

    ranges = content.split("\n")
    print(ranges)
    ranges_arr = []

    for item in ranges:
        item_arr = item.split('-')
        ranges_arr.append(item_arr)
    
    answer = 0

    for item in ranges_arr:
        start = int(item[0])
        end  = int(item[1])

        # total fresh item count in this range
        total = end - start + 1
        answer += total

    return answer

answer2 = puzzle2()
print("Answer puzzle 2:", answer2)