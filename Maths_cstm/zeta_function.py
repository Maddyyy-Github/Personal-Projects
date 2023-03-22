from math import exp
terms = 100
prev = 0


def zeta(x, type='decimals'):
    series = []
    for number in range(1, terms+1):
        if type == 'decimals':
            term = 1/(number**x)
        else:
            term = f'1/{number**x}'

        series.append(term)
    return series

# list = []
# for term in zeta(1,'fractions'):
#     list.append(eval(term))

# print(list)
def zeta_sum(x):
    zeta_series = zeta(x)
    sum = 0
    for number in zeta_series:
        sum += number
    return sum

val = 1
print(f'Zeta({val})')
for number in range(20):
    # terms = round(2.718**number)
    terms = round(exp(number))
    current = zeta_sum(val)

    # print(f'terms = {terms}\t{zeta_sum(1)}')
    print(f"{number}\t{terms}\t{current - prev}\t{current}")
    prev = current