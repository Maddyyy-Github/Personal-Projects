expression = input('Enter expression: ')
operators = ( '/', '*', '+', '-')

bits_of_expressions = []
operator_indexes = []
number = ''
for digit in expression:
    if digit not in operators:
        number += digit
    else:
        bits_of_expressions.append(int(number))
        operator_indexes.append(len(bits_of_expressions))
        bits_of_expressions.append(digit)
        number = ''
bits_of_expressions.append(int(number))
while len(bits_of_expressions)>1:
    copy_of_bits = bits_of_expressions[:]
    copy_of_indexes = operator_indexes[:]
    break_flag = False
    for operator in operators:
        for operator_index in copy_of_indexes:
            if copy_of_bits[operator_index] == operator:
                if operator == '/':
                    answer = bits_of_expressions[operator_index - 1] / bits_of_expressions[operator_index + 1]
                if operator == '*':
                    answer = bits_of_expressions[operator_index - 1] * bits_of_expressions[operator_index + 1]
                if operator == '+':
                    answer = bits_of_expressions[operator_index - 1] + bits_of_expressions[operator_index + 1]
                if operator == '-':
                    answer = bits_of_expressions[operator_index - 1] - bits_of_expressions[operator_index + 1]
                bits_of_expressions.pop(operator_index - 1)
                bits_of_expressions.pop(operator_index - 1)
                bits_of_expressions.pop(operator_index - 1)
                bits_of_expressions.insert(operator_index - 1, answer)
                for index in copy_of_indexes:
                    if index > operator_index:
                        new_index = index - 2
                        operator_indexes[copy_of_indexes.index(index)] = new_index
                operator_indexes.remove(operator_index)
                break_flag = True
                break
        if break_flag:
            break
                
print(bits_of_expressions[0])





                









