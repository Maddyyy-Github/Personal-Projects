
def check_prime_num(number):

    devisor = 1
    factors = []

    while devisor <= number:
    
        r = number % devisor
    
        if r == 0:
            q = number/devisor
            factors.append(int(q))
        
        devisor += 1

    if len(factors) == 2:
        return "It is a prime number"

    else:
        return 'It is not a prime number'

def check_prime(start, stop=0):
    prime_numbers_list = []
    if stop == False:
        print(check_prime_num(start))
    if stop > start and stop > 0:
        for number_range in range(start, (stop + 1)):
            if check_prime_num(number_range) == "It is a prime number":
                prime_numbers_list.append(number_range)

        if len(prime_numbers_list) == 0:
            message = 'There are no prime numbers in the given range'
        elif len(prime_numbers_list) == 1:
            message = f'{str(prime_numbers_list[0])} was the only prime number in the given range'
        else:
            message = 'The following are the prime numbers in the given range:'
            for number in prime_numbers_list:
                message += '\n' + str(number)
        
        print(message)


    
while True:
    user_input = input('Enter a number [or range as "start, stop"]:')
    try:
        exec(f'check_prime({user_input})')
    except:
        print("An error occured, try again.")
    else:
        break
