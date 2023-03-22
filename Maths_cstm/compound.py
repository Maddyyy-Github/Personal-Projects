from int_float import *
def compound(principal, rate_interest, time=1, intervals=1):
    """Calculates compound interest"""
    
    try:
        compounded_value = principal * ((1 + (rate_interest/(intervals*100)))**(intervals*time))
        try:
            compounded_value = int_float(compounded_value)
        except:
            pass
        
        return compounded_value
        
    except:
        "Error!"


    
    

print(compound(1000, 10))    
