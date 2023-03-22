from math import log2, log10, floor


def int_float(number, return_n_of_decimal_places=False):
    """Removes the decimal from a floating point number if not needed"""
    error_msg = "Error in int_float() module"
    try:
        if number-int(number) == 0:
            number = int(number)
            if return_n_of_decimal_places:
                decimal_places = 0
        
        else:
            if return_n_of_decimal_places:
                decimal_places = len(number - 2)


    except TypeError:
        print(error_msg)
    except ValueError:
        print(error_msg)

    else:
        if return_n_of_decimal_places:
            return decimal_places
        else:
            return number

number_line_range = 4
inverse_n = 10/number_line_range
power_of_10 = int(log10(inverse_n))
inverse_2mod3 = inverse_n/10**(power_of_10)
n = int(log2(inverse_2mod3)) + 1 + 3*power_of_10

step = int_float(1/(2**((n-1)%3)) / 10**(floor((n-1)/3)))

print(step)