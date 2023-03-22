from math import ceil
from string import digits


def digit_table(number, digits):
    '''Tells the first multiple of the number with those many digits'''
    lowest_num_in_digit = 10 ** (digits-1)
    multiple_in_digit = (ceil((lowest_num_in_digit/number))) * number #for instance first 3 digit multiple of 3 has 3 as a factor. ceil(100/3) is the other factor. 

    return multiple_in_digit


print(digit_table(9,4))