from int_float import int_float


def expn(operand, factor):
    """Returns an answer of your given {operand} raised to the power of your given {factor}
    So you can find out squares, cubes, etc. You can even find out roots, if your factor is a fraction."""
    error_code = "Error in "
    errors = 0
    
    #Validity of program
    try:
        operand_float = float(operand)
    except:
        error_code += "operand "
        errors += 1
    try:
        factor_float = float(factor)
    except:

        if errors > 0:
            error_code += "and "
        error_code += "factor "
        errors += 1
    #Error found
    if errors > 0:
        error_code.rstrip()
        error_code += "!"
        return(error_code)

    #Error not found    
    else:
        answer = operand_float ** factor_float
        answer = int_float(answer)

        return(answer)



print(expn(10,1/10))