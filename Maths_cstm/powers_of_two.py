#For a certain number of numbers, form all possible pairs such that all pairs sum upto a power of 2
#For Instance the numbers -1, 3, 5 give 3 pairs 2, 4 and 8, all of which are powers of two
#Numbers should be distinct non zero integers

#Since +n and -n will add upto 0, which is not a power of 2, such numbers must not be included in search
#In other words, magnitude of each number should also be Different
#Also, no 2 numbers should be negative since powers of 2 can not be -ve


from math import factorial, log2
from types import NoneType

def check_sum(numbers_to_check, check_for='power of 2'):
    sum = 0
    for number in numbers_to_check:
        sum += number
    
    if log2(sum)%1 == 0:
        return True
    else:
        return False


total_numbers = 3
total_pairs = factorial(total_numbers)/(factorial(total_numbers-2)*factorial(2))#Combination(total_numbers, 2)
search_upto = 10
start_search_from = 1
number_picker = 0

solution_found = False
number_list_initial = [start_search_from + _ for _ in range(total_numbers)]
number_list = number_list_initial[:]
pointer = 1
number_inspected = number_list[pointer]
list_1 = [start_search_from]
# white_list = list(range(-search_upto, search_upto))
while solution_found is False:

#For your first number, check the next match. Then check the next number for both of them. If found, move on, else, if the 2nd number is smaller than the max search domain, increment until you find the next match for number 1
        number_inspected_checked = False
        for num in number_list[:pointer]: #Check whether a particular number forms viable pairs of not
            if check_sum([num, number_inspected]) is False: 
                if number_inspected < search_upto:
                    number_inspected += 1
                else:
                    pointer -= 1 #Go back to the previous index since of possible numbers in search have been exhaused
                    if list_1[pointer] < search_upto:
                        list_1[pointer] += 1

                        #Bring Things down back to initial state, with an increment
                        index = 0


                    break

    

    



