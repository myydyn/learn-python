
def sum_number (number, option):
    sum_n = 0
    while number > 0:
        if number % 2 == option:
            sum_n += number % 10
        number = number // 10
    return sum_n

def miltiple (number):
    return sum_number (number, 0) * sum_number(number, 1)

n = int(input())
if n <0:
    print('n has to greater than 0')

else:
    print(miltiple(n))