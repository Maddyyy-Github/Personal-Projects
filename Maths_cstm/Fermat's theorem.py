from int_float import *
import time

# start_time = time.time()
power = 2
max = 1000
list_of_triplets = []
count = 1 #to keep count of len(list)


for number1 in range(1, max + 1):
    term1_sq = number1**power
    for number2 in range(1, max + 1):
        term2_sq = number2**power
        term3_sq = term1_sq + term2_sq
        number3 = term3_sq ** (1/power)
        if int(number3)**power == term3_sq:
            equation1 = f'{number1}^{power} + {number2}^{power} = {int(number3)}^{power}'
            equation2 = f'{number2}^{power} + {number1}^{power} = {int(number3)}^{power}'
            if equation1 not in list_of_triplets and equation2 not in list_of_triplets:
                list_of_triplets.append(equation1)
                print(str(count)+ '. ', equation1)
                count += 1
    if number1%100 == 0:
        index = str(number1)
    
        print(f'----------------------------------------------------------------{index}')

# print(f'There were {len(list_of_triplets)} triplets in the given range')

# print(f'\nTime Taken = {time.time() - start_time} secs')

# print(list_of_triplets)