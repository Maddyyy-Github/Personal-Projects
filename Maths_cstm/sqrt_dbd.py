#sqrt digit by digit
from string import digits
from int_float import int_float


def sqrt_dbd(operand, decimal_places=2):
    whole_numbers = []
    decimal_values = []
    for digit in int(operand):
        whole_numbers.append(digit)
    
    for digit in int_float(operand) - int(operand):
        decimal_places.append(digits)


    