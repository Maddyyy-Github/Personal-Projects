from math import ceil

def check_prime(number):
    """Checks whether a number is prime or not. Returns a boolean value."""
    number
    factors_list = []

    for num in range(1, number):
        
        if number%num == 0:
            factors_list.append(num)
        if len(factors_list) > 1:
            break
        if (num * (num + 2)) > number: #we dont need to check all the numbers to find a factor. Each number reduces the range to search in. while factorizing, xy are 2 factors. when x increases, y decreases. At x^2 both have equal value. If no factor is found until now, the y value goes below x, which we have already checked.

#Above logic explained further. In simple terms, If x^2 is greater than the number to factorize, there are no factors, since inceasing x would mean decreasing y, which we have already checked. Further more, if x(x+2) is greater than the number, squares of all the other numbers are also greater than the number {x(x+2) = x^2 + 2x and the next square is 1 more than that, others being even greater}. Which means, the number would have no factor. So actually, we can know 2 numbers in advance whether there are any remaining numbers to check.
            break

    # factors_list.append(number) although, this is what all numbers have but this is just an extra step, since its not the factors that we care about, but the number of factors. So we can just subtract 1 from all, saving us a clock cycle.
    if len(factors_list) == 1:
        prime_status = True
    else:
        prime_status = False

    return prime_status

def prime_factorize(number):
    """Prime factorizes a number, returns a list as exponents of different factors"""
    operand = number        
    prime_fact_list = []

    #Check whether the number is prime or not, this will save time in not using other operators.

    while operand != 1:
        for num in range(1, operand):
            if operand%num == 0: #first up, find a factor of the number
                if check_prime(num) is True: #if the factor is a prime number, add it to the list.
                    prime_fact_list.append(num)
                    operand = int(operand/num) #now find a factor of the rest of the number, since we have already taken out one of the prime factors. 
                
                    break # for that, the loop breaks and the program finds the next smallest prime factor. This also allows the program to make a list with acending order of factors
            if (num * (num + 2)) > operand: #REFFER TO LINE 16
                prime_fact_list.append(operand)
                operand = 1
                break




    # if check_prime(operand) is True:
    #     prime_fact_list.append(operand)
    # else:
    #     while operand != 1:
    #         for num in range(1, operand +1):
    #             if operand%num == 0: #first up, find a factor of the number
    #                 if check_prime(num) is True: #if the factor is a prime number, add it to the list.
    #                     prime_fact_list.append(num)
    #                     operand = int(operand/num) #now find a factor of the rest of the number, since we have already taken out one of the prime factors. 
                
                        #break # for that, the loop breaks and the program finds the next smallest prime factor. This also allows the program to make a list with acending order of factors
    # I dont want an entire list of all factors, I want it to be short and precise. So instead of the entire expanded form, i want exponential form.

    prime_fact_exp_list = []
    prime_checked = []
    for prime_num in prime_fact_list:
        if prime_num not in prime_checked:
            prime_checked.append(prime_num)
            num_count = prime_fact_list.count(prime_num)
            if num_count > 1:
                prime_fact_exp_list.append(f"{prime_num}^{num_count}")
            if num_count == 1:
                prime_fact_exp_list.append(str(prime_num))
    
    prime_factorization = ''
    for item in prime_fact_exp_list[:-1]:
        prime_factorization += item + ' * '
    prime_factorization += prime_fact_exp_list[-1]
            

    return prime_factorization


for num in range(2, 20000001):
    if num % 2000000 == 0:
        print(prime_factorize(num))
    else:
        prime_factorize(num)       

