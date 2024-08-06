def fabonacci(n):
    if 1 <= n <=2:
        return 1
    if n == 0:
        return 0
    return fabonacci(n-1) + fabonacci(n-2)
    

try:
    n = int(input())
    if n < 0:
        print('n iz a natural number')
    else:
        print(fabonacci(n))
except:
    print('invalid input')