#Take a user input and evaluate it.


number1 = float(input('Enter number 1: '))
number2 = float(input('Enter number 2: '))
operation = input('Enter operation (+,-,/,*): ')

if operation == '+':
    solution = number1 + number2
elif operation == '-':
    solution = number1 - number2
elif operation == '/':
    solution = number1 / number2
elif operation == '*':
    solution = number1 * number2

print('Solution = ' + str(solution) )
