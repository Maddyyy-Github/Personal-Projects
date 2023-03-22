from prime_factorize import *

def check_coll_conjucture(input):
    step_count = 0
    num = input
    while num != 1:
        if num%2 == 0:
            num = num/2
        else:
            num = (num*3) + 1
        
        step_count += 1
        # print(step_count, '. ', num)
        
    
    return step_count

# max = 10000000
# high = 0
# for number in range(1, max):
#     steps = check_coll_conjucture(number)
#     if steps > high:
#         print(number, '-', steps, "steps", '-', prime_factorize(number))
#         high = steps


#979,468,873,716,713,000,000,000 just found this by randomly punching in numbers
# magic_num_dict = {}
# for number in range(0, 10**6):
#     num = 979468873716713000000000 + number
#     # if num%(10**5) == 0:
#     #     print(num)
#     value = check_coll_conjucture(num)
#     if value not in magic_num_dict.keys():
#         magic_num_dict[value] = [number]
#     else:
#         magic_num_dict[value].append(number)
    
# # print(magic_num_dict)
# for key in magic_num_dict.keys():
#     print(key, "-", len(magic_num_dict[key]))


number = 979468873716713000000003
# print(number, '-', check_coll_conjucture(number), 'steps -', prime_factorize(number)) 
print(number, '-', check_coll_conjucture(number))
print(prime_factorize(number))
