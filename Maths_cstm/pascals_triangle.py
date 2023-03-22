#User input
number_of_rows = 14
starting_value = 1
filler_num = 0
show_filler = False


#Creating a basic stucture

lists = [] #gonna contain all row lists
max_numbers = (number_of_rows*2)-1 #number of numbers in 1st row (including 0's)
row_list = []

#creating the first row
for number in range(max_numbers):
    row_list.append(filler_num)
lists.append(row_list)

#set the first value in first row (for a start...)
lists[0][int((max_numbers-1)/2)] = starting_value #int((max_numbers+1)/2)-1 = int((max_numbers-1)/2)...(max_numbers+1)/2 is the central number, whose index is 1 minus that

#creating rest of the data
for row_index in range(1,number_of_rows):#number of lists = number of rows - 1 (we have already added row 1)
    row_list = []
    for number_index in range(max_numbers - row_index):#number of numbers in each list as per the row number
        number = lists[row_index-1][number_index] + lists[row_index-1][number_index + 1]#depicting value of the number based on numbers of previous row
        row_list.append(number)
    lists.append(row_list)
        
lists_no_filler = []
if show_filler is False:
    for list in lists:
        new_list = []
        for number in list:
            if number:
                new_list.append(number)
        lists_no_filler.append(new_list)


#Presenting the data 

#Finding the maximum number of digits
def digits(number):
    '''Returns the number of digits in a given input'''
    digit_count = 0
    for digit in str(number):
        digit_count += 1
    return digit_count

max_digits = 0  

number_of_digits = digits(starting_value)
if number_of_digits > max_digits:
    max_digits = number_of_digits
number_of_digits = digits(filler_num)
if number_of_digits > max_digits:
    max_digits = number_of_digits
for number in lists[-1][:int((number_of_rows+1)/2)]:
    number_of_digits = digits(number)
    if number_of_digits > max_digits:
        max_digits = number_of_digits

if max_digits % 2 == 0:
    max_digits += 1

# print(lists)
# print(max_digits)
space = ' '
empty_block = max_digits * space



def create_block(number, block_len):
    '''turns a number into a string of fixed number of digits for uniformity'''
    number_length = digits(number)
    if block_len % 2 == 0:
            block_length = block_len + 1
    else:
        block_length = block_len

    if number_length <= block_length: 
        if number_length % 2 == 0:
            num_of_spaces = int((block_length - number_length + 1)/2)
            block = (space * num_of_spaces) + str(number) + (space * (num_of_spaces-1))
        else:
            num_of_spaces = int((block_length - number_length)/2)
            block = (space * num_of_spaces) + str(number) + (space * num_of_spaces)
        
        return block


def make_triangle(list_of_lists):
    total_rows = len(list_of_lists)
    row_number = 0

    for list_num in list_of_lists:
        if show_filler:
            final_string = empty_block * row_number
        else:
            final_string = empty_block * (total_rows - row_number)


        final_list = []
        for number in list_num:
            final_list.append(create_block(number, max_digits))
            final_list.append(empty_block)
        for item in final_list:
            final_string += item
        print(final_string)
        row_number += 1


if show_filler:
    make_triangle(lists)
else:
    make_triangle(lists_no_filler)


        
        
        